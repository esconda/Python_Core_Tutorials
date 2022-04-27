# Author: Burak Dogancay
import serial 
from serial.tools import list_ports
def initSerialDevice():
  ser = serial.Serial('/dev/ttyUSB0', 9600)
  
def readSerialPort():
  ser = serial.Serial('/dev/ttyUSB0', 9600)
  data = ser.read(size=5)# read single bute
  daat2 = ser.readline() #read oneline from serial device
  data3 = ser.read(ser.in_waiting())
  
def infoSerialPort():
  ser = serial.Serial('/dev/ttyUSB1', 9600)
  print("--SERIAL PORT--")
  print("Baudrate", ser.baudrate )
  print("Port", ser.portstr )
  print("Name",ser.name)
  print("-----------------")

def checkSerialPorts():
  print("--LIST OF SERIAL PORT--")
  for comport in list_ports.comports():
    print(comport)
  print("-----------------")

  
  
  

def main(): 
  #infoSerialPort()
  checkSerialPorts()
 
if __name__ == '__main__':
    main()