# Author: Burak Dogancay
import subprocess
import shlex
#Errors detected during execution are called exceptions and are not unconditionally fatal. Most exceptions are not
#handled by programs; it is possible to write programs that handle selected exceptions.
#eXCEPTİONS ARE:
""" BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- StopAsyncIteration
+-- ArithmeticError
| +-- FloatingPointError
| +-- OverflowError
| +-- ZeroDivisionError
+-- AssertionError
+-- AttributeError
+-- BufferError
+-- EOFError
+-- ImportError
+-- LookupError
| +-- IndexError
| +-- KeyError
+-- MemoryError
+-- NameError
| +-- UnboundLocalError
+-- OSError
| +-- BlockingIOError
| +-- ChildProcessError
| +-- ConnectionError
| | +-- BrokenPipeError
| | +-- ConnectionAbortedError
| | +-- ConnectionRefusedError
| | +-- ConnectionResetError
| +-- FileExistsError
| +-- FileNotFoundError
| +-- InterruptedError
| +-- IsADirectoryError
| +-- NotADirectoryError
| +-- PermissionError
| +-- ProcessLookupError
| +-- TimeoutError
+-- ReferenceError
+-- RuntimeError
| +-- NotImplementedError
| +-- RecursionError
+-- SyntaxError
| +-- IndentationError
| +-- TabError
+-- SystemError
+-- ValueError
| +-- UnicodeError
| +-- UnicodeDecodeError
| +-- UnicodeEncodeError
| +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning
+-- ResourceWarning
+-- TypeError """
def catchExceptions():
  try:
    var= 15 / 0
  
  except ZeroDivisionError as e:
    #e is exception object
    print("Variable divided by zero,exceptions is :",e)
    #handle exception
    var=0
  finally:
    print("The END")
    
def reRaisingException():
  try:
    15/0
  except ZeroDivisionError as e:
    print("Got an Error",e)
    raise
  
def catchMultipleExceptions():
  try:
    d = {}
    a = d[1]
    b = d.non_existing_field
  except KeyError as e:
    print("A KeyError has occurred. Exception message:", e)
  except AttributeError as e:
    print("An AttributeError has occurred. Exception message:", e)
    

  
def main():
  catchExceptions()
  catchMultipleExceptions()
  #reRaisingException()


if __name__ == '__main__':
    main()