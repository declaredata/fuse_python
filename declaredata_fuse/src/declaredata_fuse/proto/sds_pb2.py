# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/sds.proto
# Protobuf Python Version: 5.27.4
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    4,
    '',
    'proto/sds.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fproto/sds.proto\x12\x03sds\"\x07\n\x05\x45mpty\"J\n\x11\x45xecuteSqlRequest\x12\x1f\n\x0bsession_uid\x18\x01 \x01(\tR\nsessionUid\x12\x14\n\x05query\x18\x02 \x01(\tR\x05query\"-\n\nSessionUID\x12\x1f\n\x0bsession_uid\x18\x01 \x01(\tR\nsessionUid\"3\n\x0c\x44\x61taFrameUID\x12#\n\rdataframe_uid\x18\x01 \x01(\tR\x0c\x64\x61taframeUid\"a\n\x1bSaveDataFrameAsTableRequest\x12#\n\rdataframe_uid\x18\x01 \x01(\tR\x0c\x64\x61taframeUid\x12\x1d\n\ntable_name\x18\x02 \x01(\tR\ttableName\"H\n\x0fLoadFileRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\"8\n\x1cPrettyPrintDataframeResponse\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"d\n\x15LimitDataFrameRequest\x12#\n\rdataframe_uid\x18\x01 \x01(\tR\x0c\x64\x61taframeUid\x12\x14\n\x05start\x18\x02 \x01(\x04R\x05start\x12\x10\n\x03\x65nd\x18\x03 \x01(\x04R\x03\x65nd\"%\n\tCSVOutput\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"f\n\x14SortDataFrameRequest\x12#\n\rdataframe_uid\x18\x01 \x01(\tR\x0c\x64\x61taframeUid\x12)\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x0f.sds.SortColumnR\x07\x63olumns\"W\n\x0f\x46ilterCondition\x12\x12\n\x04left\x18\x01 \x01(\tR\x04left\x12\x1a\n\x08operator\x18\x02 \x01(\tR\x08operator\x12\x14\n\x05right\x18\x03 \x01(\tR\x05right\"s\n\x16\x46ilterDataFrameRequest\x12#\n\rdataframe_uid\x18\x01 \x01(\tR\x0c\x64\x61taframeUid\x12\x34\n\nconditions\x18\x02 \x03(\x0b\x32\x14.sds.FilterConditionR\nconditions\"p\n\x10\x41ggregateRequest\x12#\n\rdataframe_uid\x18\x01 \x01(\tR\x0c\x64\x61taframeUid\x12\x19\n\x08group_by\x18\x02 \x03(\tR\x07groupBy\x12\x1c\n\x04\x61ggs\x18\x03 \x03(\x0b\x32\x08.sds.AggR\x04\x61ggs\"Y\n\nSortColumn\x12\x19\n\x08\x63ol_name\x18\x01 \x01(\tR\x07\x63olName\x12\x30\n\tdirection\x18\x02 \x01(\x0e\x32\x12.sds.SortDirectionR\tdirection\"h\n\x03\x41gg\x12\x19\n\x08\x63ol_name\x18\x01 \x01(\tR\x07\x63olName\x12!\n\x02op\x18\x02 \x01(\x0e\x32\x11.sds.AggOperationR\x02op\x12\x19\n\x05\x61lias\x18\x03 \x01(\tH\x00R\x05\x61lias\x88\x01\x01\x42\x08\n\x06_alias\"r\n\x11WithColumnRequest\x12#\n\rdataframe_uid\x18\x01 \x01(\tR\x0c\x64\x61taframeUid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12$\n\x07new_col\x18\x03 \x01(\x0b\x32\x0b.sds.ColumnR\x06newCol\"\x96\x01\n\nWindowSpec\x12!\n\x0cpartition_by\x18\x01 \x01(\tR\x0bpartitionBy\x12\x19\n\x08order_by\x18\x02 \x01(\tR\x07orderBy\x12#\n\rleft_boundary\x18\x03 \x01(\x04R\x0cleftBoundary\x12%\n\x0eright_boundary\x18\x04 \x01(\x04R\rrightBoundary\"r\n\x03Row\x12&\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x12.sds.Row.DataEntryR\x04\x64\x61ta\x1a\x43\n\tDataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12 \n\x05value\x18\x02 \x01(\x0b\x32\n.sds.ValueR\x05value:\x02\x38\x01\"\xcf\x01\n\x05Value\x12#\n\x0cstring_value\x18\x01 \x01(\tH\x00R\x0bstringValue\x12!\n\x0bint64_value\x18\x02 \x01(\x03H\x00R\nint64Value\x12!\n\x0bint32_value\x18\x03 \x01(\x05H\x00R\nint32Value\x12!\n\x0b\x62ytes_value\x18\x04 \x01(\x0cH\x00R\nbytesValue\x12/\n\nnull_value\x18\x05 \x01(\x0e\x32\x0e.sds.NullValueH\x00R\tnullValueB\x07\n\x05value\"1\n\x11\x44\x61taFrameContents\x12\x1c\n\x04rows\x18\x02 \x03(\x0b\x32\x08.sds.RowR\x04rows\"M\n\rSelectRequest\x12\x15\n\x06\x64\x66_uid\x18\x01 \x01(\tR\x05\x64\x66Uid\x12%\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x0b.sds.ColumnR\x07\x63olumns\"\x8f\x02\n\x06\x43olumn\x12\x1b\n\x08\x63ol_name\x18\x01 \x01(\tH\x00R\x07\x63olName\x12:\n\x0b\x63ol_derived\x18\x02 \x01(\x0b\x32\x17.sds.NamedDerivedColumnH\x00R\ncolDerived\x12-\n\x07\x63ol_lit\x18\x03 \x01(\x0b\x32\x12.sds.LiteralColumnH\x00R\x06\x63olLit\x12\x38\n\x0c\x63ol_coalesce\x18\x04 \x01(\x0b\x32\x13.sds.CoalesceColumnH\x00R\x0b\x63olCoalesce\x12,\n\x06window\x18\x05 \x01(\x0b\x32\x0f.sds.WindowSpecH\x01R\x06window\x88\x01\x01\x42\n\n\x08\x63ol_specB\t\n\x07_window\"\xbf\x01\n\x12NamedDerivedColumn\x12\x17\n\x07src_col\x18\x01 \x01(\tR\x06srcCol\x12\x17\n\x07new_col\x18\x02 \x01(\tR\x06newCol\x12\x1a\n\x08operator\x18\x03 \x01(\tR\x08operator\x12\x19\n\x07str_val\x18\x04 \x01(\tH\x00R\x06strVal\x12\x19\n\x07i32_val\x18\x05 \x01(\x05H\x00R\x06i32Val\x12\x19\n\x07i64_val\x18\x06 \x01(\x03H\x00R\x06i64ValB\n\n\x08\x63onstant\"d\n\x08TypedAny\x12\x19\n\x07str_val\x18\x01 \x01(\tH\x00R\x06strVal\x12\x19\n\x07i32_val\x18\x02 \x01(\tH\x00R\x06i32Val\x12\x19\n\x07i64_val\x18\x03 \x01(\tH\x00R\x06i64ValB\x07\n\x05value\"D\n\rLiteralColumn\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x03val\x18\x02 \x01(\x0b\x32\r.sds.TypedAnyR\x03val\"8\n\x0e\x43oalesceColumn\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\"A\n\x0b\x44ropRequest\x12\x15\n\x06\x64\x66_uid\x18\x01 \x01(\tR\x05\x64\x66Uid\x12\x1b\n\tcol_names\x18\x02 \x03(\tR\x08\x63olNames\"\xa9\x01\n\x0bJoinRequest\x12\x18\n\x08\x64\x66_uid_1\x18\x01 \x01(\tR\x06\x64\x66Uid1\x12\x18\n\x08\x64\x66_uid_2\x18\x02 \x01(\tR\x06\x64\x66Uid2\x12*\n\tjoin_type\x18\x03 \x01(\x0e\x32\r.sds.JoinTypeR\x08joinType\x12\x1b\n\tleft_cols\x18\x04 \x03(\tR\x08leftCols\x12\x1d\n\nright_cols\x18\x05 \x03(\tR\trightCols\"B\n\x0cUnionRequest\x12\x18\n\x08\x64\x66_uid_1\x18\x01 \x01(\tR\x06\x64\x66Uid1\x12\x18\n\x08\x64\x66_uid_2\x18\x02 \x01(\tR\x06\x64\x66Uid2*\"\n\rSortDirection\x12\x07\n\x03\x41SC\x10\x00\x12\x08\n\x04\x44\x45SC\x10\x01*I\n\x0c\x41ggOperation\x12\x07\n\x03SUM\x10\x00\x12\t\n\x05\x43OUNT\x10\x01\x12\x07\n\x03MIN\x10\x02\x12\x07\n\x03MAX\x10\x03\x12\t\n\x05\x46IRST\x10\x04\x12\x08\n\x04LAST\x10\x05*\x15\n\tNullValue\x12\x08\n\x04NULL\x10\x00*4\n\x08JoinType\x12\t\n\x05INNER\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x12\x08\n\x04\x46ULL\x10\x03\x32\xd3\x08\n\x03sds\x12\x37\n\nExecuteSql\x12\x16.sds.ExecuteSqlRequest\x1a\x11.sds.DataFrameUID\x12,\n\rCreateSession\x12\n.sds.Empty\x1a\x0f.sds.SessionUID\x12\x32\n\x07LoadCSV\x12\x14.sds.LoadFileRequest\x1a\x11.sds.DataFrameUID\x12\x36\n\x0bLoadParquet\x12\x14.sds.LoadFileRequest\x1a\x11.sds.DataFrameUID\x12\x33\n\x08LoadJSON\x12\x14.sds.LoadFileRequest\x1a\x11.sds.DataFrameUID\x12+\n\x0c\x43loseSession\x12\x0f.sds.SessionUID\x1a\n.sds.Empty\x12\x44\n\x14SaveDataFrameAsTable\x12 .sds.SaveDataFrameAsTableRequest\x1a\n.sds.Empty\x12L\n\x14PrettyPrintDataframe\x12\x11.sds.DataFrameUID\x1a!.sds.PrettyPrintDataframeResponse\x12?\n\x0eLimitDataFrame\x12\x1a.sds.LimitDataFrameRequest\x1a\x11.sds.DataFrameUID\x12=\n\rSortDataFrame\x12\x19.sds.SortDataFrameRequest\x1a\x11.sds.DataFrameUID\x12\x41\n\x0f\x46ilterDataFrame\x12\x1b.sds.FilterDataFrameRequest\x1a\x11.sds.DataFrameUID\x12\x35\n\tAggregate\x12\x15.sds.AggregateRequest\x1a\x11.sds.DataFrameUID\x12\x37\n\nWithColumn\x12\x16.sds.WithColumnRequest\x1a\x11.sds.DataFrameUID\x12/\n\x06Select\x12\x12.sds.SelectRequest\x1a\x11.sds.DataFrameUID\x12\x34\n\x07\x43ollect\x12\x11.sds.DataFrameUID\x1a\x16.sds.DataFrameContents\x12+\n\x04Join\x12\x10.sds.JoinRequest\x1a\x11.sds.DataFrameUID\x12\x30\n\x08\x44istinct\x12\x11.sds.DataFrameUID\x1a\x11.sds.DataFrameUID\x12-\n\x05Union\x12\x11.sds.UnionRequest\x1a\x11.sds.DataFrameUID\x12+\n\x04\x44rop\x12\x10.sds.DropRequest\x1a\x11.sds.DataFrameUID\x12.\n\tExportCSV\x12\x11.sds.DataFrameUID\x1a\x0e.sds.CSVOutputB?\n\x07\x63om.sdsB\x08SdsProtoP\x01\xa2\x02\x03SXX\xaa\x02\x03Sds\xca\x02\x03Sds\xe2\x02\x0fSds\\GPBMetadata\xea\x02\x03Sdsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.sds_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\007com.sdsB\010SdsProtoP\001\242\002\003SXX\252\002\003Sds\312\002\003Sds\342\002\017Sds\\GPBMetadata\352\002\003Sds'
  _globals['_ROW_DATAENTRY']._loaded_options = None
  _globals['_ROW_DATAENTRY']._serialized_options = b'8\001'
  _globals['_SORTDIRECTION']._serialized_start=2932
  _globals['_SORTDIRECTION']._serialized_end=2966
  _globals['_AGGOPERATION']._serialized_start=2968
  _globals['_AGGOPERATION']._serialized_end=3041
  _globals['_NULLVALUE']._serialized_start=3043
  _globals['_NULLVALUE']._serialized_end=3064
  _globals['_JOINTYPE']._serialized_start=3066
  _globals['_JOINTYPE']._serialized_end=3118
  _globals['_EMPTY']._serialized_start=24
  _globals['_EMPTY']._serialized_end=31
  _globals['_EXECUTESQLREQUEST']._serialized_start=33
  _globals['_EXECUTESQLREQUEST']._serialized_end=107
  _globals['_SESSIONUID']._serialized_start=109
  _globals['_SESSIONUID']._serialized_end=154
  _globals['_DATAFRAMEUID']._serialized_start=156
  _globals['_DATAFRAMEUID']._serialized_end=207
  _globals['_SAVEDATAFRAMEASTABLEREQUEST']._serialized_start=209
  _globals['_SAVEDATAFRAMEASTABLEREQUEST']._serialized_end=306
  _globals['_LOADFILEREQUEST']._serialized_start=308
  _globals['_LOADFILEREQUEST']._serialized_end=380
  _globals['_PRETTYPRINTDATAFRAMERESPONSE']._serialized_start=382
  _globals['_PRETTYPRINTDATAFRAMERESPONSE']._serialized_end=438
  _globals['_LIMITDATAFRAMEREQUEST']._serialized_start=440
  _globals['_LIMITDATAFRAMEREQUEST']._serialized_end=540
  _globals['_CSVOUTPUT']._serialized_start=542
  _globals['_CSVOUTPUT']._serialized_end=579
  _globals['_SORTDATAFRAMEREQUEST']._serialized_start=581
  _globals['_SORTDATAFRAMEREQUEST']._serialized_end=683
  _globals['_FILTERCONDITION']._serialized_start=685
  _globals['_FILTERCONDITION']._serialized_end=772
  _globals['_FILTERDATAFRAMEREQUEST']._serialized_start=774
  _globals['_FILTERDATAFRAMEREQUEST']._serialized_end=889
  _globals['_AGGREGATEREQUEST']._serialized_start=891
  _globals['_AGGREGATEREQUEST']._serialized_end=1003
  _globals['_SORTCOLUMN']._serialized_start=1005
  _globals['_SORTCOLUMN']._serialized_end=1094
  _globals['_AGG']._serialized_start=1096
  _globals['_AGG']._serialized_end=1200
  _globals['_WITHCOLUMNREQUEST']._serialized_start=1202
  _globals['_WITHCOLUMNREQUEST']._serialized_end=1316
  _globals['_WINDOWSPEC']._serialized_start=1319
  _globals['_WINDOWSPEC']._serialized_end=1469
  _globals['_ROW']._serialized_start=1471
  _globals['_ROW']._serialized_end=1585
  _globals['_ROW_DATAENTRY']._serialized_start=1518
  _globals['_ROW_DATAENTRY']._serialized_end=1585
  _globals['_VALUE']._serialized_start=1588
  _globals['_VALUE']._serialized_end=1795
  _globals['_DATAFRAMECONTENTS']._serialized_start=1797
  _globals['_DATAFRAMECONTENTS']._serialized_end=1846
  _globals['_SELECTREQUEST']._serialized_start=1848
  _globals['_SELECTREQUEST']._serialized_end=1925
  _globals['_COLUMN']._serialized_start=1928
  _globals['_COLUMN']._serialized_end=2199
  _globals['_NAMEDDERIVEDCOLUMN']._serialized_start=2202
  _globals['_NAMEDDERIVEDCOLUMN']._serialized_end=2393
  _globals['_TYPEDANY']._serialized_start=2395
  _globals['_TYPEDANY']._serialized_end=2495
  _globals['_LITERALCOLUMN']._serialized_start=2497
  _globals['_LITERALCOLUMN']._serialized_end=2565
  _globals['_COALESCECOLUMN']._serialized_start=2567
  _globals['_COALESCECOLUMN']._serialized_end=2623
  _globals['_DROPREQUEST']._serialized_start=2625
  _globals['_DROPREQUEST']._serialized_end=2690
  _globals['_JOINREQUEST']._serialized_start=2693
  _globals['_JOINREQUEST']._serialized_end=2862
  _globals['_UNIONREQUEST']._serialized_start=2864
  _globals['_UNIONREQUEST']._serialized_end=2930
  _globals['_SDS']._serialized_start=3121
  _globals['_SDS']._serialized_end=4228
# @@protoc_insertion_point(module_scope)
