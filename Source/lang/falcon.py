
from collections import defaultdict

import antlr4

from gen.FalconVisitor import FalconVisitor
from gen.FalconParser import FalconParser

# TODO:
#   - find funcs in modules & verify
#   - a -decorate option, for unittest
#   add number to test! for ordering!


class Falcon(FalconVisitor):

    def __init__(self):

        super().__init__()

        # build the namespaces
        self.ns = defaultdict(dict)
        self.ns['ordering'] = []
        self.ns['initial'] = {'directives': {}, 'imports': []}

        self.current_ns = 'global'
        self.ns[self.current_ns] = {'tests': {}, 'ordering': []}

        self.n = -1          #tests do not have a name…they will have a number

    def intermediate_tests(self):
        return self.ns

    def get_id(self):
        self.n += 1
        return self.n

    # helper functions --------------------------

    def ns_get(self, name, only_local=False):
        """Search the local namespace, if it is not there, search the global"""

        # What if the value is None!?

        value = self.ns[self.current_ns].get(name, None)

        if not only_local and value is None:
            value = self.ns['global'][name]

        # if it is still None, raise error

        return value

    def ns_set(self, names, value):
        '''Set keys to a value from the current scope'''

        pass

    # -------------------------------------------

    def visitNs(self, ctx: FalconParser.NsContext):

        # name = str(self.visit(ctx.name()))
        name = str(ctx.name().getText())

        self.ns['ordering'].append(('namespace', name))

        previous = self.current_ns
        self.current_ns = name

        self.ns[self.current_ns]['tests'] = {}
        self.ns[self.current_ns]['ordering'] = []

        for stmt in ctx.children:
            self.visit(stmt)

        self.current_ns = previous

    # Assign-------------------------------------

    def visitAssign_value(self, ctx: FalconParser.Assign_valueContext):

        name = self.visit(ctx.name())
        value = self.visit(ctx.value())

        if self.current_ns == 'initial':
            self.ns['ordering'].append(('var', name, value))
        else:
            self.ns[self.current_ns]['ordering'].append(('var', name, value))

    def visitAssign_type_value(self, ctx: FalconParser.Assign_type_valueContext):

        name = self.visit(ctx.name(0))
        value = self.visit(ctx.value())

        # have to work around CODESTMT
        if isinstance(ctx.children[2], FalconParser.NameContext):
            kind = self.visit(ctx.children[2])
        else:
            kind = ctx.children[2].getText().strip('`')

        if self.current_ns == 'initial':
            self.ns['ordering'].append(('type-var', name, kind, value))
        else:
            self.ns[self.current_ns]['ordering'].append(('type-var', name, kind, value))

    def visitArgs(self, ctx: FalconParser.ArgsContext):

        args = []
        okay_args = (FalconParser.Make_valueContext,
                     FalconParser.Make_value_typeContext,
                     FalconParser.Make_name_valueContext,
                     FalconParser.Make_name_type_valueContext)

        for child in ctx.children:
            if isinstance(child, okay_args):
                args.append(self.visit(child))

        return {'kind': 'arguments', 'args': args}

    # make value/named values arg-list
    def visitMake_value(self, ctx: FalconParser.Make_valueContext):
        return 'value', self.visit(ctx.value())

    def visitMake_name_value(self, ctx: FalconParser.Make_name_valueContext):
        return 'named-value', self.visit(ctx.name()), self.visit(ctx.value())

    def visitMake_value_type(self, ctx: FalconParser.Make_value_typeContext):
        return 'value-type', self.visit(ctx.value(0)).strip('`'), self.visit(ctx.value(1)).strip('`')

    def visitMake_name_type_value(self, ctx: FalconParser.Make_name_type_valueContext):

        # have to work around CODESTMT
        if isinstance(ctx.children[2], FalconParser.NameContext):
            kind = self.visit(ctx.children[2])
        else:
            kind = ctx.children[2].getText().strip('`')

        return 'name-type-value', self.visit(ctx.children[0]), kind, self.visit(ctx.value()).strip('`')

    # -------------------------------------------

    def visitName(self, ctx: FalconParser.NameContext):
        return ctx.getText()

    def visitPredicate(self, ctx: FalconParser.PredicateContext):
        return ctx.getText()

    def visitValue(self, ctx: FalconParser.ValueContext):
        return ctx.getText()

    def visitDictate(self, ctx: FalconParser.DictateContext):
        return ctx.getText()

    # -------------------------------------------

    def visitSet_directive(self, ctx: FalconParser.Set_directiveContext):

        directive = str(ctx.DIRECTIVE())
        value = str(self.visit(ctx.dictate()))

        # if initial...
        self.ns[self.current_ns].setdefault('directives', {})[directive] = value

        # print(self.ns[self.current]['directives'])

    def visitMake_codestmt(self, ctx: FalconParser.Make_codestmtContext):

        # if self.current == 'initial':
        #     self.ns['ordering'].append(('code', ctx.getText().strip('`')))
        # else:
        #     self.ns[self.current]['ordering'].append(('code', ctx.getText().strip('`')))

        self.ns[self.current_ns]['ordering'].append(('code', ctx.getText().strip('`')))

    # Tests -------------------------------------
    # the kinds of tests that get performed

    def visitTest_basic(self, ctx: FalconParser.Test_basicContext):

        test = {}

        test['kind'] = 'test-basic'
        test['function'] = self.visit(ctx.name(0))
        test['domain'] = str(self.visit(ctx.name(1)))
        test['id'] = self.get_id()
        test['directives'] = {}
        test['stubs'] = []

        okay_stubs = (FalconParser.Stub_pvContext,
                      FalconParser.Stub_many_pvContext,
                      FalconParser.Stub_codeContext)

        for stub in ctx.children:

            if isinstance(stub, okay_stubs):
                test['stubs'].append(self.visit(stub))

                if self.current_ns == 'global': print(self.visit(stub))

            elif isinstance(stub, FalconParser.Stub_directivesContext):
                directives = self.visit(stub)
                test['directives'] = directives
            else:
                # TODO raise error! How did it get here‽
                continue

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('test', test['id']))

        return

    def visitAssert_test(self, ctx: FalconParser.Assert_testContext):

        test = {}
        test['kind'] = 'assert-test'
        test['function'] = self.visit(ctx.name())
        test['id'] = self.get_id()
        test['stubs'] = []
        test['directives'] = {}

        for stub in ctx.children:

            if isinstance(stub, FalconParser.Stub_assertContext):
                # print('args received: ', args)
                test['stubs'].append(self.visit(stub))
            elif isinstance(stub, FalconParser.Stub_directivesContext):
                directives = self.visit(stub)
                test['directives'] = directives
            elif isinstance(stub, FalconParser.Stub_codeContext):
                self.visit(stub)

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('assertion', test['id']))

        return

    # stubs -------------------------------------

    def visitStub_pv(self, ctx: FalconParser.Stub_pvContext):

        stub = {}

        stub['kind'] = 'predicate-value'
        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = self.visit(ctx.value())

        return stub

    def visitStub_many_pv(self, ctx: FalconParser.Stub_many_pvContext):

        stub = {}

        stub['kind'] = 'predicate-value+'
        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = tuple(self.visit(child) for child in ctx.children[2:])

        return stub

    def visitStub_code(self, ctx: FalconParser.Stub_codeContext):

        stub = {}

        stub['kind'] = 'code'
        stub['value'] = str(ctx.CODESMNT()).strip('`')
        return stub

    def visitStub_directives(self, ctx: FalconParser.Stub_directivesContext):

        directives = {}

        for child in ctx.children:
            if isinstance(child, FalconParser.Set_directiveContext):
                d = child.DIRECTIVE().getText()
                directives[d] = child.dictate().getText()

        return directives

    def visitStub_assert(self, ctx: FalconParser.Stub_assertContext):

        stub = {}
        stub['kind'] = 'assertion'
        stub['argument'] = self.visit(ctx.arg_list())
        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = self.visit(ctx.value())

        return stub
