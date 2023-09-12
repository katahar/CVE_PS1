'''
Using OpenCV, write a Python program that takes as input a color image and applies gamma correction to
make the image more natural-looking and/or appealing. Use your program to find the gamma value that
makes an image as natural-looking and/or appealing as possible.
Your program should:
    (1) Ask the user for an input color image and open two image display windows, one for the original image
        (Window 1) and the other for a gamma-corrected image (Window 2),
    (2) Ask the user to specify a gamma value and show the corrected image in Window 2,
    (3) Repeat Step 2 iteratively until you find the best gamma value, and
    (4) Save the final corrected image file; name the file by adding “_gcorrected” to the input file name.

Make sure to include plenty of comment lines in your Python code. Apply your program to two files,
smiley.jpg and carnival.jpg, shown in Figures 3 and 4

Note to self: be sure to run "conda activate cve" before running this file

'''


import cv2
import os
import numpy as np


def gamma_corr(img, gamma =1):
    
    # building lookup table for gamma-corrected values that will be applied to all channels
    lookup_table = np.zeros(256)
    for i in range(256):
        lookup_table[i] = ( (i/255) ** (1/gamma) ) * 255
    lookup_table = np.array(lookup_table, np.uint8) # makes sure that an 8 bit integer is used

    # uses lookup table to scale each channel of the image
    return cv2.LUT(img, lookup_table)



# get file input
print("Greetings! What photo would you like to edit? Your options are: ")
for file_names in os.listdir():
    if file_names.endswith(".png") or file_names.endswith(".jpg"):
        print("\t" + file_names)
input_file = input("\n input file: ")


# creating empty named windows for later population
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE )
cv2.namedWindow("gamma-corrected", cv2.WINDOW_AUTOSIZE )


# read image
img = cv2.imread(input_file)
cv2.imshow("input", img)

# extracting extension and file base name
extension = input_file[-4:]
input_file = input_file[:-4]


# gamma correction
gamma_img = img
while True: 
    input_val = input("Enter new gamma value here! Type \"done\" if you were happy with your last image. \nInput: ")
    if(input_val.lower().strip()== "done"): #forces input to lowercase and removes whitespace for easier comparison
        break
    elif (input_val.lower().strip()== ""): #accounts for accidental enter presses
        # do nothing
        print("")
    else: #applies gamma correction function and renders images
        gamma = float(input_val)
        gamma_img = gamma_corr(img, gamma)
        cv2.imshow("input", img)
        cv2.imshow("gamma-corrected", gamma_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

print("Saving gamma-corrected image...")
cv2.imwrite(input_file+"_gcorrected"+extension, gamma_img)

