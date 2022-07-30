from PIL import Image
import os

original_directory = "Images/Original"
modified_directory = "Images/Modified"


class ImgProcessor:
    def __init__(self,  size):
        self.size = size

    def resize(self, img, filename):
        self.img = Image.open(img).convert('L')
        img_resized = self.img.resize(self.size)
        os.chdir(modified_directory)
        im_resize = img_resized.save(filename + "_resized.jpg")


    def modify_all(self):
        for filename in os.listdir(original_directory):
            f = os.path.join(original_directory, filename)
            if os.path.isfile(f):
                self.resize(f, filename)

