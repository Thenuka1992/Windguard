#import packages cv2 and time
import cv2
import time


i = 0

#set default camera port and frames per sec
camera_port = 0
ramp_frames = 30

#set default camera to capture frames
camera = cv2.VideoCapture(camera_port)


#read the frame into a image object
def get_image():
    retval, im = camera.read()
    return im

#Save the images into sperate files
def save_image():
    
    for i in range(4):
        camera_capture = get_image()
        file = "test_image"+ str(i) + ".png"
        cv2.imwrite(file, camera_capture)
        print "photo taken"
        time.sleep(2)

        
#Call the function to get and save images
save_image()
del(camera)  
 

 



