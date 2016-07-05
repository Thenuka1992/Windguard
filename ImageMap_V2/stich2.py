import os
from panorama import Stitcher
import imutils
import cv2


def fileCount():
    count = 0
    
    for filename in os.listdir("."):
        if filename.endswith(".jpg"):
            count = count + 1
            
    return count

def getFileNames():
    nameArray = []
    
    for filename in os.listdir("."):
        if filename.endswith(".jpg"):
            nameArray.append(filename)
            
    return nameArray

'''imageA = cv2.imread('file0.jpg')
imageB = cv2.imread('file1.jpg')


# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)'''

stitcher = Stitcher()

filename = getFileNames()

count = fileCount()

image1 = cv2.imread(filename[0])
for i in range(2):    
    image2 = cv2.imread(filename[i+1])
    (result, vis) = stitcher.stitch([image1, image2], showMatches=True)
    image1 = result
    
    
cv2.imwrite("2stichedimages.jpg", result)
#cv2.imshow("Result2", vis)
cv2.waitKey(0)


