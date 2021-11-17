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


    # Visit a parse tree produced by FalconParser#assert_test.
    def visitAssert_test(self, ctx:FalconParser.Assert_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#test_basic.
    def visitTest_basic(self, ctx:FalconParser.Test_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#get_domain_name.
    def visitGet_domain_name(self, ctx:FalconParser.Get_domain_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#get_domain_names.
    def visitGet_domain_names(self, ctx:FalconParser.Get_domain_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_p.
    def visitStub_p(self, ctx:FalconParser.Stub_pContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_pv.
    def visitStub_pv(self, ctx:FalconParser.Stub_pvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_many_pv.
    def visitStub_many_pv(self, ctx:FalconParser.Stub_many_pvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_assert.
    def visitStub_assert(self, ctx:FalconParser.Stub_assertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_assert_p.
    def visitStub_assert_p(self, ctx:FalconParser.Stub_assert_pContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_code.
    def visitStub_code(self, ctx:FalconParser.Stub_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_directives.
    def visitStub_directives(self, ctx:FalconParser.Stub_directivesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#stub_logical.
    def visitStub_logical(self, ctx:FalconParser.Stub_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#test_logical.
    def visitTest_logical(self, ctx:FalconParser.Test_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_domain.
    def visitMake_domain(self, ctx:FalconParser.Make_domainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_domain_args.
    def visitMake_domain_args(self, ctx:FalconParser.Make_domain_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#set_directive.
    def visitSet_directive(self, ctx:FalconParser.Set_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_fn_directive.
    def visitMake_fn_directive(self, ctx:FalconParser.Make_fn_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_codestmt.
    def visitMake_codestmt(self, ctx:FalconParser.Make_codestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#assign_value.
    def visitAssign_value(self, ctx:FalconParser.Assign_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#assign_type_value.
    def visitAssign_type_value(self, ctx:FalconParser.Assign_type_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#args.
    def visitArgs(self, ctx:FalconParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_list_c.
    def visitMake_list_c(self, ctx:FalconParser.Make_list_cContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_list.
    def visitMake_list(self, ctx:FalconParser.Make_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#get_name.
    def visitGet_name(self, ctx:FalconParser.Get_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#get_card.
    def visitGet_card(self, ctx:FalconParser.Get_cardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#get_not.
    def visitGet_not(self, ctx:FalconParser.Get_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#predicate.
    def visitPredicate(self, ctx:FalconParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#value.
    def visitValue(self, ctx:FalconParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_value.
    def visitMake_value(self, ctx:FalconParser.Make_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_name_value.
    def visitMake_name_value(self, ctx:FalconParser.Make_name_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_value_type.
    def visitMake_value_type(self, ctx:FalconParser.Make_value_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#make_name_type_value.
    def visitMake_name_type_value(self, ctx:FalconParser.Make_name_type_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FalconParser#dictate.
    def visitDictate(self, ctx:FalconParser.DictateContext):
        return self.visitChildren(ctx)



del FalconParser