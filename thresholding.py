'''
PS 1-2: Using OpenCV, write a Python program that takes as input a color image and paints bright/dark regions
with red to emphasize them. For example, the program reads an image of a circuit board,
“circuit_board.png,” shown in Figure 1(a), and generates another color image shown in Figure 1(d) by
painting the wiring red and keeping the background unchanged. Note: use the background of the input color
image, not the grayscale/black-and-white image.

Use this five-step method to achieve this color conversion:
    (1) Ask the user for an input color image and whether the program should emphasize brighter regions
        (wirings in Figure 1) or darker regions (cracks in Figure 2). Display the input image in the first
        window (see Figure 1(a)).
    (2) Convert the color image to a grayscale image and display the image in the second window (see
        Figure 1(b)); save and name the grayscale image file by adding “_grayscale” to the input filename.
        24-678: Computer Vision for Engineers 2
    (3) Convert the grayscale image to a binary image by using a threshold value that can differentiate the
        brighter regions and darker regions. Display the image in the third window (see Figure 1(c)); save
        and name the binary image file by adding “_binary” to the input filename.
    (4) Create the output color image by painting each pixel of the wiring red. Display the image in the
        fourth window (see Figure 1(d)); save and name the output image file by adding “_output” to the
        input filename.

For “circuit.png,” shown in Figure 1, we want to emphasize wiring regions, or brighter regions. On the other
hand, for “crack.png,” shown in Figure 2, we want to emphasize crack regions, or darker regions.
Your program should prompt the user to specify the filename of an input image, whether the program should
emphasize brighter regions or darker regions, display four images (input, grayscale, binary, and output) on
the screen, and save the grayscale, binary, and output image files in the same directory. Make sure to
include plenty of comment lines in your Python code.

Note to self: be sure to run "conda activate cve" before running this file

'''


import cv2
import sys
import numpy as np
import os

# get file input
print("Greetings! What photo would you like to edit? Your options are: ")
for file_names in os.listdir():
    if file_names.endswith(".png") or file_names.endswith(".jpg"):
        print("\t" + file_names)
input_file = input("\n input file: ")



# giving more chances if file name doesnt match
# while(input_file not in file_names):
#     print("That name is not valid. Please try again. Your options are: ")
#     for file_names in os.listdir():
#         if file_names.endswith(".png") or file_names.endswith(".jpg"):
#             print("\t" + file_names)
#     input_file = input("\n input file: ")
#     input_file = input_file.strip() #removes newline characters
#     print(input_file + "|")

# get mode
dark_cmp = False
hl_input = input("Got it! Type \"dark\" to highlight dark areas, or \"light\" to highlight brighter areas. ")
if(hl_input.lower().strip()== "dark"): #forces input to lowercase and removes whitespace for easier comparison
    dark_cmp = True
    print("Opening " + input_file + "in dark highlight mode...")
else:
    print("Opening " + input_file + "in bright highlight mode...")


cv2.namedWindow("input", cv2.WINDOW_NORMAL)
cv2.namedWindow("grayscale", cv2.WINDOW_NORMAL)
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
# cv2.namedWindow("input", cv2.WINDOW_NORMAL)

# read image
img = cv2.imread(input_file)
cv2.imshow("input", img)

# grayscale 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale", gray_image)
# @TODO: save image

# binary
bin_thresh = 70
if(dark_cmp):
    ret,thresh = cv2.threshold(gray_image,bin_thresh,255,cv2.THRESH_BINARY)
else:
    ret,thresh = cv2.threshold(gray_image,bin_thresh,255,cv2.THRESH_BINARY_INV)
cv2.imshow("mask", thresh)
# @TODO: save image




# waits unitl escape key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
