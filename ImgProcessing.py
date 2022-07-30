from PIL import Image
import os
import cv2
import numpy as np

original_directory = "Images/Original"
modified_directory = "Images/Modified"


class ImgProcessor:
    def __init__(self,  size):
        self.size = size

    def modify(self, img, filename):
        self.img = np.asarray(Image.open(img))
        im_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)
        #cv2.resize(im_gray_th_otsu, self.size)
        inverted_image = self.invert(im_gray_th_otsu)
        os.chdir(modified_directory)
        cv2.imwrite(filename, inverted_image)

    def invert(self, image):
        return 255 - image

    def modify_all(self):
        for filename in os.listdir(original_directory):
            f = os.path.join(original_directory, filename)
            if os.path.isfile(f):
                self.modify(f, filename)

