import numpy as np

NX = 512
NY = 512
HORIZONGRADIENT = 2.015

PDDOGRADIENTKERNEL = np.loadtxt('../data/simData/PDDOGradientKernel.csv', delimiter=",")

PDDOLAPLACIANKERNEL = np.loadtxt('../data/simData/PDDOLaplacianKernel.csv', delimiter=",")

HORIZONGRADIENT = 2.015
KERNELDIMGRADIENT = 5
GMASKGRADIENT = np.ones((KERNELDIMGRADIENT, KERNELDIMGRADIENT))

HORIZONLAPLACIAN = 3.015
KERNELDIMLAPLACIAN = 7
GMASKLAPLACIAN = np.ones((KERNELDIMLAPLACIAN, KERNELDIMLAPLACIAN))

#GCENTER = np.array([-255, -244.80, -234.60, -224.40, -214.20, -204, -193.80, -183.60, -173.40, -163.20, -153, -142.80, -132.60, -122.40, -112.20, -102, -91.80, -81.60, -71.40, -61.20, -51, -40.80, -30.60, -20.40, -10.20, 0, 10.20, 20.40, 30.60, 40.80, 51, 61.20, 71.40, 81.60, 91.80, 102, 112.20, 122.40, 132.60, 142.80, 153, 163.20, 173.40, 183.60, 193.80, 204.00, 214.20, 224.40, 234.60, 244.80, 255.00])

#GCENTER = np.array([-80, -76.80, -73.60, -70.40, -67.20, -64.00, -60.80, -57.60, -54.40, -51.20, -48.00, -44.80, -41.60, -38.40, -35.20, -32.00, -28.80, -25.60, -22.40, -19.20, -16.00, -12.80, -9.59,	-6.39, -3.19, 0, 3.20, 6.40, 9.60, 12.80, 16, 19.20, 22.40, 25.60, 28.80, 32.00, 35.20, 38.40, 41.60, 44.80, 48.00, 51.20, 54.40, 57.60, 60.80, 64.00, 67.20, 70.40, 73.60, 76.80, 80])

GCENTERGRADIENT = np.loadtxt('../data/simData/grayScaleDerivative5by5Kernel.csv', delimiter=",")

GCENTERLAPLACIAN = np.loadtxt('../data/simData/grayScaleDerivative7by7Kernel.csv', delimiter=",")
