# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
import argparse
import imutils
import cv2
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, ElementNotInteractableException, TimeoutException

"""
# construc the argument parse and parse the arguments
# its used to load the images from the command line interface by using
# this command  # python image_diff.py --first 1.jpg --second 2.jpg
                # python image_diff.py --first 1_1.jpg --second 2_1.jpg

# copy paste these 4 lines of code below and you will be able to use the below commands in the terminal
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image")
ap.add_argument("-s", "--second", required=True, help="second input image")
args = vars(ap.parse_args())

#load two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

"""
# pyautogui.screenshot("2_6.jpg")


# load two input images
img1_path = "C:\\image_recog\\images\\1_6.jpg"
img2_path = "C:\\image_recog\\images\\2_6.jpg"

imageA = cv2.imread(img1_path)
imageB = cv2.imread(img2_path)


## get image dimensions
# heightA, widthA, channelsA = imageA.shape
# heightB, widthB, channelsB = imageB.shape
# print(heightA, widthA, channelsA)
# print(heightB, widthB, channelsB)
# sumof = height + width
# print(sumof)

# conver the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)


#COMPUTE THE STRUCTURAL SIMILARITY INDEX (SSIM) between the two
# images, ensuring that the difference in the images is returned
(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff* 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0 , 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0]
# LOOP OVER THE CONTOURS
for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)



# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# different show



# python image_diff.py --first 1.jpg --second 2.jpg
# python image_diff.py --first 1_1.jpg --second 2_1.jpg