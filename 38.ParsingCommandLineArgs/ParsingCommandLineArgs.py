# Author: Burak Dogancay
import argparse
import sys
def argumentParse():
  #enter command from commandline
  parser = argparse.ArgumentParser()
  parser.add_argument('name',help='name of user')
  parser.add_argument('-g', '--greeting',default='Hello',help='optional alternate greeting')
  
  args = parser.parse_args()
  print("{greeting}, {name}!".format(greeting=args.greeting,name=args.name))
  
def argvargs():
  words = sys.argv[1:]
  sentence = " ".join(words)
  print("[%s] %s" % (getpass.getuser(), sentence))
  # reverse and copy sys.argv
  argv = reversed(sys.argv)
  # extract the first element
  arg = argv.pop()
  # stop iterating when there's no more args to pop()
  while len(argv) > 0:
    if arg in ('-f', '--foo'):
      print('seen foo!')
    elif arg in ('-b', '--bar'):
      print('seen bar!')
    elif arg in ('-a', '--with-arg'):
      arg = arg.pop()
  print('seen value: {}'.format(arg))
  # get the next value
  arg = argv.pop()
  
def groupingArguments():
  parser = argparse.ArgumentParser(description='Simple example')
  parser.add_argument('name', help='Who to greet', default='World')
  parser.add_argument('--bar_this')
  parser.add_argument('--bar_that')
  parser.add_argument('--foo_this')
  parser.add_argument('--foo_that')
  args = parser.parse_args()

def main():
  argumentParse()
  argvargs()
  
if __name__ == '__main__':
    main()

  
  
    
