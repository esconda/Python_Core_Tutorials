# Author: Burak Dogancay
from socket import socket, SOCK_RAW,AF_INET,SOCK_DGRAM,SOCK_STREAM,SO_REUSEADDR,SOL_SOCKET
import threading


def rawSocketLinux():
  mySocket = socket(AF_PACKET, SOCK_RAW)
  mySocket.bind(("eth1",0))
  
  #Ethernet Frame Structure is:
  
  src_addr = "\x01\x02\x03\x04\x05\x06"
  dst_addr = "\x01\x02\x03\x04\x05\x06"
  payload = ("["*30)+"PAYLOAD"+("]"*30)
  checksum = "\x1a\x2b\x3c\x4d"
  ethertype = "\x08\x01"
  
  mySocket.send(dst_addr+src_addr+ethertype+payload+checksum)

#UDP is a connectionless protocol. This means that peers sending messages do not require establishing a
#connection before sending messages. socket.recvfromthus returns a tuple (msg [the message the socket received],
#addr [the address of the sender])
def sendingDataUDP(): #CLIENT
  msgInfo = ("Incredible Socket").encode('utf-8')
  destination = ('localhost', 6667)
  UdpSocket = socket(AF_INET,SOCK_DGRAM)
  while True:
    UdpSocket.sendto(msgInfo,destination)

def readingDataUDP():#SERVER
  destination = ('localhost', 6667)
  UdpSocket = socket(AF_INET,SOCK_DGRAM)
  UdpSocket.bind(destination)
  
  while True:
    rcvMsg, adress = UdpSocket.recvfrom(8192)
    print("Recieved Message is : ", (rcvMsg).decode())

def runNetworkUdp():
  #------------------UDP SOCKET------------------
  #sending reading message via UDP with threading
  sendingThread = threading.Thread(target=sendingDataUDP)
  readingThread = threading.Thread(target=readingDataUDP)
  
  sendingThread.start()
  readingThread.start()
  
  sendingThread.join()
  readingThread.join()
  #----------------------------------------------
  
#When run with no arguments, this program starts a TCP socket server that listens for connections to 127.0.0.1 on
#port 6666. The server handles each connection in a separate thread.
def sendingDataTcp():#TCP CLIENT EXAMPLE
  destination = ('localhost', 6666)
  TcpSocket = socket(AF_INET,SOCK_STREAM)
  TcpSocket.connect(destination)
  while True:
    TcpSocket.send(("Hello, everything is fine").encode('utf-8'))
  
def readingDataTcp():#TCP SERVER EXAMPLE
  destination = ('localhost', 6666)
  TcpSocket = socket(AF_INET,SOCK_STREAM)
  TcpSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
  TcpSocket.bind(destination)
  TcpSocket.listen(10)
  conn, addr = TcpSocket.accept()
  while True:
    data = conn.recv(1024)
    print("TCP Received Data is : ", data.decode())
    
def runNetworkTcp():
  #------------------TCP SOCKET------------------
  #sending reading message via UDP with threading
  sendingThread = threading.Thread(target=sendingDataTcp)
  readingThread = threading.Thread(target=readingDataTcp)
  
  sendingThread.start()
  readingThread.start()
  
  sendingThread.join()
  readingThread.join()
  #----------------------------------------------
    

def main():
  #rawSocketLinux()
  
  #------------------UDP SOCKET------------------
  #runNetworkUdp()
  #----------------------------------------------
  
  #------------------TCP SOCKET------------------
  runNetworkTcp()
  #----------------------------------------------
  

if __name__ == '__main__':
    main()