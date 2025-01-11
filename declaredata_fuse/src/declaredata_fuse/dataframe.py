from dataclasses import dataclass
from typing import Any

from declaredata_fuse.dataframe_impl.collect import collect_impl
from declaredata_fuse.dataframe_impl.drop import drop_impl
from declaredata_fuse.dataframe_impl.select import select_impl
from declaredata_fuse.dataframe_impl.sort import to_sorted_col_list
from declaredata_fuse.proto import sds_pb2, sds_pb2_grpc
from declaredata_fuse.column import BasicColumn, Column, Condition, SortedColumn
from declaredata_fuse.column import SelectColumn, DropColumn
from declaredata_fuse.grouped import Grouped
from declaredata_fuse.row import Row
from declaredata_fuse.dataframe_impl.join import reify_join_cols, str_to_join_type


@dataclass(frozen=True)
class DataFrameWriter:
    """
    A convenience class that knows how to write a DataFrame to a table
    that can be queried from SQL.

    Generally, instances of this class should be created by creating
    a DataFrame, then calling DataFrame.write()
    """

    df_uid: str
    stub: sds_pb2_grpc.sdsStub

    def saveAsTable(self, table_name: str) -> None:
        """
        Save the DataFrame to a table with the specified name.

        After this function successfully succeeds, you can call reference the
        new table name in FuseSession.sql, using the same FuseSession from
        which this DataFrame originated.
        """
        req = sds_pb2.SaveDataFrameAsTableRequest(
            dataframe_uid=self.df_uid,
            table_name=table_name,
        )
        self.stub.SaveDataFrameAsTable(req)  # type: ignore


