
from collections import defaultdict

import antlr4

from gen.FalconVisitor import FalconVisitor
from gen.FalconParser import FalconParser

# TODO:
#   - falcon must return the dict
#   - find funcs in modules & verify


class Falcon(FalconVisitor):

    def __init__(self):

        super().__init__()

        # build the namespaces
        self.current = 'global'
        self.ns = defaultdict(dict)
        self.ns[self.current] = {'directives': []}

        # the thing to return
        self.json = {}

    # helper functions --------------------------

    def ns_get(self, name, only_local=False):
        """Search the local namespace, if it is not there, search the global"""

        # What if the value is None!?

        value = self.ns[self.current].get(name, None)

        if not only_local and value is None:
            value = self.ns['global'][name]

        # if it is still None, raise error

        return value

    # -------------------------------------------

    def visitNs(self, ctx: FalconParser.NsContext):

        # name = str(self.visit(ctx.name()))
        name = str(ctx.name().getText())
        # print('NS: ', name)

        previous = self.current
        self.current = name

        for stmt in ctx.children:
            self.visit(stmt)

        print(self.ns)
        print('done')

        self.current = previous

    # -------------------------------------------

    def visitName(self, ctx: FalconParser.NameContext):
        return ctx.getText()

    def visitPredicate(self, ctx: FalconParser.PredicateContext):
        return ctx.getText()

    def visitValue(self, ctx: FalconParser.ValueContext):
        return ctx.getText()

    # -------------------------------------------

    def visitSet_directive(self, ctx: FalconParser.Set_directiveContext):

        pass

    # Tests -------------------------------------
    # the kinds of tests that get performed

    def visitTest_basic(self, ctx: FalconParser.Test_basicContext):

        test = {}

        # test['function'] = str(ctx.name(0))
        test['function'] = self.visit(ctx.name(0))
        test['domain'] = str(self.visit(ctx.name(1)))

        stubs = []

        for stub in ctx.children:

            # should be every thing but the other 'stuff'
            # if not isinstance(stub, antlr4.tree.Tree.TerminalNodeImpl):
            if isinstance(stub, FalconParser.Stub_pvContext):
                stubs.append(self.visit(stub))

        test['stubs'] = stubs

        self.ns[self.current]['TestBasic'] = test

        return

    # stubs -------------------------------------

    def visitStub_pv(self, ctx: FalconParser.Stub_pvContext):

        stub = {}

        stub['kind'] = 'predicate-value'
        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = self.visit(ctx.value())

        return stub

