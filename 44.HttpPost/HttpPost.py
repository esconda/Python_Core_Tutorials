# Author: Burak Dogancay
from requests import post
#THIS MODULE IS USED FOR SENDING POST FROM CLIENT TO SERVER
def simplePosting():
    specPost = post('http://httpbin.org/post', data = {'key':'value'})
    print("--FIRST POST SPECIFICATION--")
    print("HEADERS: ",specPost.headers)
    print("HISTORY: ",specPost.history)
    print("JSON: ",specPost.json)
    print("---------------------") 
    
    #Headers can also prepared before post

  
  
  
def main():
    simplePosting()


if __name__ == '__main__':
    main()