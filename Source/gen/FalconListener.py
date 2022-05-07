# Generated from /media/aaron/Shared2/School/BGSU-thesis/Source/lang/Falcon.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FalconParser import FalconParser
else:
    from FalconParser import FalconParser

# This class defines a complete listener for a parse tree produced by FalconParser.
class FalconListener(ParseTreeListener):

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


    # Enter a parse tree produced by FalconParser#macro_basic.
    def enterMacro_basic(self, ctx:FalconParser.Macro_basicContext):
        pass

    # Exit a parse tree produced by FalconParser#macro_basic.
    def exitMacro_basic(self, ctx:FalconParser.Macro_basicContext):
        pass


    # Enter a parse tree produced by FalconParser#get_domain_name.
    def enterGet_domain_name(self, ctx:FalconParser.Get_domain_nameContext):
        pass

    # Exit a parse tree produced by FalconParser#get_domain_name.
    def exitGet_domain_name(self, ctx:FalconParser.Get_domain_nameContext):
        pass


    # Enter a parse tree produced by FalconParser#get_domain_names.
    def enterGet_domain_names(self, ctx:FalconParser.Get_domain_namesContext):
        pass

    # Exit a parse tree produced by FalconParser#get_domain_names.
    def exitGet_domain_names(self, ctx:FalconParser.Get_domain_namesContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_p.
    def enterStub_p(self, ctx:FalconParser.Stub_pContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_p.
    def exitStub_p(self, ctx:FalconParser.Stub_pContext):
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


    # Enter a parse tree produced by FalconParser#stub_assert_p.
    def enterStub_assert_p(self, ctx:FalconParser.Stub_assert_pContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_assert_p.
    def exitStub_assert_p(self, ctx:FalconParser.Stub_assert_pContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_directives.
    def enterStub_directives(self, ctx:FalconParser.Stub_directivesContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_directives.
    def exitStub_directives(self, ctx:FalconParser.Stub_directivesContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_logical.
    def enterStub_logical(self, ctx:FalconParser.Stub_logicalContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_logical.
    def exitStub_logical(self, ctx:FalconParser.Stub_logicalContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_code.
    def enterStub_code(self, ctx:FalconParser.Stub_codeContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_code.
    def exitStub_code(self, ctx:FalconParser.Stub_codeContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_side_effect_many.
    def enterStub_side_effect_many(self, ctx:FalconParser.Stub_side_effect_manyContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_side_effect_many.
    def exitStub_side_effect_many(self, ctx:FalconParser.Stub_side_effect_manyContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_side_effect.
    def enterStub_side_effect(self, ctx:FalconParser.Stub_side_effectContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_side_effect.
    def exitStub_side_effect(self, ctx:FalconParser.Stub_side_effectContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_fail_side_effect.
    def enterStub_fail_side_effect(self, ctx:FalconParser.Stub_fail_side_effectContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_fail_side_effect.
    def exitStub_fail_side_effect(self, ctx:FalconParser.Stub_fail_side_effectContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_fail_side_effect_many.
    def enterStub_fail_side_effect_many(self, ctx:FalconParser.Stub_fail_side_effect_manyContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_fail_side_effect_many.
    def exitStub_fail_side_effect_many(self, ctx:FalconParser.Stub_fail_side_effect_manyContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_logic.
    def enterStub_logic(self, ctx:FalconParser.Stub_logicContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_logic.
    def exitStub_logic(self, ctx:FalconParser.Stub_logicContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_paren.
    def enterStub_paren(self, ctx:FalconParser.Stub_parenContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_paren.
    def exitStub_paren(self, ctx:FalconParser.Stub_parenContext):
        pass


    # Enter a parse tree produced by FalconParser#stub_logic_multi.
    def enterStub_logic_multi(self, ctx:FalconParser.Stub_logic_multiContext):
        pass

    # Exit a parse tree produced by FalconParser#stub_logic_multi.
    def exitStub_logic_multi(self, ctx:FalconParser.Stub_logic_multiContext):
        pass


    # Enter a parse tree produced by FalconParser#test_winnow.
    def enterTest_winnow(self, ctx:FalconParser.Test_winnowContext):
        pass

    # Exit a parse tree produced by FalconParser#test_winnow.
    def exitTest_winnow(self, ctx:FalconParser.Test_winnowContext):
        pass


    # Enter a parse tree produced by FalconParser#test_groupby.
    def enterTest_groupby(self, ctx:FalconParser.Test_groupbyContext):
        pass

    # Exit a parse tree produced by FalconParser#test_groupby.
    def exitTest_groupby(self, ctx:FalconParser.Test_groupbyContext):
        pass


    # Enter a parse tree produced by FalconParser#test_satisfy.
    def enterTest_satisfy(self, ctx:FalconParser.Test_satisfyContext):
        pass

    # Exit a parse tree produced by FalconParser#test_satisfy.
    def exitTest_satisfy(self, ctx:FalconParser.Test_satisfyContext):
        pass


    # Enter a parse tree produced by FalconParser#groupby_stub.
    def enterGroupby_stub(self, ctx:FalconParser.Groupby_stubContext):
        pass

    # Exit a parse tree produced by FalconParser#groupby_stub.
    def exitGroupby_stub(self, ctx:FalconParser.Groupby_stubContext):
        pass


    # Enter a parse tree produced by FalconParser#groupby_stub_many.
    def enterGroupby_stub_many(self, ctx:FalconParser.Groupby_stub_manyContext):
        pass

    # Exit a parse tree produced by FalconParser#groupby_stub_many.
    def exitGroupby_stub_many(self, ctx:FalconParser.Groupby_stub_manyContext):
        pass


    # Enter a parse tree produced by FalconParser#groupby_code.
    def enterGroupby_code(self, ctx:FalconParser.Groupby_codeContext):
        pass

    # Exit a parse tree produced by FalconParser#groupby_code.
    def exitGroupby_code(self, ctx:FalconParser.Groupby_codeContext):
        pass


    # Enter a parse tree produced by FalconParser#groupby_directives.
    def enterGroupby_directives(self, ctx:FalconParser.Groupby_directivesContext):
        pass

    # Exit a parse tree produced by FalconParser#groupby_directives.
    def exitGroupby_directives(self, ctx:FalconParser.Groupby_directivesContext):
        pass


    # Enter a parse tree produced by FalconParser#winnow_stub_many_many.
    def enterWinnow_stub_many_many(self, ctx:FalconParser.Winnow_stub_many_manyContext):
        pass

    # Exit a parse tree produced by FalconParser#winnow_stub_many_many.
    def exitWinnow_stub_many_many(self, ctx:FalconParser.Winnow_stub_many_manyContext):
        pass


    # Enter a parse tree produced by FalconParser#winnow_stub_directives.
    def enterWinnow_stub_directives(self, ctx:FalconParser.Winnow_stub_directivesContext):
        pass

    # Exit a parse tree produced by FalconParser#winnow_stub_directives.
    def exitWinnow_stub_directives(self, ctx:FalconParser.Winnow_stub_directivesContext):
        pass


    # Enter a parse tree produced by FalconParser#make_domain.
    def enterMake_domain(self, ctx:FalconParser.Make_domainContext):
        pass

    # Exit a parse tree produced by FalconParser#make_domain.
    def exitMake_domain(self, ctx:FalconParser.Make_domainContext):
        pass


    # Enter a parse tree produced by FalconParser#make_domain_args.
    def enterMake_domain_args(self, ctx:FalconParser.Make_domain_argsContext):
        pass

    # Exit a parse tree produced by FalconParser#make_domain_args.
    def exitMake_domain_args(self, ctx:FalconParser.Make_domain_argsContext):
        pass


    # Enter a parse tree produced by FalconParser#set_directive.
    def enterSet_directive(self, ctx:FalconParser.Set_directiveContext):
        pass

    # Exit a parse tree produced by FalconParser#set_directive.
    def exitSet_directive(self, ctx:FalconParser.Set_directiveContext):
        pass


    # Enter a parse tree produced by FalconParser#set_single_directive.
    def enterSet_single_directive(self, ctx:FalconParser.Set_single_directiveContext):
        pass

    # Exit a parse tree produced by FalconParser#set_single_directive.
    def exitSet_single_directive(self, ctx:FalconParser.Set_single_directiveContext):
        pass


    # Enter a parse tree produced by FalconParser#make_fn_directive.
    def enterMake_fn_directive(self, ctx:FalconParser.Make_fn_directiveContext):
        pass

    # Exit a parse tree produced by FalconParser#make_fn_directive.
    def exitMake_fn_directive(self, ctx:FalconParser.Make_fn_directiveContext):
        pass


    # Enter a parse tree produced by FalconParser#make_fn_flag_directive.
    def enterMake_fn_flag_directive(self, ctx:FalconParser.Make_fn_flag_directiveContext):
        pass

    # Exit a parse tree produced by FalconParser#make_fn_flag_directive.
    def exitMake_fn_flag_directive(self, ctx:FalconParser.Make_fn_flag_directiveContext):
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


    # Enter a parse tree produced by FalconParser#make_list_c.
    def enterMake_list_c(self, ctx:FalconParser.Make_list_cContext):
        pass

    # Exit a parse tree produced by FalconParser#make_list_c.
    def exitMake_list_c(self, ctx:FalconParser.Make_list_cContext):
        pass


    # Enter a parse tree produced by FalconParser#make_list.
    def enterMake_list(self, ctx:FalconParser.Make_listContext):
        pass

    # Exit a parse tree produced by FalconParser#make_list.
    def exitMake_list(self, ctx:FalconParser.Make_listContext):
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