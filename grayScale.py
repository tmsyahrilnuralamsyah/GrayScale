import cv2
import numpy as np
from matplotlib import pyplot as plt

def showHist(image):
    image1 = cv2.imread(image)
    image2 = cv2.imread(image, 0)
    color = ('b', 'g', 'r')
    mask = np.zeros(image2.shape[:2], np.uint8)
    hist_full = cv2.calcHist([image2], [0], None, [256], [0,256])
    hist_mask = cv2.calcHist([image2], [0], mask, [256], [0,256])

    plt.subplot(221), plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(image2, 'gray')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223),
    for i,col in enumerate(color):
        hist = cv2.calcHist([image1], [i], None, [256], [0,256])
        plt.plot(hist, color = col)
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0,256])
    plt.show()

showHist("foto-terang.jpg")
showHist("foto-gelap.jpg")