
from collections import defaultdict

import antlr4

from gen.FalconVisitor import FalconVisitor
from gen.FalconParser import FalconParser

# TODO:
#   - find funcs in modules & verify
#   - a -decorate option, for unittest

# TODO:
#   - function args
#   - lists
#   - validation, ie domain is a domain, name is a py-name


class Falcon(FalconVisitor):

    def __init__(self):

        super().__init__()

        # build the namespaces
        self.ns = defaultdict(dict)
        self.ns['ordering'] = []
        self.ns['initial'] = {'directives': {}, 'imports': []}

        self.current_ns = 'global'
        self.ns[self.current_ns] = {'tests': {}, 'ordering': [], 'directives': {}}

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

    # def visitGet_card(self, ctx: FalconParser.Get_cardContext):
    #     return {'value': ctx.getText(), 'modifier': 'cardinality'}
    #
    # def visitGet_not(self, ctx: FalconParser.Get_notContext):
    #     return {'value': ctx.getText(), 'modifier': 'not'}

    # ----------------------------

    def visitPredicate(self, ctx: FalconParser.PredicateContext):
        return ctx.getText()

    def visitValue(self, ctx: FalconParser.ValueContext):
        return ctx.getText().strip('`')

    def visitDictate(self, ctx: FalconParser.DictateContext):

        value = None

        if ctx.value_list() is not None:
            value = self.visit(ctx.value_list())
            value = '[{}]'.format(', '.join(value))
        else:
            value = ctx.getText()

        return value

    # -------------------------------------------

    def visitSet_directive(self, ctx: FalconParser.Set_directiveContext, set_global=True):

        directive = str(ctx.DIRECTIVE())
        value = str(self.visit(ctx.dictate()))

        params = []

        for child in ctx.children:
            if isinstance(child, FalconParser.Make_fn_directiveContext):
                params.append(self.visit(child))
            elif isinstance(child, FalconParser.Make_fn_flag_directiveContext):
                params.append(self.visit(child))

        # if initial...
        if set_global:
            # imports are a special case, ie many of them
            if directive == ':import':
                self.ns['initial']['imports'].append((value, {arg: value for arg, value in params}))
            else:
                self.ns[self.current_ns].setdefault('directives', {})[directive] = (value, params)
        else:
            return {'directive': directive, 'value': value, 'params': params}

    def visitSet_single_directive(self, ctx:FalconParser.Set_single_directiveContext):

        directive = str(ctx.DIRECTIVE())

        self.ns[self.current_ns].setdefault('directives', {})[directive] = (None, None)

        return {'directive': directive, 'value': None, 'params': None}

    def visitMake_codestmt(self, ctx: FalconParser.Make_codestmtContext, set_global=False):

        # this logic is ugly...

        if set_global:
            self.ns[self.current_ns]['ordering'].append(('code', ctx.getText().strip('`')))
        # else:
        #     self.ns[self.current_ns]['ordering'].append(('code', ctx.getText().strip('`')))

        return {'kind': 'code', 'value': ctx.getText().strip('`')}

    def visitMake_fn_directive(self, ctx: FalconParser.Make_fn_directiveContext):

        directive = str(ctx.FNARG())
        params = self.visit(ctx.dictate())

        return directive.strip('-'), params

    def visitMake_fn_flag_directive(self, ctx: FalconParser.Make_fn_flag_directiveContext):

        directive = str(ctx.FNARG())
        # params = self.visit(ctx.dictate())
        flag = self.visit(ctx.FNARG())

        return directive.strip('-'), flag

    # ------------------------------------------

    def visitMake_list(self, ctx: FalconParser.Make_listContext):

        values = []

        for child in ctx.children:
            if child.getText() in '[]': continue

            value = self.visit(child)
            value = value.strip().rstrip('\'').lstrip('\'')
            values.append(value)

        return values

    def visitMake_list_c(self, ctx: FalconParser.Make_list_cContext):

        values = []

        for child in ctx.children:
            if child.getText() in ',[]': continue

            value = self.visit(child).strip().rstrip('\'').lstrip('\'')
            values.append(value)

        return values

    # Tests -------------------------------------
    # the kinds of tests that get performed

    def visitTest_basic(self, ctx: FalconParser.Test_basicContext):

        test = {}

        test['kind'] = 'test-basic'
        test['function'] = self.visit(ctx.name())
        test['domain'] = self.visit(ctx.domain_names())
        test['id'] = self.get_id()
        test['directives'] = {}
        # test['directives'] = []
        test['stubs'] = []

        okay_stubs = (FalconParser.Stub_pvContext,
                      FalconParser.Stub_pContext,
                      FalconParser.Stub_many_pvContext,
                      FalconParser.Stub_codeContext,
                      FalconParser.Stub_logicalContext,
                      FalconParser.Stub_side_effectContext,
                      FalconParser.Stub_side_effect_manyContext,
                      FalconParser.Stub_fail_side_effectContext,
                      FalconParser.Stub_fail_side_effect_manyContext)

        for stub in ctx.children:

            if isinstance(stub, okay_stubs):
                test['stubs'].append(self.visit(stub))
            elif isinstance(stub, FalconParser.Stub_directivesContext):
                # directives = self.visit(stub)
                ds = self.visit(stub)
                for d in ds:
                    test['directives'][d['directive']] = {'value': d['value'], 'params': d['params']}
                # test['directives'][d['directive']].append({'value': d['value'], 'params': d['params']})
            else:
                # TODO raise error! How did it get here‽
                # print('Test -> ', type(stub))
                continue

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('test', test['id']))

        return

    def visitMacro_basic(self, ctx: FalconParser.Macro_basicContext):

        test = {}

        test['kind'] = 'macro'
        test['name'] = self.visit(ctx.name(0))
        test['function'] = self.visit(ctx.name(1))
        test['domain'] = self.visit(ctx.domain_names())
        test['id'] = self.get_id()
        test['directives'] = {}
        # test['directives'] = []
        test['stubs'] = []

        okay_stubs = (FalconParser.Stub_pvContext,
                      FalconParser.Stub_pContext,
                      FalconParser.Stub_many_pvContext,
                      FalconParser.Stub_codeContext,
                      FalconParser.Stub_logicalContext,
                      FalconParser.Stub_side_effectContext,
                      FalconParser.Stub_side_effect_manyContext,
                      FalconParser.Stub_fail_side_effectContext,
                      FalconParser.Stub_fail_side_effect_manyContext)

        for stub in ctx.children:

            if isinstance(stub, okay_stubs):
                test['stubs'].append(self.visit(stub))
            elif isinstance(stub, FalconParser.Stub_directivesContext):
                # directives = self.visit(stub)
                ds = self.visit(stub)
                for d in ds:
                    test['directives'][d['directive']] = {'value': d['value'], 'params': d['params']}
                # test['directives'][d['directive']].append({'value': d['value'], 'params': d['params']})
            else:
                # TODO raise error! How did it get here‽
                # print('Test -> ', type(stub))
                continue

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('test', test['id']))

    def visitAssert_test(self, ctx: FalconParser.Assert_testContext):

        test = {}
        test['kind'] = 'assert-test'
        test['function'] = self.visit(ctx.name())
        test['id'] = self.get_id()
        test['stubs'] = []
        test['directives'] = {}

        okay_stubs = (FalconParser.Stub_assertContext, FalconParser.Stub_assert_pContext)

        for stub in ctx.children:

            if isinstance(stub, okay_stubs):
                test['stubs'].append(self.visit(stub))
            elif isinstance(stub, FalconParser.Stub_directivesContext):
                # directives = self.visit(stub)
                # test['directives'] = directives
                ds = self.visit(stub)
                for d in ds:
                    test['directives'][d['directive']] = {'value': d['value'], 'params': d['params']}
            elif isinstance(stub, FalconParser.Stub_codeContext):
                self.visit(stub)
                # TODO: THIS IS MISSING!!!
                test['stubs'].append(self.visit(stub))

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('assertion', test['id']))

        return

    # def visitTest_winnow(self, ctx: FalconParser.Test_winnowContext):
    def visitTest_groupby(self, ctx: FalconParser.Test_groupbyContext):

        # test = {'kind': 'winnow-test'}
        test = {'kind': 'groupby-test'}
        test['function'] = self.visit(ctx.name(0))
        test['domain'] = self.visit(ctx.domain_names())
        test['id'] = self.get_id()
        test['directives'] = {}
        test['stubs'] = []
        # test['group-predicates'] = []                # this is useful later on

        # there has to be a better way…  _ == Falcon.ARROW?
        if ctx.children[3].getText() == '->' or ctx.children[3].getText() == '→':
            test['bin'] = self.visit((ctx.name(1)))
        else:
            test['bin'] = None

        for child in ctx.children:
            # if isinstance(child, FalconParser.Winnow_stubContext):
            if isinstance(child, FalconParser.Groupby_stubContext):
                stub = self.visit(child)
                test['stubs'].append(stub)
                # test['group-predicates'].append((stub['group'], stub['predicate']))
            # elif isinstance(child, FalconParser.Winnow_stub_manyContext):
            elif isinstance(child, FalconParser.Groupby_stub_manyContext):
                stub = self.visit(child)
                test['stubs'].append(stub)
                # test['group-predicates'].append((stub['group'], stub['predicate'], stub['values']))
            # elif isinstance(child, FalconParser.Winnow_codeContext):
            elif isinstance(child, FalconParser.Groupby_codeContext):
                stub = self.visit(child)
                test['stubs'].append(stub)
            elif isinstance(child, FalconParser.Groupby_directivesContext):
                ds = self.visit(child)
                for d in ds:
                    test['directives'][d['directive']] = {'value': d['value'], 'params': d['params']}
            else:
                # print(self.visit(child), type(child))
                # TODO: return error
                # raise FalconError('')
                continue

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('test', test['id']))

    def visitTest_satisfy(self, ctx: FalconParser.Test_satisfyContext):

        test = {'kind': 'satisfy-test'}
        test['function'] = self.visit(ctx.name(0))
        test['domain'] = self.visit(ctx.domain_names())
        test['bin'] = None
        test['id'] = self.get_id()
        test['directives'] = {}
        test['stubs'] = []
        test['group-predicates'] = []                # this is useful later on

        # this is for the old version of Satisfy
        # # there has to be a better way…  _ == Falcon.ARROW?
        # if ctx.children[3].getText() == '->' or ctx.children[3].getText() == '→':
        #     test['bin'] = self.visit((ctx.name(1)))
        # else:
        #     test['bin'] = None
        #
        # for child in ctx.children:
        #     if isinstance(child, FalconParser.Winnow_stubContext):
        #         stub = self.visit(child)
        #         test['stubs'].append(stub)
        #         # test['group-predicates'].append((stub['group'], stub['predicate']))
        #     elif isinstance(child, FalconParser.Winnow_stub_manyContext):
        #         stub = self.visit(child)
        #         test['stubs'].append(stub)
        #         test['group-predicates'].append((stub['group'], stub['predicate'], stub['values']))
        #     else:
        #         # print(self.visit(child), type(child))
        #         continue
        #
        # self.ns[self.current_ns]['tests'][test['id']] = test
        # self.ns[self.current_ns]['ordering'].append(('test', test['id']))

        okay_stubs = (FalconParser.Stub_pvContext,
                      FalconParser.Stub_pContext,
                      FalconParser.Stub_many_pvContext,
                      FalconParser.Stub_codeContext,
                      FalconParser.Stub_logicalContext,
                      FalconParser.Stub_side_effectContext,
                      FalconParser.Stub_side_effect_manyContext)

        for stub in ctx.children:

            if isinstance(stub, okay_stubs):
                test['stubs'].append(self.visit(stub))
            elif isinstance(stub, FalconParser.Stub_directivesContext):
                # directives = self.visit(stub)
                ds = self.visit(stub)
                for d in ds:
                    test['directives'][d['directive']] = {'value': d['value'], 'params': d['params']}
                # test['directives'][d['directive']].append({'value': d['value'], 'params': d['params']})
            else:
                # TODO raise error! How did it get here‽
                # print('Test -> ', type(stub))
                continue

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('test', test['id']))

        return

    def visitTest_winnow(self, ctx: FalconParser.Test_winnowContext):

        # many many -> many predicate value*s* & many group predicate value*s*

        test = {'kind': 'winnow-test'}
        test['function'] = self.visit(ctx.name(0))
        test['domain'] = self.visit(ctx.domain_names())
        test['id'] = self.get_id()
        test['directives'] = {}
        test['stubs'] = []
        # test['group-predicates'] = []                # this is useful later on

        test['bin'] = self.visit((ctx.name(1)))

        for child in ctx.children:
            if isinstance(child, FalconParser.Winnow_stub_many_manyContext):
                stub = self.visit(child)
                test['stubs'].append(stub)
                # test['group-predicates'].append((stub['group'], stub['predicate']))
            # elif isinstance(child, FalconParser.Winnow_stub_manyContext):
            #     stub = self.visit(child)
            #     test['stubs'].append(stub)
                # test['group-predicates'].append((stub['group'], stub['predicate'], stub['values']))
            # elif isinstance(child, FalconParser.Winnow_codeContext):
            # # elif isinstance(child, FalconParser.Groupby_codeContext):
            #     stub = self.visit(child)
            #     test['stubs'].append(stub)
            if isinstance(child, FalconParser.Winnow_stub_directivesContext):
                ds = self.visit(child)
                for d in ds:
                    test['directives'][d['directive']] = {'value': d['value'], 'params': d['params']}
            else:
                # print(self.visit(child), type(child))
                # TODO: return error
                continue

        self.ns[self.current_ns]['tests'][test['id']] = test
        self.ns[self.current_ns]['ordering'].append(('test', test['id']))

    # stubs -------------------------------------
    # groupby/satisfy----
    # def visitWinnow_stub(self, ctx: FalconParser.Winnow_stubContext):
    def visitGroupby_stub(self, ctx: FalconParser.Groupby_stubContext):

        stub = {'kind': 'group-predicate'}
        stub['group'] = self.visit(ctx.value())
        stub['predicate'] = self.visit(ctx.predicate())

        return stub

    # def visitWinnow_stub_many(self, ctx: FalconParser.Winnow_stub_manyContext):
    def visitGroupby_stub_many(self, ctx: FalconParser.Groupby_stub_manyContext):

        stub = {'kind': 'group-predicate-values'}
        stub['group'] = self.visit(ctx.value(0))
        stub['predicate'] = self.visit(ctx.predicate())
        stub['values'] = tuple(self.visit(child) for child in ctx.children[3:])

        return stub

    # def visitWinnow_code(self, ctx: FalconParser.Winnow_codeContext):
    def visitGroupby_code(self, ctx: FalconParser.Groupby_codeContext):
        # TODO: This!
        return self.visit(ctx.CODESMNT())

    # def visitWinnow_directives(self, ctx: FalconParser.Winnow_directivesContext):
    def visitGroupby_directives(self, ctx: FalconParser.Groupby_directivesContext):

        directives = []

        for child in ctx.children:
            if isinstance(child, FalconParser.Set_directiveContext):
                d = self.visitSet_directive(child, False)
                directives.append(d)

        return directives

    # Winnow stubs ------------------------------

    def visitWinnow_stub_many_many(self, ctx: FalconParser.Winnow_stub_many_manyContext):

        # there are 2 things to get - the predicate & values for the result,
        #                             the predicate & values for the group

        stub = {'kind': 'winnow-many'}
        stub['group'] = self.visit(ctx.value(0))
        stub['predicate'] = self.visit(ctx.predicate(0))
        stub['values'] = []
        stub['group-values'] = []

        i = 2

        # get the first predicate values, if any
        for child in ctx.children[i+1:]:
            value = self.visit(child)
            if value is None:
                i += 1
                break                     # this is the ':' separator
            stub['values'].append(value)
            i += 1

        child = ctx.children[i+1]
        stub['group-predicate'] = self.visit(child)

        for child in ctx.children[i+2:]:
            # print('group-values ￫ ', self.visit(child))
            stub['group-values'].append(self.visit(child))

        return stub

    def visitWinnow_stub_directives(self, ctx: FalconParser.Stub_directivesContext):

        directives = []

        for child in ctx.children:
            if isinstance(child, FalconParser.Set_directiveContext):
                d = self.visitSet_directive(child, False)
                directives.append(d)
            elif isinstance(child, FalconParser.Set_single_directiveContext):
                d = self.visitSet_single_directive(child)
                directives.append(d)

        return directives

    # test/assert ------
    def visitStub_p(self, ctx: FalconParser.Stub_pContext):

        stub = {'kind': 'predicate', 'value': 'True', 'error-message': None}
        stub['predicate'] = self.visit(ctx.predicate())

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_pv(self, ctx: FalconParser.Stub_pvContext):

        stub = {'kind': 'predicate-value', 'value': None, 'error-message': None}

        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = self.visit(ctx.value())

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_many_pv(self, ctx: FalconParser.Stub_many_pvContext):

        stub = {'kind': 'predicate-value+', 'error-message': None}
        # stub['name'] = self.visit(ctx.label())
        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = tuple(self.visit(child) for child in ctx.children[2:])

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_code(self, ctx: FalconParser.Stub_codeContext):

        # stub = {}
        #
        # stub['kind'] = 'code'
        # # stub['value'] = str(ctx.CODESMNT()).strip('`')
        # stub['value'] = self.visit(ctx.code())

        return self.visit(ctx.code())

    def visitStub_side_effect(self, ctx: FalconParser.Stub_side_effectContext):

        stub = {'kind': 'predicate-side-effect', 'values': [], 'error-message': None}
        stub['name'] = self.visit(ctx.value())
        stub['predicate'] = self.visit(ctx.predicate())

        # if len(ctx.children) > 2:
        #     for child in ctx.children[3:]:
        #         stub['values'].append(self.visit(child))

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_side_effect_many(self, ctx: FalconParser.Stub_side_effect_manyContext):

        stub = {'kind': 'predicate-side-effect+', 'values': [], 'error-message': None}
        stub['name'] = self.visit(ctx.value(0))
        stub['predicate'] = self.visit(ctx.predicate())

        if len(ctx.children) > 2:
            for child in ctx.children[3:]:
                stub['values'].append(self.visit(child))

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_fail_side_effect(self, ctx: FalconParser.Stub_fail_side_effectContext):

        stub = {'kind': 'predicate-fail-side-effect', 'values': [], 'error-message': None}
        stub['predicate'] = self.visit(ctx.predicate())

        stub['error'] = self.visit(ctx.value()) if ctx.value() else None

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_fail_side_effect_many(self, ctx: FalconParser.Stub_fail_side_effect_manyContext):

        stub = {'kind': 'predicate-fail-side-effect+', 'values': [], 'error-message': None}
        stub['predicate'] = self.visit(ctx.predicate())

        has_error = isinstance(ctx.children[1], FalconParser.ValueContext) and isinstance(ctx.children[2], FalconParser.PredicateContext)
        stub['error'] = self.visit(ctx.value(0)) if has_error else None

        n = 3 if has_error else 2
        stub['value'] = tuple(self.visit(child) for child in ctx.children[n:])

        print(f'{has_error} ', stub['error'], ' children ', stub['value'])

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_directives(self, ctx: FalconParser.Stub_directivesContext):

        directives = []

        for child in ctx.children:
            if isinstance(child, FalconParser.Set_directiveContext):
                d = self.visitSet_directive(child, False)
                directives.append(d)
            elif isinstance(child, FalconParser.Set_single_directiveContext):
                d = self.visitSet_single_directive(child)
                directives.append(d)

        return directives

    def visitStub_assert(self, ctx: FalconParser.Stub_assertContext):

        stub = {'value': None, 'error-message': None}
        stub['kind'] = 'assertion'
        stub['argument'] = self.visit(ctx.arg_list())
        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = self.visit(ctx.value())

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_assert_p(self, ctx: FalconParser.Stub_assert_pContext):

        stub = {'value': None, 'error-message': None}
        stub['kind'] = 'assertion-p'
        stub['argument'] = self.visit(ctx.arg_list())
        stub['predicate'] = self.visit(ctx.predicate())
        stub['value'] = 'True'

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        return stub

    def visitStub_logical(self, ctx: FalconParser.Stub_logicalContext):

        stub = {'kind': 'logical', 'error-message': None}

        values = None
        okay_logicals = (FalconParser.Stub_logicContext,
                         FalconParser.Stub_logic_multiContext,
                         FalconParser.Stub_parenContext)

        for child in ctx.children:
            if isinstance(child, okay_logicals):
                # values.append(self.visit(child))
                values = self.visit(child)

        if ctx.STRING():
            stub['error-message'] = str(ctx.STRING())

        stub['values'] = values

        return stub

    # these deal with the logical stubs --
    def visitStub_logic(self, ctx: FalconParser.Stub_logicContext):

        stub = dict(kind='logic', values=[])

        for child in ctx.children:

            if isinstance(child, FalconParser.PredicateContext):
                stub['values'].append(self.visit(child))
            elif isinstance(child, FalconParser.ValueContext):
                # making a tuple of values
                if len(stub['values']) > 1 and isinstance(stub['values'][-1], tuple):
                    stub['values'][-1] += (self.visit(child),)
                else:
                    stub['values'].append((self.visit(child),))
                # stub['values'].append(self.visit(child))
            elif isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
                value = child.getText()
                stub['values'].append(value)

        # print(stub['values'])

        return stub

    def visitStub_logic_multi(self, ctx: FalconParser.Stub_logic_multiContext):

        stub = dict(kind='logic-multi', values=[])
        # values = []

        for child in ctx.children:

            if isinstance(child, (FalconParser.Stub_logicContext, FalconParser.Stub_parenContext)):
                s = self.visit(child)
                stub['values'].extend(s['values'])
            elif isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
                value = child.getText()
                stub['values'].append(value)

        return stub

    def visitStub_paren(self, ctx: FalconParser.Stub_parenContext):

        stub = dict(kind='logic-paren', values=[])
        # add {'values': {'predicate': value}}

        for child in ctx.children:

            if isinstance(child, FalconParser.PredicateContext):
                stub['values'].append(self.visit(child))
            elif isinstance(child, FalconParser.Stub_logicContext):
                s = self.visit(child)
                stub['values'].extend(s['values'])
            # elif isinstance(child, FalconParser.ValueContext):
            #     # print('some value…', child.getText())
            #     continue
            elif isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
                value = child.getText()
                stub['values'].append(value)

        # print('paren stub: ', stub['values'])

        return stub

    # Domain ------------------------------------

    def visitMake_domain(self, ctx: FalconParser.Make_domainContext):

        domain = {'kind': 'domain'}
        name = self.visit(ctx.name(0))
        domain['var-name'] = name
        domain['domain'] = self.visit(ctx.name(1))

        # self.ns[self.current_ns].setdefault('domains', {})[name] = domain
        self.ns[self.current_ns]['ordering'].append(('domain', domain))

        return

    def visitMake_domain_args(self, ctx: FalconParser.Make_domain_argsContext):

        domain = {'kind': 'domain-args'}
        name = self.visit(ctx.name(0))
        domain['var-name'] = name
        domain['domain'] = self.visit(ctx.name(1))
        domain['args'] = []
        domain['kwargs'] = {}

        for child in ctx.children:

            if isinstance(child, FalconParser.ValueContext):
                domain['args'].append(self.visit(child))
            elif isinstance(child, FalconParser.Make_fn_directiveContext):
                directive = self.visit(child)
                # domain['kwargs'][directive['fn-directive']] = directive['parameter']
                domain['kwargs'][directive[0]] = directive[1]
        # self.ns[self.current_ns].setdefault('domains', {})[name] = domain
        self.ns[self.current_ns]['ordering'].append(('domain', domain))

        return

    # -------------

    def visitGet_domain_name(self, ctx: FalconParser.Get_domain_nameContext):
        return [self.visit(ctx.name())]

    def visitGet_domain_names(self, ctx: FalconParser.Get_domain_namesContext):

        domains = []

        for child in ctx.children:
            if isinstance(child, FalconParser.NameContext):
                name = self.visit(child)
                domains.append(name)

        return domains
