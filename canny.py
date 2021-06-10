import cv2
from matplotlib import pyplot as plt

img = "images/single_photo/test1.jpeg"

img = cv2.imread(img)
edge = cv2.Canny(img[:,:,1], 5,30)
plt.imshow(edge, cmap = "gray")
plt.show()