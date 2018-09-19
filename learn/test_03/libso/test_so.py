# ! /usr/bin/env python
# test_so.py
from ctypes import cdll
import os
p = os.getcwd() + '/libfunc.so'
f = cdll.LoadLibrary(p)
print f.func(99)