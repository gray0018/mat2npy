import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

from scipy.io import loadmat

if __name__ == '__main__':

    filename = sys.argv[1]
    img = loadmat(filename)[filename[:-4]]

    np.save(filename[:-4], img)