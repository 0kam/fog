from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from matplotlib import pyplot as plt

img = io.imread("images/single_photo/test1.jpeg")
ent = entropy(img[:,:,2], disk(50))
plt.imshow(ent)
plt.show()