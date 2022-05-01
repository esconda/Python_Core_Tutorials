#Author: Burak Dogancay
#ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. 
# It can be used to wrap these libraries in pure Python.
from ctypes import *
def basicUsage():
    libc = cdll.LoadLibrary('libc.so.6')
    getFuncObject = libc.func

def complexUsage():
    #Let's combine all of the examples above into one complex scenario: using libc's lfind function
    compar_proto = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
    lfind_proto = CFUNCTYPE(c_void_p, c_void_p, c_void_p, POINTER(c_uint), c_uint, compar_proto)
    
    key = c_int(12)
    arr = (c_int * 16)(*range(16))
    nmemb = c_uint(16)
    
def main():
    


if __name__ == '__main__':
    main()
