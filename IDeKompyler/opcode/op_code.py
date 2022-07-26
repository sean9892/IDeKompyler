from dataclasses import dataclass

@dataclass
class OPCODE:
    opname : str  # name of opcode
    oparg  : bool # existence of oparg
    push   : int  # the number of elements that operation pushes
    pop    : int  # the number of elements that operation pops
    def __repr__(self):
        return f"{self.opname,self.oparg,self.push,self.pop}"

opcode = {} # opcode to OPCODE object
opmap  = {} # opname to OPCODE object

def def_op(_opcode:int, _opname:str, _oparg:bool, _push:int, _pop:int):
    global opcode
    op = OPCODE(_opname,_oparg,_push,_pop)
    opcode[_opcode] = op
    opmap[_opname]  = op

def rm_op(_opcode):
    _opname = opcode[_opcode].opname
    del opcode[_opcode]
    del opmap[_opname]

