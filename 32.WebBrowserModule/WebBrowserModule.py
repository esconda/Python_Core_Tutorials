# Author: Burak Dogancay
import webbrowser

def openBrowser():
    webbrowser.open("https://www.youtube.com/watch?v=Jo2sA_GfLHY")

def openNewTab():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=O3ydI3_X_Q4")
     
def getBrowser():
    browserPath = webbrowser.get("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe")
    browser = webbrowser.get(browserPath)
    print("--BROWSER  NAME--")
    print(browser)
    print("---------------------")  

def registerBrowser():
    browserPath = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe")
    browser = webbrowser.get(browserPath)
    webbrowser.register('firefox', None, browser)
    # Now to refer to use Firefox in the future you can use this
    webbrowser.get('firefox').open("https://stackoverflow.com/")
    
def main():
    openBrowser()
    openNewTab()
    #getBrowser()
    #registerBrowser()
    

if __name__ == '__main__':
    main()