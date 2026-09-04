from PIL import Image, ImageFilter
import cv2
import numpy as np
import os
import sys


def load_and_blur(path):
    img = Image.open(path)
    return img.filter(ImageFilter.BLUR)


def load_with_opencv(path):
    return cv2.imread(path)


def to_array(img):
    return np.array(img)
