"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SortDirection:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SortDirectionEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _SortDirection.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ASC: _SortDirection.ValueType  # 0
    DESC: _SortDirection.ValueType  # 1

class SortDirection(_SortDirection, metaclass=_SortDirectionEnumTypeWrapper): ...

ASC: SortDirection.ValueType  # 0
DESC: SortDirection.ValueType  # 1
global___SortDirection = SortDirection

class _AggOperation:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AggOperationEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _AggOperation.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SUM: _AggOperation.ValueType  # 0
    COUNT: _AggOperation.ValueType  # 1
    MIN: _AggOperation.ValueType  # 2
    MAX: _AggOperation.ValueType  # 3
    FIRST: _AggOperation.ValueType  # 4
    LAST: _AggOperation.ValueType  # 5

class AggOperation(_AggOperation, metaclass=_AggOperationEnumTypeWrapper): ...

SUM: AggOperation.ValueType  # 0
COUNT: AggOperation.ValueType  # 1
MIN: AggOperation.ValueType  # 2
MAX: AggOperation.ValueType  # 3
FIRST: AggOperation.ValueType  # 4
LAST: AggOperation.ValueType  # 5
global___AggOperation = AggOperation

class _NullValue:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _NullValueEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NullValue.ValueType],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NULL: _NullValue.ValueType  # 0

class NullValue(_NullValue, metaclass=_NullValueEnumTypeWrapper):
    """used to represent a null value in a row"""

NULL: NullValue.ValueType  # 0
global___NullValue = NullValue

class _JoinType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _JoinTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JoinType.ValueType],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INNER: _JoinType.ValueType  # 0
    LEFT: _JoinType.ValueType  # 1
    RIGHT: _JoinType.ValueType  # 2
    FULL: _JoinType.ValueType  # 3

class JoinType(_JoinType, metaclass=_JoinTypeEnumTypeWrapper): ...

INNER: JoinType.ValueType  # 0
LEFT: JoinType.ValueType  # 1
RIGHT: JoinType.ValueType  # 2
FULL: JoinType.ValueType  # 3
global___JoinType = JoinType

@typing.final
class Empty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Empty = Empty

@typing.final
class ExecuteSqlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_UID_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    session_uid: builtins.str
    query: builtins.str
    def __init__(
        self,
        *,
        session_uid: builtins.str = ...,
        query: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal["query", b"query", "session_uid", b"session_uid"],
    ) -> None: ...

global___ExecuteSqlRequest = ExecuteSqlRequest

