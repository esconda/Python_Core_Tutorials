import glob
import cv2
import os
#Author: Burak Dogancay
import numpy as np



def glob_example(path):
    data = glob.glob(path + "*.png")
    numpyaarrayglob = np.array(data)
    print("Glob list",data)
    print("Numpy Array",numpyaarrayglob)
    print("Length of the array",len(numpyaarrayglob))

    for i in data:
        frame = cv2.imread(i)
        cv2.imshow(i, frame)
        cv2.waitKey(3000)

def another_method1(path):

    #lengthofthefile = [for name in os.get]
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            frame = cv2.imread(path+filename)
            cv2.imshow(filename, frame)
            cv2.waitKey(3000)




def main():
    path ="D:/Projeler/Datasets/satellite/Background/yedek/"
    glob_example(path)
    another_method1(path)

if __name__=='__main__':
    main()