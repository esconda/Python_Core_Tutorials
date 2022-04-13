# Author: Burak Dogancay
import subprocess
import shlex

def launchingsubProcess():
  process = subprocess.Popen([r'C://Program Files//Google//Chrome//Application//chrome.exe', 'arg1', '--flag', 'arg'])
  print("Hello")
  process.wait()

def readingOutput():
  process = subprocess.Popen([r'C://Program Files//Google//Chrome//Application//chrome.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  # This will block until process completes
  stdout, stderr = process.communicate()
  print (stdout)
  print (stderr)
  
def writingSubprocess():
  process = subprocess.Popen([r'C://Program Files//Google//Chrome//Application//chrome.exe'], stdout = subprocess.PIPE, stdin =subprocess.PIPE)
  process.stdin.write('line of input\n') # Write input
  line = process.stdout.readline() # Read a line from stdout
  print(line)

def callExternalCommands():
  #The simplest use case is using the subprocess.call function. It accepts a list as the first argument. The first item in
  #the list should be the external application you want to call. The other items in the list are arguments that will be
  #passed to that application.
  subprocess.call([r'C:\path\to\app.exe', 'arg1', '--flag', 'arg'])
  subprocess.call('echo "Hello, world"', shell=True)
  shlex.split('ls --color -l -t -r')
  
def main():
  launchingsubProcess()
  readingOutput()
  #writingSubprocess()


if __name__ == '__main__':
    main()