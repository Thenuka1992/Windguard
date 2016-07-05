import cv2
import numpy as np

i = 0
count = 0
vidcap = cv2.VideoCapture('C:\Users\Thenuka\Documents\WindGuard\imageMap\V3\vediocap\vid5.mp4')
success,image = vidcap.read()
print success

while success:
    success,image = vidcap.read()

    getvalue = vidcap.get(0)
    print "get value = "+str(getvalue)
    print "count id = "+str(count)
    
    if count%60 == 0:
        cv2.imwrite("frame%d.jpg" %count, image)

    if cv2.waitKey(10) == 27:                     
        break
    count += 1
