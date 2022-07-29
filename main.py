import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

import ImgProcessing

X, y = make_blobs(centers=3, n_samples=500, random_state=1)
fig, ax = plt.subplots(figsize=(4, 4))
ax.scatter(X[:, 0], X[:, 1], alpha=0.5)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')

imgprocessor = ImgProcessing.ImgProcessor((480,640))
imgprocessor.resize("Sample Car.jpg")

