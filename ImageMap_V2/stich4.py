from panorama import Stitcher
import imutils
import cv2

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread('file1.jpg')
imageB = cv2.imread('file2.jpg')
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

imageC = cv2.imread('file3.jpg')
imageD = cv2.imread('file4.jpg')
imageC = imutils.resize(imageC, width=400)
imageD = imutils.resize(imageD, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result2, vis2) = stitcher.stitch([imageC, imageD], showMatches=True)


imageE = result
imageF = result2
# stitch the images together to create a panorama
stitcher = Stitcher()
(result3, vis3) = stitcher.stitch([imageE, imageF], showMatches=True)


cv2.imwrite("4stichedimages.jpg", result3)
cv2.waitKey(0)
