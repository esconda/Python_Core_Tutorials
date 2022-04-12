# Author: Burak Dogancay

def basicSlicing():
   variable = "Burak Dogancay"
   print("--BASIC SLICING--")
   print("Last variable:", variable[-1])
   print("All variable:", variable[:])
   print("All variable 2:", variable[::])
   print("From index 4 to end:", variable[4:])
   print("From beginning to position 6:", variable[:4])
   print("From index 3 to 10:", variable[3:10])
   print("Every 2nd element:", variable[::2])
   print("From index 1, to index 4 (excluded), every 2nd element): ", variable[1:4:2])
   print("Beginning to last position:", variable[:-1])
   print("Every 2nd element:", variable[::2])
   print("---------------------")
    
def main():
  basicSlicing()
    

if __name__ == '__main__':
    main()