# Author: Burak Dogancay
import urllib
import urllib.request
import urllib


def httpGet():
  response = urllib.request.urlopen("http://stackoverflow.com/documentation/")
  print("--HTTP GET--")
  print("Code size : ",response.code)#Getcode size
  print("Whole code : ",response.read())#get all bacground code
  print("---------------------")  
  
def httpPost():
  #To POST data pass the encoded query arguments as data to urlopen()
  query_parms = {'username':'stackoverflow', 'password':'me.me'}
  encoded_parms = urllib.parse.urlencode(query_parms).encode('utf-8')
  response = urllib.request.urlopen("https://stackoverflow.com/users/login", encoded_parms)
  print("--HTTP POST--")
  print("Code size : ",response.code)#Getcode size
  print("Whole code : ",response.read())#get all bacground code
  print("---------------------") 
  
def httpDecoding():
  #The received bytes have to be decoded with the correct character encoding to be interpreted as text:
  response = urllib.request.urlopen("http://stackoverflow.com/")
  data = response.read()
  
  encoding = response.info().get_content_charset()
  html = data.decode(encoding)
  print(html)
  
def main():
  #httpGet()
  #httpPost()
  httpDecoding()


if __name__ == '__main__':
    main()