@dataclass(frozen=True)
class DataFrame:
    """
    The core class in the Fuse library. DataFrame represents tabular data that
    has the following properties:

    - It either came directly from a FuseSession (i.e. via a call to
        FuseSession.read.csv()), or came from an operation on an existing
        DataFrame
    - It is "owned" by exactly one FuseSession - when its owner is destroyed
        with a call to FuseSession.stop, it (and all other DataFrames owned by
        that FuseSession) are immediately invalidated and deleted
    - It is _lazy_ - most operations may return very quickly and will only be
        _evaluated_ when the data is actually requested. Eager (non-lazy)
        operations will be clearly documented.
    - It it _immutable_ - all mutating operations will return a _new_
        DataFrame that reflects the changes.
    """

    df_uid: str
    """The unique ID of this DataFrame. Do not modify"""
    stub: sds_pb2_grpc.sdsStub
    """The connection to the Fuse server. Do not modify"""

    @property
    def write(self) -> DataFrameWriter:
        """
        Prepare this DataFrame to have its contents written to a table
        so that it can be queried from SQL. See documentation under
        DataFrameWriter for more details.
        """
        return DataFrameWriter(df_uid=self.df_uid, stub=self.stub)

    def pretty_print(self) -> None:
        """Alias of display"""
        request = sds_pb2.DataFrameUID(
            dataframe_uid=self.df_uid,
        )
        response = self.stub.PrettyPrintDataframe(request)  # type: ignore
        print(
            response.content  # type: ignore
        )

    def display(self) -> None:
        """
        Collect all the data in this DataFrame (this is an eager evaluation),
        format it in a human-readable way, and print it to stdout.
        """
        self.pretty_print()

    def show(self, n: int) -> None:
        """Alias of self.limit(0, n).display()"""
        self.limit(0, n).display()

    def limit(self, start: int, end: int) -> "DataFrame":
        """
        Return a new DataFrame with only the rows in the range [start, end]
        (inclusive on both sides).
        """
        req = sds_pb2.LimitDataFrameRequest(
            dataframe_uid=self.df_uid, start=start, end=end
        )
        resp = self.stub.LimitDataFrame(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )

    def take(self, num: int) -> list[Row]:
        """
        Get the first num rows from this DataFrame and return them
        as a list of Row

        See the following pyspark documentation for more:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.take.html
        """
        return self.limit(0, num).collect()

    def collect(self) -> list[Row]:
        return collect_impl(df_uid=self.df_uid, stub=self.stub)

    def select(self, *cols: SelectColumn) -> "DataFrame":
        new_uid = select_impl(df_uid=self.df_uid, stub=self.stub, cols=list(cols))
        return DataFrame(df_uid=new_uid, stub=self.stub)

    def drop(self, *cols: DropColumn) -> "DataFrame":
        new_uid = drop_impl(df_uid=self.df_uid, stub=self.stub, cols=list(cols))
        return DataFrame(df_uid=new_uid, stub=self.stub)

    def groupBy(self, col_name: str | list[str]) -> Grouped:
        """
        Start building an aggregation on this DataFrame. Start by grouping
        the rows by the values in the given column or columns.
        """
        return Grouped(
            df_uid=self.df_uid,
            stub=self.stub,
            group_cols=([col_name] if isinstance(col_name, str) else col_name),
        )

    def __getattr__(self, name: str) -> BasicColumn:
        """
        Convenience method for referencing a column in this DataFrame.

        Allows you to do the following (assuming mydf is a DataFrame with
        column mycol)

            mydf.mycol

        See the following pyspark documentation for more:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.__getattr__.html
        """
        return BasicColumn(_name=name)

    def __getitem__(self, name: str) -> Column:
        """
        Convenience method for referencing a column in this DataFrame

        Allows you to do the following (assuming mydf is a DataFrame with
        column mycol)

            mydf["mycol"]

        See the following pyspark documentation for more:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.__getitem__.html?highlight=__getitem__#pyspark.sql.DataFrame.__getitem__
        """
        return self.__getattr__(name)

    def export_csv(self) -> str:
        """
        Eagerly evaluate the DataFrame, collect all its data, format it as
        a CSV, and return the CSV contents as a str
        """
        req = sds_pb2.DataFrameUID(dataframe_uid=self.df_uid)
        resp = self.stub.ExportCSV(req)  # type: ignore
        return resp.content  # type: ignore

    def sort_typed(self, cols: list[SortedColumn]) -> "DataFrame":
        """
        Sort the rows in this DataFrame based on the values in the given column.

        This is a strongly-typed method for sorting, not included in the
        standard pyspark API. Use DataFrame.sort for the compatible version.
        """
        pb_cols = [col.to_pb() for col in cols]
        req = sds_pb2.SortDataFrameRequest(
            dataframe_uid=self.df_uid,
            columns=pb_cols,
        )
        resp = self.stub.SortDataFrame(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )

    def sort(
        self, *cols: str | Column | list[str | Column], **kwargs: Any
    ) -> "DataFrame":
        """
        Sort the rows in this DataFrame based on the given columns. Directions
        can be set individually on each column, or globally with the ascending
        keyword.

        For more, see pyspark documentation:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.sort.html?highlight=sort#pyspark.sql.DataFrame.sort
        """
        sorted_cols_list = to_sorted_col_list(*cols, **kwargs)
        return self.sort_typed(sorted_cols_list)

    def orderBy(
        self, *cols: str | Column | list[str | Column], **kwargs: Any
    ) -> "DataFrame":
        """
        Alias for self.sort(*cols, **kwargs)

        For more, see pyspark documentation:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.orderBy.html?highlight=orderby#pyspark.sql.DataFrame.orderBy
        """
        sorted_cols_list = to_sorted_col_list(*cols, **kwargs)
        return self.sort_typed(sorted_cols_list)

    def filter(self, condition: Condition) -> "DataFrame":
        """
        Return a new DataFrame with rows filtered out from this DataFrame, using
        the given filter condition.
        """
        pb_cond = condition.to_pb()
        req = sds_pb2.FilterDataFrameRequest(
            dataframe_uid=self.df_uid,
            conditions=[pb_cond],
        )
        resp = self.stub.FilterDataFrame(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )

    def where(self, condition: Condition) -> "DataFrame":
        """An alias for df.filter(self, condition)"""
        return self.filter(condition)

    def withColumn(self, new_col_name: str, col: Column) -> "DataFrame":
        """
        Return a new DataFrame with a single column added to it with the given
        name. Values in the new column will be calculated by the given function.
        """
        assert col is not None
        req = sds_pb2.WithColumnRequest(
            name=new_col_name,
            dataframe_uid=self.df_uid,
            new_col=col.to_pb(),
        )
        resp = self.stub.WithColumn(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )
    
    def withColumns(self, cols_dict: dict[str, Column]) -> "DataFrame":
        df = self
        for col_name, col in cols_dict.items():
            df = df.withColumn(col_name, col)
        return df

    def join(
        self,
        other: "DataFrame",
        on: list[str] | str | Column | None = None,
        how: str | None = None,
    ):
        """
        Join this DataFrame to the given 'other' one
        """
        join_type = str_to_join_type(how or "inner")
        on_reified = reify_join_cols(on)
        req = sds_pb2.JoinRequest(
            df_uid_1=self.df_uid,
            df_uid_2=other.df_uid,
            join_type=join_type,
            left_cols=on_reified,
            right_cols=on_reified,
        )
        resp = self.stub.Join(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )

    def union(self, other: "DataFrame") -> "DataFrame":
        req = sds_pb2.UnionRequest(df_uid_1=self.df_uid, df_uid_2=other.df_uid)
        resp = self.stub.Union(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )

    def distinct(self) -> "DataFrame":
        """
        Return a new `DataFrame` with de-duplicated rows.

        Equivalent to the `PySpark` `DataFrame.distinct` function:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.distinct.html
        """
        req = sds_pb2.DataFrameUID(dataframe_uid=self.df_uid)
        resp = self.stub.Distinct(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )

    def alias(self, new_name: str) -> "DataFrame":
        """
        Create a new `DataFrame`  whose columns and rows are equivalent to
        `self`, but all column names are prefixed with `new_name`.

        Equivalent to the PySpark `DataFrame.alias` function:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.alias.html
        """
        req = sds_pb2.AliasRequest(df_uid=self.df_uid, alias_prefix=new_name)
        resp = self.stub.Alias(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )
