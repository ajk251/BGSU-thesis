# Generated from /media/aaron/Shared2/School/BGSU-thesis/Source/lang/Falcon.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FalconParser import FalconParser
else:
    from FalconParser import FalconParser

# This class defines a complete generic visitor for a parse tree produced by FalconParser.

class FalconVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FalconParser#program.
    def visitProgram(self, ctx:FalconParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#block.
    def visitBlock(self, ctx:FalconParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#ns.
    def visitNs(self, ctx:FalconParser.NsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stmt.
    def visitStmt(self, ctx:FalconParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#test_basic.
    def visitTest_basic(self, ctx:FalconParser.Test_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_pv.
    def visitStub_pv(self, ctx:FalconParser.Stub_pvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#set_directive.
    def visitSet_directive(self, ctx:FalconParser.Set_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#fn_arg.
    def visitFn_arg(self, ctx:FalconParser.Fn_argContext):
        return self.visitChildren(ctx)



del FalconParser