import constants
import numpy as np

class fuzzyEdgeDetectionPDDO:
    def __init__(self, image, pathToMembershipFunction):
        self.image = image
        self.pathToMembershipFunction = pathToMembershipFunction
        self.Nx = constants.NX
        self.Ny = constants.NY
        self.horizon = constants.HORIZON
        self.gradientKernel = constants.PDDOGradientKernel
        self.gMask = constants.GMASK
        self.gCenter = constants.GCENTER
        self.kerneldim = constants.KERNELDIM

    def loadMembershipFunction(self):
        self.membershipFunction = np.loadtxt(self.pathToMembershipFunction, delimiter=",")

    def addBoundary(self):
        self.image = np.pad(self.image,int(self.horizon),mode='symmetric')
        self.Nx = self.Nx + 2*int(self.horizon)
        self.Ny = self.Ny + 2*int(self.horizon)

    def assignMembership(self):
        pixelMemberships = []
        for iCol in range(self.Nx):
            for iRow in range(self.Ny):
                currentPixelMembership = []
                currentPixelMembership.append(self.image[iCol,iRow])
                membershipIndex = int(self.image[iCol,iRow])
                currentPixelMembership.append(list(self.membershipFunction[membershipIndex])[0])
                currentPixelMembership.append(list(self.membershipFunction[membershipIndex])[1])
                pixelMemberships.append(currentPixelMembership)
        self.pixelMemberships = pixelMemberships

    def createFuzzyMembershipImage(self):
        fuzzyMembershipImage = []
        for iPixel in range(self.Nx*self.Ny):
            fuzzyMembershipImage.append(self.pixelMemberships[iPixel][1])
        self.fuzzyMembershipImage = np.array(fuzzyMembershipImage).reshape((self.Nx,self.Ny))

    def findFuzzyDerivativeRule(self):
        D = []
        for iCol in range(int(self.horizon),self.Nx-int(self.horizon)):
            for iRow in range(int(self.horizon),self.Ny-int(self.horizon)):
                D.append(np.sum(np.multiply(self.gradientKernel, self.fuzzyMembershipImage[iRow-int(self.horizon):iRow+int(self.horizon)+1,iCol-int(self.horizon):iCol+int(self.horizon)+1]).flatten()).astype(int))
        D = np.array(D)
        while np.max(np.absolute(D))>255:
            D = np.divide(D,2)
        self.D = np.pad(D.reshape((self.Nx-int(2*self.horizon),self.Ny-int(2*self.horizon))),int(self.horizon),mode='symmetric')

    def calculateGradient(self):
        gradient = []
        for iCol in range(int(self.horizon),self.Nx-int(self.horizon)):
            for iRow in range(int(self.horizon),self.Ny-int(self.horizon)):
                D = np.multiply(self.gMask,self.D[iRow-int(self.horizon):iRow+int(self.horizon)+1,iCol-int(self.horizon):iCol+int(self.horizon)+1]).astype(int).flatten()
                L = np.multiply(self.gMask,self.image[iRow-int(self.horizon):iRow+int(self.horizon)+1,iCol-int(self.horizon):iCol+int(self.horizon)+1]).astype(int).flatten()
                muPrem = np.sum(self.membershipFunction[L,1])
                gCents = []
                for iD in D:
                    gCents.append(self.gCenter[np.abs(self.gCenter-iD).argmin()])
                gCents = np.array(gCents).reshape((self.kerneldim,self.kerneldim))
                gradient.append(np.sum(np.multiply(self.gMask,(np.multiply(gCents, self.membershipFunction[L,1].reshape((self.kerneldim,self.kerneldim))))/muPrem).flatten()))
        while np.max(np.absolute(gradient))>255:
            gradient = np.divide(gradient,2)
        self.gradient = np.array(gradient)
    
    def solve(self):
        self.loadMembershipFunction()
        self.addBoundary()
        self.assignMembership()
        self.createFuzzyMembershipImage()
        self.findFuzzyDerivativeRule()
        self.calculateGradient()
        np.savetxt('../data/output/gradient.csv',  self.gradient, delimiter=",")
        print('Here')
        a = input('').split(" ")[0]

