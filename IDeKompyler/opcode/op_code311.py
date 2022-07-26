from IDeKompyler.opcode.op_code import (
    OPCODE,
    opcode,
    opmap,
    def_op,
    rm_op
)

def init():
    def_op(  1, "POP_TOP"                     , False, 0, 1)
    def_op(  2, "ROT_TWO"                     , False, 2, 2)
    def_op(  3, "ROT_THREE"                   , False, 3, 3)
    def_op(  4, "DUP_TOP"                     , False, 2, 1)
    def_op(  5, "DUP_TOP_TWO"                 , False, 4, 2)
    def_op(  9, "NOP"                         , False,-1,-1)
    def_op( 10, "UNARY_POSITIVE"              , False, 1, 1)
    def_op( 11, "UNARY_NEGATIVE"              , False, 1, 1)
    def_op( 12, "UNARY_NOT"                   , False, 1, 1)
    def_op( 15, "UNARY_INVERT"                , False, 1, 1)
    def_op( 16, "BINARY_MATRIX_MULTIPLY"      , False, 1, 2)
    def_op( 17, "INPLACE_MATRIX_MULTIPLY"     , False, 1, 2)
    def_op( 19, "BINARY_POWER"                , False, 1, 2)
    def_op( 20, "BINARY_MULTIPLY"             , False, 1, 2)
    def_op( 22, "BINARY_MODULO"               , False, 1, 2)
    def_op( 23, "BINARY_ADD"                  , False, 1, 2)
    def_op( 24, "BINARY_SUBTRACT"             , False, 1, 2)
    def_op( 25, "BINARY_SUBSCR"               , False, 1, 2)
    def_op( 26, "BINARY_FLOOR_DIVIDE"         , False, 1, 2)
    def_op( 27, "BINARY_TRUE_DIVIDE"          , False, 1, 2)
    def_op( 28, "INPLACE_FLOOR_DIVIDE"        , False, 1, 2)
    def_op( 29, "INPLACE_TRUE_DIVIDE"         , False, 1, 2)
    def_op( 50, "GET_AITER"                   , False, 1, 1)
    def_op( 51, "GET_ANEXT"                   , False, 2, 1)
    def_op( 52, "BEFORE_ASYNC_WITH"           , False, 2, 1)
    def_op( 55, "INPLACE_ADD"                 , False, 1, 2)
    def_op( 56, "INPLACE_SUBTRACT"            , False, 1, 2)
    def_op( 57, "INPLACE_MULTIPLY"            , False, 1, 2)
    def_op( 59, "INPLACE_MODULO"              , False, 1, 2)
    def_op( 60, "STORE_SUBSCR"                , False, 0, 3)
    def_op( 61, "DELETE_SUBSCR"               , False, 0, 2)
    def_op( 62, "BINARY_LSHIFT"               , False, 1, 2)
    def_op( 63, "BINARY_RSHIFT"               , False, 1, 2)
    def_op( 64, "BINARY_AND"                  , False, 1, 2)
    def_op( 65, "BINARY_XOR"                  , False, 1, 2)
    def_op( 66, "BINARY_OR"                   , False, 1, 2)
    def_op( 67, "INPLACE_POWER"               , False, 1, 2)
    def_op( 68, "GET_ITER"                    , False, 1, 1)
    def_op( 69, "GET_YIELD_FROM_ITER"         , False, 1, 1)
    def_op( 70, "PRINT_EXPR"                  , False, 0, 1)
    def_op( 71, "LOAD_BUILD_CLASS"            ,  True, 1, 0)
    def_op( 72, "YIELD_FROM"                  , False, 0, 1)
    def_op( 73, "GET_AWAITABLE"               , False, 0, 0)
    def_op( 75, "INPLACE_LSHIFT"              , False, 1, 2)
    def_op( 76, "INPLACE_RSHIFT"              , False, 1, 2)
    def_op( 77, "INPLACE_AND"                 , False, 1, 2)
    def_op( 78, "INPLACE_XOR"                 , False, 1, 2)
    def_op( 79, "INPLACE_OR"                  , False, 1, 2)
    def_op( 80, "BREAK_LOOP"                  , False, 0, 0)
    def_op( 81, "WITH_CLEANUP_START"          , False, 0, 1)
    def_op( 82, "WITH_CLEANUP_FINISH"         , False, 1, 0)
    def_op( 83, "RETURN_VALUE"                , False, 0, 1)
    def_op( 84, "IMPORT_STAR"                 , False, 0, 1)
    def_op( 85, "SETUP_ANNOTATIONS"           , False, 0, 0)
    def_op( 86, "YIELD_VALUE"                 , False, 1, 1)
    def_op( 87, "POP_BLOCK"                   , False, 0, 0)
    def_op( 88, "END_FINALLY"                 , False, 0, 6)
    def_op( 89, "POP_EXCEPT"                  , False, 0, 3)
    def_op( 90, "STORE_NAME"                  ,  True,-1,-1)
    def_op( 91, "DELETE_NAME"                 ,  True,-1,-1)
    def_op( 92, "UNPACK_SEQUENCE"             ,  True,-1,-1)
    def_op( 93, "FOR_ITER"                    ,  True,-1,-1)
    def_op( 94, "UNPACK_EX"                   ,  True,-1,-1)
    def_op( 95, "STORE_ATTR"                  ,  True,-1,-1)
    def_op( 96, "DELETE_ATTR"                 ,  True,-1,-1)
    def_op( 97, "STORE_GLOBAL"                ,  True,-1,-1)
    def_op( 98, "DELETE_GLOBAL"               ,  True,-1,-1)
    def_op(100, "LOAD_CONST"                  ,  True,-1,-1)
    def_op(101, "LOAD_NAME"                   ,  True,-1,-1)
    def_op(102, "BUILD_TUPLE"                 ,  True,-1,-1)
    def_op(103, "BUILD_LIST"                  ,  True,-1,-1)
    def_op(104, "BUILD_SET"                   ,  True,-1,-1)
    def_op(105, "BUILD_MAP"                   ,  True,-1,-1)
    def_op(106, "LOAD_ATTR"                   ,  True,-1,-1)
    def_op(107, "COMPARE_OP"                  ,  True,-1,-1)
    def_op(108, "IMPORT_NAME"                 ,  True,-1,-1)
    def_op(109, "IMPORT_FROM"                 ,  True,-1,-1)
    def_op(110, "JUMP_FORWARD"                ,  True,-1,-1)
    def_op(111, "JUMP_IF_FALSE_OR_POP"        ,  True,-1,-1)
    def_op(112, "JUMP_IF_TRUE_OR_POP"         ,  True,-1,-1)
    def_op(113, "JUMP_ABSOLUTE"               ,  True,-1,-1)
    def_op(114, "POP_JUMP_IF_FALSE"           ,  True,-1,-1)
    def_op(115, "POP_JUMP_IF_TRUE"            ,  True,-1,-1)
    def_op(116, "LOAD_GLOBAL"                 ,  True,-1,-1)
    def_op(119, "CONTINUE_LOOP"               ,  True,-1,-1)
    def_op(120, "SETUP_LOOP"                  ,  True,-1,-1)
    def_op(121, "SETUP_EXCEPT"                ,  True,-1,-1)
    def_op(122, "SETUP_FINALLY"               ,  True,-1,-1)
    def_op(124, "LOAD_FAST"                   ,  True,-1,-1)
    def_op(125, "STORE_FAST"                  ,  True,-1,-1)
    def_op(126, "DELETE_FAST"                 ,  True,-1,-1)
    def_op(130, "RAISE_VARARGS"               ,  True,-1,-1)
    def_op(131, "CALL_FUNCTION"               ,  True,-1,-1)
    def_op(132, "MAKE_FUNCTION"               ,  True,-1,-1)
    def_op(133, "BUILD_SLICE"                 ,  True,-1,-1)
    def_op(135, "LOAD_CLOSURE"                ,  True,-1,-1)
    def_op(136, "LOAD_DEREF"                  ,  True,-1,-1)
    def_op(137, "STORE_DEREF"                 ,  True,-1,-1)
    def_op(138, "DELETE_DEREF"                ,  True,-1,-1)
    def_op(141, "CALL_FUNCTION_KW"            ,  True,-1,-1)
    def_op(142, "CALL_FUNCTION_EX"            ,  True,-1,-1)
    def_op(143, "SETUP_WITH"                  ,  True,-1,-1)
    def_op(144, "EXTENDED_ARG"                ,  True,-1,-1)
    def_op(145, "LIST_APPEND"                 ,  True,-1,-1)
    def_op(146, "SET_ADD"                     ,  True,-1,-1)
    def_op(147, "MAP_ADD"                     ,  True,-1,-1)
    def_op(148, "LOAD_CLASSDEREF"             ,  True,-1,-1)
    def_op(149, "BUILD_LIST_UNPACK"           ,  True,-1,-1)
    def_op(150, "BUILD_MAP_UNPACK"            ,  True,-1,-1)
    def_op(151, "BUILD_MAP_UNPACK_WITH_CALL"  ,  True,-1,-1)
    def_op(152, "BUILD_TUPLE_UNPACK"          ,  True,-1,-1)
    def_op(153, "BUILD_SET_UNPACK"            ,  True,-1,-1)
    def_op(154, "SETUP_ASYNC_WITH"            ,  True,-1,-1)
    def_op(155, "FORMAT_VALUE"                ,  True,-1,-1)
    def_op(156, "BUILD_CONST_KEY_MAP"         ,  True,-1,-1)
    def_op(157, "BUILD_STRING"                ,  True,-1,-1)
    def_op(158, "BUILD_TUPLE_UNPACK_WITH_CALL",  True,-1,-1)
    def_op(160, "LOAD_METHOD"                 ,  True,-1,-1)
    def_op(161, "CALL_METHOD"                 ,  True,-1,-1)

if __name__ == "__main__":
    init()
    print(opmap["BUILD_TUPLE_UNPACK_WITH_CALL"])