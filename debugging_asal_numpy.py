import importlib, traceback
try:
    import numpy
    print('numpy imported from:', getattr(numpy,'__file__', repr(numpy)))
except Exception:
    traceback.print_exc()