@typing.final
class SessionUID(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_UID_FIELD_NUMBER: builtins.int
    session_uid: builtins.str
    def __init__(
        self,
        *,
        session_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["session_uid", b"session_uid"]
    ) -> None: ...

global___SessionUID = SessionUID

@typing.final
class DataFrameUID(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATAFRAME_UID_FIELD_NUMBER: builtins.int
    dataframe_uid: builtins.str
    def __init__(
        self,
        *,
        dataframe_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["dataframe_uid", b"dataframe_uid"]
    ) -> None: ...

global___DataFrameUID = DataFrameUID

@typing.final
class SaveDataFrameAsTableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATAFRAME_UID_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    dataframe_uid: builtins.str
    table_name: builtins.str
    def __init__(
        self,
        *,
        dataframe_uid: builtins.str = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "dataframe_uid", b"dataframe_uid", "table_name", b"table_name"
        ],
    ) -> None: ...

global___SaveDataFrameAsTableRequest = SaveDataFrameAsTableRequest

@typing.final
class LoadFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_ID_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    source: builtins.str
    def __init__(
        self,
        *,
        session_id: builtins.str = ...,
        source: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal["session_id", b"session_id", "source", b"source"],
    ) -> None: ...

global___LoadFileRequest = LoadFileRequest

@typing.final
class PrettyPrintDataframeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    content: builtins.str
    def __init__(
        self,
        *,
        content: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["content", b"content"]) -> None: ...

global___PrettyPrintDataframeResponse = PrettyPrintDataframeResponse

@typing.final
class LimitDataFrameRequest(google.protobuf.message.Message):
    """limit a dataframe to fields in the range [start, end)

    (includes start but not end)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATAFRAME_UID_FIELD_NUMBER: builtins.int
    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    dataframe_uid: builtins.str
    start: builtins.int
    end: builtins.int
    def __init__(
        self,
        *,
        dataframe_uid: builtins.str = ...,
        start: builtins.int = ...,
        end: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "dataframe_uid", b"dataframe_uid", "end", b"end", "start", b"start"
        ],
    ) -> None: ...

global___LimitDataFrameRequest = LimitDataFrameRequest

@typing.final
class CSVOutput(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    content: builtins.str
    def __init__(
        self,
        *,
        content: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["content", b"content"]) -> None: ...

global___CSVOutput = CSVOutput

@typing.final
class SortDataFrameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATAFRAME_UID_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    dataframe_uid: builtins.str
    @property
    def columns(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___SortColumn
    ]: ...
    def __init__(
        self,
        *,
        dataframe_uid: builtins.str = ...,
        columns: collections.abc.Iterable[global___SortColumn] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "columns", b"columns", "dataframe_uid", b"dataframe_uid"
        ],
    ) -> None: ...

global___SortDataFrameRequest = SortDataFrameRequest

@typing.final
class FilterCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LEFT_FIELD_NUMBER: builtins.int
    OPERATOR_FIELD_NUMBER: builtins.int
    RIGHT_FIELD_NUMBER: builtins.int
    left: builtins.str
    operator: builtins.str
    right: builtins.str
    def __init__(
        self,
        *,
        left: builtins.str = ...,
        operator: builtins.str = ...,
        right: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "left", b"left", "operator", b"operator", "right", b"right"
        ],
    ) -> None: ...

global___FilterCondition = FilterCondition

@typing.final
class FilterDataFrameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATAFRAME_UID_FIELD_NUMBER: builtins.int
    CONDITIONS_FIELD_NUMBER: builtins.int
    dataframe_uid: builtins.str
    @property
    def conditions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___FilterCondition
    ]: ...
    def __init__(
        self,
        *,
        dataframe_uid: builtins.str = ...,
        conditions: collections.abc.Iterable[global___FilterCondition] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "conditions", b"conditions", "dataframe_uid", b"dataframe_uid"
        ],
    ) -> None: ...

global___FilterDataFrameRequest = FilterDataFrameRequest

@typing.final
class AggregateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATAFRAME_UID_FIELD_NUMBER: builtins.int
    GROUP_BY_FIELD_NUMBER: builtins.int
    AGGS_FIELD_NUMBER: builtins.int
    dataframe_uid: builtins.str
    @property
    def group_by(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    @property
    def aggs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Agg
    ]: ...
    def __init__(
        self,
        *,
        dataframe_uid: builtins.str = ...,
        group_by: collections.abc.Iterable[builtins.str] | None = ...,
        aggs: collections.abc.Iterable[global___Agg] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "aggs", b"aggs", "dataframe_uid", b"dataframe_uid", "group_by", b"group_by"
        ],
    ) -> None: ...

global___AggregateRequest = AggregateRequest

@typing.final
class SortColumn(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COL_NAME_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    col_name: builtins.str
    direction: global___SortDirection.ValueType
    def __init__(
        self,
        *,
        col_name: builtins.str = ...,
        direction: global___SortDirection.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal["col_name", b"col_name", "direction", b"direction"],
    ) -> None: ...

global___SortColumn = SortColumn

@typing.final
class Agg(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COL_NAME_FIELD_NUMBER: builtins.int
    OP_FIELD_NUMBER: builtins.int
    ALIAS_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    col_name: builtins.str
    op: global___AggOperation.ValueType
    alias: builtins.str
    @property
    def window(self) -> global___WindowSpec: ...
    def __init__(
        self,
        *,
        col_name: builtins.str = ...,
        op: global___AggOperation.ValueType = ...,
        alias: builtins.str | None = ...,
        window: global___WindowSpec | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "_alias",
            b"_alias",
            "_window",
            b"_window",
            "alias",
            b"alias",
            "window",
            b"window",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_alias",
            b"_alias",
            "_window",
            b"_window",
            "alias",
            b"alias",
            "col_name",
            b"col_name",
            "op",
            b"op",
            "window",
            b"window",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing.Literal["_alias", b"_alias"]
    ) -> typing.Literal["alias"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing.Literal["_window", b"_window"]
    ) -> typing.Literal["window"] | None: ...

global___Agg = Agg

@typing.final
class WithColumnRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATAFRAME_UID_FIELD_NUMBER: builtins.int
    NEW_COL_NAME_FIELD_NUMBER: builtins.int
    AGGREGATION_FIELD_NUMBER: builtins.int
    dataframe_uid: builtins.str
    """the DataFrame from which to compute the new column"""
    new_col_name: builtins.str
    """the name of the new column. the new column will be available
    in a _new_ dataframe. the existing one will not be modified
    """
    @property
    def aggregation(self) -> global___Agg:
        """the aggregation to be applied, to create the new column"""

    def __init__(
        self,
        *,
        dataframe_uid: builtins.str = ...,
        new_col_name: builtins.str = ...,
        aggregation: global___Agg | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["aggregation", b"aggregation"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "aggregation",
            b"aggregation",
            "dataframe_uid",
            b"dataframe_uid",
            "new_col_name",
            b"new_col_name",
        ],
    ) -> None: ...

global___WithColumnRequest = WithColumnRequest

@typing.final
class WindowSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARTITION_BY_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    LEFT_BOUNDARY_FIELD_NUMBER: builtins.int
    RIGHT_BOUNDARY_FIELD_NUMBER: builtins.int
    partition_by: builtins.str
    order_by: builtins.str
    left_boundary: builtins.int
    right_boundary: builtins.int
    def __init__(
        self,
        *,
        partition_by: builtins.str = ...,
        order_by: builtins.str = ...,
        left_boundary: builtins.int = ...,
        right_boundary: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "left_boundary",
            b"left_boundary",
            "order_by",
            b"order_by",
            "partition_by",
            b"partition_by",
            "right_boundary",
            b"right_boundary",
        ],
    ) -> None: ...

global___WindowSpec = WindowSpec

@typing.final
class Row(google.protobuf.message.Message):
    """the data in a single DataFrame row, including the column names.

    we purposely do not deduplicate column names in case a set of rows
    have heterogenous data
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class DataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Value: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Value | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self, field_name: typing.Literal["key", b"key", "value", b"value"]
        ) -> None: ...

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___Value
    ]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Mapping[builtins.str, global___Value] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data"]) -> None: ...

