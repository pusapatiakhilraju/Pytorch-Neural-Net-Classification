import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import cv2


class ImagePreprocessor:
    def __init__(self):
        self.folder = "/Users/akhil/Documents/Machine learning/Datasets/Cat vs Dog classifier/train"
        self.dict = {0: 'Cat', 1: ' Dog'}

    def load_data(self):
        labels = []
        images = []
        for file_name in os.listdir(self.folder):
            if file_name.split(".")[0] == "cat":
                image = cv2.imread(self.folder+"/"+file_name)
                images.append([image, 0])
            else:
                image = cv2.imread(self.folder+"/"+file_name)
                images.append([image, 1])

        return images

    def plot_image(self, image):
        plt.imshow(cv2.cvtColor(image[0], cv2.COLOR_BGR2RGB))
        plt.title(self.dict[image[1]])
        plt.show()


a = ImagePreprocessor()
images = a.load_data()
a.plot_image(images[0])
