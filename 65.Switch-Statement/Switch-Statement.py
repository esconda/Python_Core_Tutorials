# Author: Burak Dogancay

def switch(value):
  if value == 1: 
    return "one TB2"
  if value == 2:
    return "two Aksungur"
  if value == 42:
    return "fourty two Akinci"  
  raise Exception("No case found")

class CustomSwitch:
  def case_1(self):
    return 'one'
  def case_2(self):
    return 'two'
  def case_3(self):
    return 'three'
  def default(self):
    return 'default'
  


def main():
  #First switch
  switch(1)
  
  #Second Switch
  switchX = CustomSwitch()
  print(switchX.case_1())
  

  

if __name__ == '__main__':
    main()