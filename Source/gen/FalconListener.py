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


    # Enter a parse tree produced by FalconParser#assert_test.
    def enterAssert_test(self, ctx:FalconParser.Assert_testContext):
        pass

    # Exit a parse tree produced by FalconParser#assert_test.
    def exitAssert_test(self, ctx:FalconParser.Assert_testContext):
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


    # Enter a parse tree produced by FalconParser#stub_many_pv.
    def enterStub_many_pv(self, ctx:FalconParser.Stub_many_pvContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_many_pv.
    def exitStub_many_pv(self, ctx:FalconParser.Stub_many_pvContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_assert.
    def enterStub_assert(self, ctx:FalconParser.Stub_assertContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_assert.
    def exitStub_assert(self, ctx:FalconParser.Stub_assertContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_code.
    def enterStub_code(self, ctx:FalconParser.Stub_codeContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_code.
    def exitStub_code(self, ctx:FalconParser.Stub_codeContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_directives.
    def enterStub_directives(self, ctx:FalconParser.Stub_directivesContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_directives.
    def exitStub_directives(self, ctx:FalconParser.Stub_directivesContext):
        pass


    # Enter a parse tree produced by FalconParser#set_directive.
    def enterSet_directive(self, ctx:FalconParser.Set_directiveContext):
        pass

    # Exit a parse tree produced by FalconParser#set_directive.
    def exitSet_directive(self, ctx:FalconParser.Set_directiveContext):
        pass


    # Enter a parse tree produced by FalconParser#make_codestmt.
    def enterMake_codestmt(self, ctx:FalconParser.Make_codestmtContext):
        pass

    # Exit a parse tree produced by FalconParser#make_codestmt.
    def exitMake_codestmt(self, ctx:FalconParser.Make_codestmtContext):
        pass


    # Enter a parse tree produced by FalconParser#assign_value.
    def enterAssign_value(self, ctx:FalconParser.Assign_valueContext):
        pass

    # Exit a parse tree produced by FalconParser#assign_value.
    def exitAssign_value(self, ctx:FalconParser.Assign_valueContext):
        pass


    # Enter a parse tree produced by FalconParser#assign_type_value.
    def enterAssign_type_value(self, ctx:FalconParser.Assign_type_valueContext):
        pass

    # Exit a parse tree produced by FalconParser#assign_type_value.
    def exitAssign_type_value(self, ctx:FalconParser.Assign_type_valueContext):
        pass


    # Enter a parse tree produced by FalconParser#args.
    def enterArgs(self, ctx:FalconParser.ArgsContext):
        pass

    # Exit a parse tree produced by FalconParser#args.
    def exitArgs(self, ctx:FalconParser.ArgsContext):
        pass


    # Enter a parse tree produced by FalconParser#name.
    def enterName(self, ctx:FalconParser.NameContext):
        pass

    # Exit a parse tree produced by FalconParser#name.
    def exitName(self, ctx:FalconParser.NameContext):
        pass


    # Enter a parse tree produced by FalconParser#predicate.
    def enterPredicate(self, ctx:FalconParser.PredicateContext):
        pass

    # Exit a parse tree produced by FalconParser#predicate.
    def exitPredicate(self, ctx:FalconParser.PredicateContext):
        pass


    # Enter a parse tree produced by FalconParser#value.
    def enterValue(self, ctx:FalconParser.ValueContext):
        pass

    # Exit a parse tree produced by FalconParser#value.
    def exitValue(self, ctx:FalconParser.ValueContext):
        pass


    # Enter a parse tree produced by FalconParser#make_value.
    def enterMake_value(self, ctx:FalconParser.Make_valueContext):
        pass

    # Exit a parse tree produced by FalconParser#make_value.
    def exitMake_value(self, ctx:FalconParser.Make_valueContext):
        pass


    # Enter a parse tree produced by FalconParser#make_name_value.
    def enterMake_name_value(self, ctx:FalconParser.Make_name_valueContext):
        pass

    # Exit a parse tree produced by FalconParser#make_name_value.
    def exitMake_name_value(self, ctx:FalconParser.Make_name_valueContext):
        pass


    # Enter a parse tree produced by FalconParser#make_value_type.
    def enterMake_value_type(self, ctx:FalconParser.Make_value_typeContext):
        pass

    # Exit a parse tree produced by FalconParser#make_value_type.
    def exitMake_value_type(self, ctx:FalconParser.Make_value_typeContext):
        pass


    # Enter a parse tree produced by FalconParser#make_name_type_value.
    def enterMake_name_type_value(self, ctx:FalconParser.Make_name_type_valueContext):
        pass

    # Exit a parse tree produced by FalconParser#make_name_type_value.
    def exitMake_name_type_value(self, ctx:FalconParser.Make_name_type_valueContext):
        pass


    # Enter a parse tree produced by FalconParser#dictate.
    def enterDictate(self, ctx:FalconParser.DictateContext):
        pass

    # Exit a parse tree produced by FalconParser#dictate.
    def exitDictate(self, ctx:FalconParser.DictateContext):
        pass



del FalconParser