# Author: Burak Dogancay
from struct import pack,unpack
import struct

from importlib_metadata import Sectioned

def formatToByte():
  print("--BYTE VALUE--")
  print(pack('I3c', 25, b'a', b'b', b'c'))
  print("--------------")

def unpackByte():
  print("--UNPACK VALUE--")
  print(unpack('I3c', b'\x19\x00\x00\x00abc'))
  print("--------------")
  
def packMethod():
  firstBuffer = struct.pack("hhh",6,7,8)
  print("Native byte order : ", repr(firstBuffer))
  
  secondBuffer = struct.pack("!hhh",2,3,4)
  print("Network byte order : ",repr(secondBuffer))
  

def main():
  formatToByte()
  unpackByte()
  packMethod()
  


if __name__ == '__main__':
    main()