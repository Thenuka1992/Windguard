import cv2
import numpy as np
i =0
imgArray = []
croppedArray1 = []
croppedArray2 = []


#reading the image using cv2

for i in range(8):
    
    name = "map"+str(i)+".jpg"
    imgArray.append(cv2.imread(name));
    print "Img"+str(i)+".jpg added successfully"


#get a default height and width of a single image
h1, w1, c1 = imgArray[0].shape

print "\n"

for i in range(4):
    croppedArray1.append(imgArray[i][1:h1, 1:w1])
    print "crop"+str(i)+" added sucessfully"


for i in range(4,8):
    croppedArray2.append(imgArray[i][1:h1, 1:w1])
    print "crop"+str(i)+" added sucessfully"

#get height and width of a single crop partition
height, width, channels = croppedArray1[0].shape

#create a null image using numpy with all zeros with diemnetions = 4*width
blank_image = np.zeros((height,width*4,channels), np.uint8)
blank_image2 = np.zeros((height,width*4,channels), np.uint8)


#add each croped partition consecutive locations of empty image file
blank_image[:,0:width] = croppedArray1[0]      
blank_image[:,width:width*2] = croppedArray1[1]
blank_image[:,2*width:width*3] = croppedArray1[2]
blank_image[:,width*3:width*4] = croppedArray1[3]

blank_image2[:,0:width] = croppedArray2[0]      
blank_image2[:,width:width*2] = croppedArray2[1]
blank_image2[:,2*width:width*3] = croppedArray2[2]
blank_image2[:,width*3:width*4] = croppedArray2[3]

#Write out the final image file to disk
cv2.imwrite("testing1.jpg", blank_image)
cv2.imwrite("testing2.jpg", blank_image2)

print " \nimage testing1.jpg saved successfully"
print " \nimage testing2.jpg saved successfully"

#create a null image using numphy of height*2 and width*4
blank_image3 = np.zeros((height*2,width*4,channels), np.uint8)

#add testing1 and testing two together 
blank_image3[:height] = blank_image
blank_image3[height:] = blank_image2

#write final image to disk
cv2.imwrite("testing3.jpg", blank_image3)

print " \nimage testing3.jpg saved successfully"


#Display the final image with a fixed window size
cv2.namedWindow('Test1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Test1', 1200, 600)
cv2.imshow('Test1', blank_image3)
cv2.waitKey(0)
cv2.destroyAllWindows()


