from PIL import Image
import os

original_directory = "Images/Original"
modified_directory = "Images/Modified"


class ImgProcessor:
    def __init__(self,  size):
        self.size = size

    def resize(self, img):
        self.img = Image.open(img)
        img_resized = self.img.resize(self.size)
        im_resize = img_resized.save("resized_img.jpg")


    def resize_all(self):
        for filename in os.listdir(original_directory):
            f = os.path.join(original_directory, filename)
            if os.path.isfile(f):
                self.resize(f)
