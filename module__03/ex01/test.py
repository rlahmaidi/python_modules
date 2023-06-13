import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# img = Image.open('./image.png')
# print("the type of the object is", type(img))
# print("the format and size and mode are")
# print(img.format, img.size, img.mode)
try:
    img = np.asarray(Image.open('./image.png'))
except FileNotFoundError as fn:
    print(fn)
# print(type(img))
# print(repr(img))
# print(img)