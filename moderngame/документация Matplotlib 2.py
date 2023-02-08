import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.array(Image.open('IMG_20211124_160711.jpg'))
data = np.random.randint(0, 255, (100, 100))

# fig = plt.figure(figsize=(6, 4))
# ax = fig.add_subplot()
# ax.imshow(img)

# Можно записать всё проще вот так внизу

plt.imshow(img, cmap='inferno')


plt.show()
