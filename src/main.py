import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
import fuzzyEdgeDetectionPDDO
import constants
from PIL import Image


def main():
    saveGrayScaleImage = False

    #for iThreshold in constants.THRESHOLDS:
    if sys.platform.startswith('linux'):
        pathToLena = \
             '../data/simData/Lena.png'
        pathToMembershipFunction = '../data/simData/triangularMembershipFunction.csv'

    else:
        pathToLena = \
            '..\\data\\simData\\Lena.png'
        pathToMembershipFunction = '..\\data\\simData\\triangularMembershipFunction.csv'

    image = cv2.imread(pathToLena)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if saveGrayScaleImage:
        im = Image.fromarray(image)
        im.save("../data/simData/LenaGrayScale.png")
    
    fuzzyEdgeDetector = fuzzyEdgeDetectionPDDO.fuzzyEdgeDetectionPDDO(image,pathToMembershipFunction)
    fuzzyEdgeDetector.solve()





    imagePlot = plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()

