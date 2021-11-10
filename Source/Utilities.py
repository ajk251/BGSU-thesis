

from collections import namedtuple
from inspect import getfullargspec, signature

FnDesc = namedtuple('FnDesc', 'name, module, kind, n_args, total_args, args, var_args, kw_args, default_args, annotations')

# ---------------------------------------------------------

def desc_fn(func):
    
    fn_spec = getfullargspec(func)
    fn_sig  = signature(func)
    # fn_pm   = 
    
    fnds = FnDesc(func.__name__,
                  func.__module__,  # inspect.getmodule(func)
                  fn_sig.kind,
                  len(fn_spec.args),
                  len(fn_spec.args) + len(fn_spec.defaults) + len(fn_spec.kwonlyargs),
                  fn_spec.args,
                  fn_spec.varargs,
                  fn_spec.kwonlyargs,
                  func.__defaults__)
    
    return fnds
    

# ---------------------------------------------------------    

def add1(n):
    return n + 1

def add2(m, n):
    return n + m

def add3(m, n, o):
    return m + n + o

def add4(m, n, o, q=1):
    return m + m + o + q



print(desc_fn(add1))
