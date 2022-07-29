from PIL import Image


class ImgProcessor:
    def __init__(self,  size):
        self.size = size

    def resize(self, img):
        self.img = Image.open(img)
        img_resized = self.img.resize(self.size)
        im_resize = img_resized.save("resized_img.jpg")