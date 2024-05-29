import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
import fuzzyEdgeDetectionPDDO
import constants

def main():
    
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
        
    fuzzyEdgeDetector = fuzzyEdgeDetectionPDDO.fuzzyEdgeDetectionPDDO(image,pathToMembershipFunction)
    fuzzyEdgeDetector.solve()





    imagePlot = plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()