global___Row = Row

@typing.final
class Value(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STRING_VALUE_FIELD_NUMBER: builtins.int
    INT64_VALUE_FIELD_NUMBER: builtins.int
    INT32_VALUE_FIELD_NUMBER: builtins.int
    BYTES_VALUE_FIELD_NUMBER: builtins.int
    NULL_VALUE_FIELD_NUMBER: builtins.int
    string_value: builtins.str
    int64_value: builtins.int
    int32_value: builtins.int
    bytes_value: builtins.bytes
    null_value: global___NullValue.ValueType
    def __init__(
        self,
        *,
        string_value: builtins.str = ...,
        int64_value: builtins.int = ...,
        int32_value: builtins.int = ...,
        bytes_value: builtins.bytes = ...,
        null_value: global___NullValue.ValueType = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "bytes_value",
            b"bytes_value",
            "int32_value",
            b"int32_value",
            "int64_value",
            b"int64_value",
            "null_value",
            b"null_value",
            "string_value",
            b"string_value",
            "value",
            b"value",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "bytes_value",
            b"bytes_value",
            "int32_value",
            b"int32_value",
            "int64_value",
            b"int64_value",
            "null_value",
            b"null_value",
            "string_value",
            b"string_value",
            "value",
            b"value",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["value", b"value"]
    ) -> (
        typing.Literal[
            "string_value", "int64_value", "int32_value", "bytes_value", "null_value"
        ]
        | None
    ): ...

global___Value = Value

@typing.final
class DataFrameContents(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROWS_FIELD_NUMBER: builtins.int
    @property
    def rows(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Row
    ]: ...
    def __init__(
        self,
        *,
        rows: collections.abc.Iterable[global___Row] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["rows", b"rows"]) -> None: ...

global___DataFrameContents = DataFrameContents

@typing.final
class SelectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DF_UID_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    df_uid: builtins.str
    @property
    def columns(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Column
    ]: ...
    def __init__(
        self,
        *,
        df_uid: builtins.str = ...,
        columns: collections.abc.Iterable[global___Column] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["columns", b"columns", "df_uid", b"df_uid"]
    ) -> None: ...

global___SelectRequest = SelectRequest

@typing.final
class Column(google.protobuf.message.Message):
    """The definition of a column in Fuse.

    This is either a reference to an existing column or a specification
    for how to compute a new column, possibly from an existing column.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COL_NAME_FIELD_NUMBER: builtins.int
    COL_DERIVED_FIELD_NUMBER: builtins.int
    COL_LIT_FIELD_NUMBER: builtins.int
    COL_COALESCE_FIELD_NUMBER: builtins.int
    col_name: builtins.str
    @property
    def col_derived(self) -> global___NamedDerivedColumn: ...
    @property
    def col_lit(self) -> global___LiteralColumn: ...
    @property
    def col_coalesce(self) -> global___CoalesceColumn: ...
    def __init__(
        self,
        *,
        col_name: builtins.str = ...,
        col_derived: global___NamedDerivedColumn | None = ...,
        col_lit: global___LiteralColumn | None = ...,
        col_coalesce: global___CoalesceColumn | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "col_coalesce",
            b"col_coalesce",
            "col_derived",
            b"col_derived",
            "col_lit",
            b"col_lit",
            "col_name",
            b"col_name",
            "col_spec",
            b"col_spec",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "col_coalesce",
            b"col_coalesce",
            "col_derived",
            b"col_derived",
            "col_lit",
            b"col_lit",
            "col_name",
            b"col_name",
            "col_spec",
            b"col_spec",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["col_spec", b"col_spec"]
    ) -> (
        typing.Literal["col_name", "col_derived", "col_lit", "col_coalesce"] | None
    ): ...

global___Column = Column

@typing.final
class NamedDerivedColumn(google.protobuf.message.Message):
    """A new column that is derived by performing a binary operation
    on an existing column with a constant. for example:

     existing_col + 2

    The following expression would _not_ be supported by
    ConstBinaryOpDerivedColumn

     existing_col + other_existing_col

    because this is not an expression representing an existing column with a
    binary operation applied to a constant (it's applied to a 2nd existing
    column)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SRC_COL_FIELD_NUMBER: builtins.int
    NEW_COL_FIELD_NUMBER: builtins.int
    OPERATOR_FIELD_NUMBER: builtins.int
    STR_VAL_FIELD_NUMBER: builtins.int
    I32_VAL_FIELD_NUMBER: builtins.int
    I64_VAL_FIELD_NUMBER: builtins.int
    src_col: builtins.str
    new_col: builtins.str
    operator: builtins.str
    str_val: builtins.str
    i32_val: builtins.int
    i64_val: builtins.int
    def __init__(
        self,
        *,
        src_col: builtins.str = ...,
        new_col: builtins.str = ...,
        operator: builtins.str = ...,
        str_val: builtins.str = ...,
        i32_val: builtins.int = ...,
        i64_val: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "constant",
            b"constant",
            "i32_val",
            b"i32_val",
            "i64_val",
            b"i64_val",
            "str_val",
            b"str_val",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "constant",
            b"constant",
            "i32_val",
            b"i32_val",
            "i64_val",
            b"i64_val",
            "new_col",
            b"new_col",
            "operator",
            b"operator",
            "src_col",
            b"src_col",
            "str_val",
            b"str_val",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["constant", b"constant"]
    ) -> typing.Literal["str_val", "i32_val", "i64_val"] | None: ...

global___NamedDerivedColumn = NamedDerivedColumn

@typing.final
class TypedAny(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STR_VAL_FIELD_NUMBER: builtins.int
    I32_VAL_FIELD_NUMBER: builtins.int
    I64_VAL_FIELD_NUMBER: builtins.int
    str_val: builtins.str
    i32_val: builtins.str
    i64_val: builtins.str
    def __init__(
        self,
        *,
        str_val: builtins.str = ...,
        i32_val: builtins.str = ...,
        i64_val: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "i32_val",
            b"i32_val",
            "i64_val",
            b"i64_val",
            "str_val",
            b"str_val",
            "value",
            b"value",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "i32_val",
            b"i32_val",
            "i64_val",
            b"i64_val",
            "str_val",
            b"str_val",
            "value",
            b"value",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["value", b"value"]
    ) -> typing.Literal["str_val", "i32_val", "i64_val"] | None: ...

global___TypedAny = TypedAny

@typing.final
class LiteralColumn(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VAL_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def val(self) -> global___TypedAny: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        val: global___TypedAny | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["val", b"val"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["name", b"name", "val", b"val"]
    ) -> None: ...

global___LiteralColumn = LiteralColumn

@typing.final
class CoalesceColumn(google.protobuf.message.Message):
    """A new column that is created from choosing the first non-null value from
    one or more columns in a row.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    COLS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """the name of the new column"""
    @property
    def cols(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cols: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["cols", b"cols", "name", b"name"]
    ) -> None: ...

global___CoalesceColumn = CoalesceColumn

@typing.final
class DropRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DF_UID_FIELD_NUMBER: builtins.int
    COL_NAMES_FIELD_NUMBER: builtins.int
    df_uid: builtins.str
    @property
    def col_names(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    def __init__(
        self,
        *,
        df_uid: builtins.str = ...,
        col_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["col_names", b"col_names", "df_uid", b"df_uid"]
    ) -> None: ...

global___DropRequest = DropRequest

@typing.final
class JoinRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DF_UID_1_FIELD_NUMBER: builtins.int
    DF_UID_2_FIELD_NUMBER: builtins.int
    JOIN_TYPE_FIELD_NUMBER: builtins.int
    LEFT_COLS_FIELD_NUMBER: builtins.int
    RIGHT_COLS_FIELD_NUMBER: builtins.int
    df_uid_1: builtins.str
    df_uid_2: builtins.str
    join_type: global___JoinType.ValueType
    @property
    def left_cols(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    @property
    def right_cols(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    def __init__(
        self,
        *,
        df_uid_1: builtins.str = ...,
        df_uid_2: builtins.str = ...,
        join_type: global___JoinType.ValueType = ...,
        left_cols: collections.abc.Iterable[builtins.str] | None = ...,
        right_cols: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "df_uid_1",
            b"df_uid_1",
            "df_uid_2",
            b"df_uid_2",
            "join_type",
            b"join_type",
            "left_cols",
            b"left_cols",
            "right_cols",
            b"right_cols",
        ],
    ) -> None: ...

global___JoinRequest = JoinRequest

@typing.final
class UnionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DF_UID_1_FIELD_NUMBER: builtins.int
    DF_UID_2_FIELD_NUMBER: builtins.int
    df_uid_1: builtins.str
    df_uid_2: builtins.str
    def __init__(
        self,
        *,
        df_uid_1: builtins.str = ...,
        df_uid_2: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal["df_uid_1", b"df_uid_1", "df_uid_2", b"df_uid_2"],
    ) -> None: ...

global___UnionRequest = UnionRequest
