from abc import *
import marshal
from IDeKompyler.opcode.op_code import (
    OPCODE,
    opcode,
    opmap
)

class _Parser(metaclass=ABCMeta):
    def __init__(self):
        self.code_obj = None
        self.dis_out  = None
        self.parsed   = None
    
    def load(filepath):
        # TODO: import code object from pyc file
        pass

    @abstractmethod
    def dis(self):
        pass

    def parse(self):
        assert self.code_obj
        self.dis()
        assert self.dis_out

        code_obj = self.code_obj
        dis_out  = self.dis_out
        FIRST_LINENO = code_obj.co_firstlineno
        LINENO_LEN = self.dis_out.find(str(FIRST_LINENO))+len(str(FIRST_LINENO))
        OFFSET_LEN = 12
        
        self.parsed = []
        for line in dis_out.split("\n"):
            line = line[:LINENO_LEN+OFFSET_LEN].strip()
            splitted_line = line.split()
            OPERATION = splitted_line[0]
            bytecode = opmap[OPERATION]

            # TODO: parse oparg and append to self.parsed

