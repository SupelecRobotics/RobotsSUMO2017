import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('schema_table.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
