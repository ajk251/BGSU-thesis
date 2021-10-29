# Generated from /media/aaron/Shared2/School/BGSU-thesis/Source/lang/Falcon.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FalconParser import FalconParser
else:
    from FalconParser import FalconParser

# This class defines a complete listener for a parse tree produced by FalconParser.
class FalconListener(ParseTreeListener):

    # Enter a parse tree produced by FalconParser#program.
    def enterProgram(self, ctx:FalconParser.ProgramContext):
        pass

    # Exit a parse tree produced by FalconParser#program.
    def exitProgram(self, ctx:FalconParser.ProgramContext):
        pass


    # Enter a parse tree produced by FalconParser#block.
    def enterBlock(self, ctx:FalconParser.BlockContext):
        pass

    # Exit a parse tree produced by FalconParser#block.
    def exitBlock(self, ctx:FalconParser.BlockContext):
        pass


    # Enter a parse tree produced by FalconParser#ns.
    def enterNs(self, ctx:FalconParser.NsContext):
        pass

    # Exit a parse tree produced by FalconParser#ns.
    def exitNs(self, ctx:FalconParser.NsContext):
        pass


    # Enter a parse tree produced by FalconParser#stmt.
    def enterStmt(self, ctx:FalconParser.StmtContext):
        pass

    # Exit a parse tree produced by FalconParser#stmt.
    def exitStmt(self, ctx:FalconParser.StmtContext):
        pass


    # Enter a parse tree produced by FalconParser#test_basic.
    def enterTest_basic(self, ctx:FalconParser.Test_basicContext):
        pass

    # Exit a parse tree produced by FalconParser#test_basic.
    def exitTest_basic(self, ctx:FalconParser.Test_basicContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_pv.
    def enterStub_pv(self, ctx:FalconParser.Stub_pvContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_pv.
    def exitStub_pv(self, ctx:FalconParser.Stub_pvContext):
        pass


    # Enter a parse tree produced by FalconParser#set_directive.
    def enterSet_directive(self, ctx:FalconParser.Set_directiveContext):
        pass

    # Exit a parse tree produced by FalconParser#set_directive.
    def exitSet_directive(self, ctx:FalconParser.Set_directiveContext):
        pass


    # Enter a parse tree produced by FalconParser#fn_arg.
    def enterFn_arg(self, ctx:FalconParser.Fn_argContext):
        pass

    # Exit a parse tree produced by FalconParser#fn_arg.
    def exitFn_arg(self, ctx:FalconParser.Fn_argContext):
        pass



del FalconParser