import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('./image.png'))
print(repr(img))