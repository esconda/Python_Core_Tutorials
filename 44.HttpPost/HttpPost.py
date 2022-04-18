# Author: Burak Dogancay
from requests import post
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import os
#THIS MODULE IS USED FOR SENDING POST FROM CLIENT TO SERVER

def getSpecFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName

def simplePosting():
    specPost = post('http://httpbin.org/post', data = {'key':'value'})
    print("--FIRST POST SPECIFICATION--")
    print("HEADERS: ",specPost.headers)
    print("HISTORY: ",specPost.history)
    print("JSON: ",specPost.json)
    print("---------------------") 
    
    #Headers can also prepared before post
    
    #SSL VERIFICATION
    #Requests by default validates SSL certificates of domains
    specPostSsl = post('http://httpbin.org/post', data = {'key':'value'}, verify=False)
    
    #REDIRECTION
    #Any redirection will be followed (e.g. http to https) this can also be changed:
    specPostRedirect = post('http://httpbin.org/post', data = {'key':'value'}, allow_redirects=False)
    
    print("--SECOND AND THIRD POST SPECIFICATION--")
    print("URL: ",specPostSsl.url)
    print("HISTORY: ",specPostRedirect.history)
    print("---------------------") 

def formEncodedData():
#To pass form encoded data with the post operation, data must be structured as dictionary and supplied as the data parameter
    payload = {'key1' : 'value1',
               'key2' : 'value2'}
    specPostPayload = post('http://httpbin.org/post', data=payload)
    
def fileUpload():
    
    #Single file upload
    files = {'file' : open(getSpecFile('data.txt'), 'rb')}
    specPostFileLoad = post('http://http.org/post', files=files)
    
    #Multiple File load
    multiple_files = [
                      ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
                      ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
    specMultiFileLoad = post('http://httpbin.org/post', files=multiple_files)

def response():
    #Response codes can be viewed from a post operation:
    specPostResponse = post('http://httpbin.org/post', data={'data' : 'value'})
    print("--RESPONSE POST SPECIFICATION--")
    print("Status Code: ",specPostResponse.status_code)
    print("Returned Data: ",specPostResponse.text)
    print("Raw Response : ", specPostResponse.raw.read())
    print("---------------------") 

def authenticationFunc():
    #Simple HTTP Authentication 
    authenticationPost = post('http://natas0.natas.labs.overthewire.org', auth=HTTPBasicAuth('natas0', 'natas0'))
    
    #Digest Authentication
    digestAuthPost = post('http://natas0.natas.labs.overthewire.org', auth=HTTPDigestAuth('natas0', 'natas0'))

def proxyPost():
    #Each request POST operation can be configured to use network proxies
    proxies = {
                'http': 'http://192.168.0.128:3128',
                'https': 'http://192.168.0.127:1080',
                }
    proxyPost = post('http://httpbin.org/post', proxies=proxies)
    
    #Socket Proxy settings
    proxiesSock = {
                'http': 'socks5://user:pass@host:port',
                'https': 'socks5://user:pass@host:port'
                }
    proxySockPost = post('http://httpbin.org/post', proxies=proxiesSock)
  
def main():
    simplePosting()
    formEncodedData()
    #fileUpload()
    response()
    authenticationFunc()
    proxyPost()


if __name__ == '__main__':
    main()