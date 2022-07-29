from PIL import Image


class ImgProcessor:
    def __init__(self, img, size):
        self.img = Image.open(img)
        self.size = size

    def resize(self):
        img_resized = self.img.resize(self.size)
        im_resize = img_resized.save(self.img + "_resized", "PNG")