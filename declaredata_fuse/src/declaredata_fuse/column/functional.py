from dataclasses import dataclass
from declaredata_fuse.column.basic import BasicColumn
from declaredata_fuse.column.base import Column
from declaredata_fuse.proto import sds_pb2
from declaredata_fuse.window import WindowSpec


@dataclass(frozen=True)
class FunctionalColumn(BasicColumn):
    """
    A column that is derived by calling a function to aggregate grouped
    rows or to summarize a window of rows.
    """

    function: sds_pb2.Function.ValueType
    args: list[str]
    window_spec: WindowSpec | None = None

    @staticmethod
    def col_name(func_name: str, *cols: str) -> str:
        arg_list = ", ".join(cols)
        return f"{func_name}({arg_list})"

    def alias(self, new_name: str) -> Column:
        return FunctionalColumn(
            _name=new_name,
            function=self.function,
            args=self.args,
            window_spec=self.window_spec,
        )

    def cur_name(self) -> str:
        return self._name

    def over(self, window: WindowSpec) -> "Column":
        return FunctionalColumn(
            _name=self._name,
            function=self.function,
            args=self.args,
            window_spec=window,
        )

    def to_pb(self) -> sds_pb2.Column:
        window = self.window_spec.to_pb2() if self.window_spec is not None else None
        return sds_pb2.Column(
            col_functional=sds_pb2.FunctionalColumn(
                name=self.cur_name(),
                function=self.function,
                params=self.args,
            ),
            window=window,
        )
