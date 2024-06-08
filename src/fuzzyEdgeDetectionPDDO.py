import constants
import numpy as np
from scipy import signal


class fuzzyEdgeDetectionPDDO:
    def __init__(self, image, pathToMembershipFunction):
        self.image = image
        self.pathToMembershipFunction = pathToMembershipFunction
        self.Nx = constants.NX
        self.Ny = constants.NY
        self.horizonGradient = constants.HORIZONGRADIENT
        self.horizonLaplacian = constants.HORIZONLAPLACIAN
        self.kernelGradient = constants.PDDOGRADIENTKERNEL
        self.kernelLaplacian = constants.PDDOLAPLACIANKERNEL
        self.gMaskGradient = constants.GMASKGRADIENT
        self.gMaskLaplacian = constants.GMASKLAPLACIAN
        self.gCenterGradient = constants.GCENTERGRADIENT
        self.gCenterLaplacian = constants.GCENTERLAPLACIAN
        self.kerneldimGradient = constants.KERNELDIMGRADIENT
        self.kerneldimLaplacian = constants.KERNELDIMLAPLACIAN


    def loadMembershipFunction(self):
        self.membershipFunction = np.loadtxt(self.pathToMembershipFunction, delimiter=",")

    def addBoundary(self, horizon):
        self.extendedImage = np.pad(self.image,int(horizon),mode='symmetric')
        self.extendedNx = self.Nx + 2*int(horizon)
        self.extendedNy = self.Ny + 2*int(horizon)

    def assignMembership(self):
        pixelMemberships = []
        for iCol in range(self.extendedNx):
            for iRow in range(self.extendedNy):
                currentPixelMembership = []
                currentPixelMembership.append(self.extendedImage[iCol,iRow])
                membershipIndex = int(self.extendedImage[iCol,iRow])
                currentPixelMembership.append(list(self.membershipFunction[membershipIndex])[0])
                currentPixelMembership.append(list(self.membershipFunction[membershipIndex])[1])
                pixelMemberships.append(currentPixelMembership)
        self.pixelMemberships = pixelMemberships

    def createFuzzyMembershipImage(self):
        fuzzyMembershipImage = []
        for iPixel in range(self.extendedNx*self.extendedNy):
            fuzzyMembershipImage.append(self.pixelMemberships[iPixel][1])
        self.fuzzyMembershipImage = np.array(fuzzyMembershipImage).reshape((self.extendedNx,self.extendedNy))

    def findFuzzyDerivativeRule(self, horizon, kernel):
        D = []
        for iCol in range(int(horizon),self.extendedNx-int(horizon)):
            for iRow in range(int(horizon),self.extendedNy-int(horizon)):
                D.append(np.sum(np.multiply(kernel, self.fuzzyMembershipImage[iRow-int(horizon):iRow+int(horizon)+1,iCol-int(horizon):iCol+int(horizon)+1]).flatten()).astype(int))
        D = np.array(D)
        while np.max(np.absolute(D))>255:
            D = np.divide(D,2)
        self.D = np.pad(D.reshape((self.extendedNx-int(2*horizon),self.extendedNy-int(2*horizon))),int(horizon),mode='symmetric')

    def calculateFuzzyPDDODerivative(self, horizon, mask, kerneldim):
        derivative = []
        for iCol in range(int(horizon),self.extendedNx-int(horizon)):
            for iRow in range(int(horizon),self.extendedNy-int(horizon)):
                D = np.multiply(mask,self.D[iRow-int(horizon):iRow+int(horizon)+1,iCol-int(horizon):iCol+int(horizon)+1]).astype(int).flatten()
                L = np.multiply(mask,self.extendedImage[iRow-int(horizon):iRow+int(horizon)+1,iCol-int(horizon):iCol+int(horizon)+1]).astype(int).flatten()
                muPrem = np.sum(self.membershipFunction[L,1])
                gCents = []
                for iD in D:
                    gCents.append(self.gCenter[np.abs(self.gCenter-iD).argmin()])
                    #gCents.append(iD)
                gCents = np.array(gCents).reshape((kerneldim,kerneldim))
                derivative.append(np.sum(np.multiply(mask,(np.multiply(gCents, self.membershipFunction[L,1].reshape((kerneldim,kerneldim))))/muPrem).flatten()))
        while np.max(np.absolute(derivative))>255:
            derivative = np.divide(derivative,2)
        return np.array(derivative).reshape((self.Nx,self.Ny))
    
    def calculatePDDOGradient(self):
        self.gradientPDDO = signal.convolve2d(self.image, self.kernelGradient, boundary='symm', mode='same')

    def calculatePDDOLaplacian(self):
        self.laplacianPDDO = signal.convolve2d(self.image, self.kernelLaplacian, boundary='symm', mode='same')

    def solve(self):
        self.loadMembershipFunction()
        #Calculate fuzzyPDDOGradient
        self.addBoundary(self.horizonGradient)
        self.assignMembership()
        self.createFuzzyMembershipImage()
        self.findFuzzyDerivativeRule(self.horizonGradient, self.kernelGradient)
        DGradient = self.D
        self.gCenter = self.gCenterGradient
        fuzzyPDDOGradient = self.calculateFuzzyPDDODerivative(self.horizonGradient, self.gMaskGradient, self.kerneldimGradient)
        
        #Calculate fuzzyPDDOLaplacian
        self.addBoundary(self.horizonLaplacian)
        self.assignMembership()
        self.createFuzzyMembershipImage()
        self.findFuzzyDerivativeRule(self.horizonLaplacian, self.kernelLaplacian)
        DLaplacian = self.D
        self.gCenter = self.gCenterLaplacian
        fuzzyPDDOLaplacian = self.calculateFuzzyPDDODerivative(self.horizonLaplacian, self.gMaskLaplacian, self.kerneldimLaplacian)

        self.calculatePDDOGradient()
        self.calculatePDDOLaplacian()
        np.savetxt('../data/output/fuzzyPDDOGradient2.csv',  fuzzyPDDOGradient, delimiter=",")
        np.savetxt('../data/output/fuzzyPDDOLaplacian2.csv',  fuzzyPDDOLaplacian, delimiter=",")
        np.savetxt('../data/output/gradientPDDO.csv',  self.gradientPDDO, delimiter=",")
        np.savetxt('../data/output/laplacianPDDO.csv',  self.laplacianPDDO, delimiter=",")
        np.savetxt('../data/output/DGradient.csv2',  DGradient, delimiter=",")
        np.savetxt('../data/output/DLaplacian.csv2',  DLaplacian, delimiter=",")
        print('Here')
        a = input('').split(" ")[0]

