## Assume data directory is on the same path
## of the script

import os
import pandas as pd
import re
import parsing
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import dicom
import sphinx
import random


def gettingPairedMriContour(dsDir, pwd, iContourDir):
    """parse directories with MRI and Contour files

    :param dsDir: Dataset Directory
    :param pwd: presents work directory
    :param iContourDir: defined by author
    :returns: lists paired MRI and Contour files

    """
    ## set paths to dirs
    pathDataDir = os.path.join(cwd, dataDir)
    linker, contourDir, mriDir = os.listdir(pathDataDir)
    pathLinker = os.path.join(pathDataDir, linker)
    pathMriDir = os.path.join(pathDataDir, mriDir)
    pathContourDir = os.path.join(pathDataDir, contourDir)
    ## produces a list without the header after
    ## reading csv files with and without header
    df = pd.read_csv(pathLinker, sep=',')
    linksMriContour = df.values.tolist()
    ## produces a list with the paths of the
    ## paired dicom and contour files.
    pairedMriContour = []
    for link in linksMriContour:
        mriDirPatient = os.path.join(pathMriDir, link[0])
        mriImages = os.listdir(mriDirPatient)
        contourDirPatient = os.path.join(pathContourDir, link[1], contourSubDir)
        contourFiles = os.listdir(contourDirPatient)
        for file in mriImages:
            name, ext = os.path.splitext(file)
            fname = ".*(" + "{0:0>4}".format(name) + "-icontour).*"
            regex = re.compile(fname)
            res = [match.group(0) for f in contourFiles for match in [regex.search(f)] if match]
            if(len(res) > 0):
                tmpPathMri = os.path.join(mriDirPatient, file)
                tmpPathContour = os.path.join(contourDirPatient, res[0])
                pairedMriContour.append(tmpPathMri + "," + tmpPathContour)
    return pairedMriContour


def displayBlendMriMask(minRange, maxRange, pairedList):
    """display a blended image from a paired MRI and Mask file
       minRange < maxRange < len(pairedfile)

    :param minRange: int
    :param maxRange: int
    :param pairedList: list of paired MRI to Contourn file
    :returns: show imgs

    """
    if(minRange < maxRange and maxRange < len(pairedList)):
        for i in range(minRange, maxRange):
            pair = pairedList[i]
            pathImg, pathContour = pair.split(",")
            img = parsing.parse_dicom_file(pathImg)
            coordsContour = parsing.parse_contour_file(pathContour)
            height = img.shape[0]
            width = img.shape[1]
            imgMask = parsing.poly_to_mask(coordsContour, width, height)
            ## blend mri and mask files
            plt.figure(frameon=False)
            plt.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
            plt.imshow(imgMask, cmap=plt.cm.PuBu, alpha=.2, interpolation='nearest')
            plt.show()
    else:
        return None



def train():
    """Setting the inputs and labels for training

    :returns: void
    """
    global maskList
    ## make a shuffled list of the total input and labels
    maskList = list(range(len(pairs)))
    random.shuffle(maskList)
    for i in range(0, numBatchesPerEpoch):
        inputs, labels = getInputs(i)
        print(inputs.shape)
        print(labels.shape)
    del maskList[:]


def getInputs(batchNumber):
    """parse the dicom and contour files and place them in an array.

    :param batchNumber: 
    :returns: arrays of batch size for images & contours  
    """
    mriLst = []
    contourLst = []
    start = batchSize * batchNumber
    end = start + batchSize
    for i in range(start, end):
        print(maskList[i])
        pair = pairs[maskList[i]]
        pathImg, pathContour = pair.split(",")
        img = parsing.parse_dicom_file(pathImg)
        coordsContour = parsing.parse_contour_file(pathContour)
        height = img.shape[0]
        width = img.shape[1]
        imgMask = parsing.poly_to_mask(coordsContour, width, height)
        contourLst.append(imgMask.flatten())
        mriLst.append(img.flatten())
    mriArr = np.asarray(mriLst)
    contourArr = np.asarray(contourLst)
    return mriArr, contourArr


dataDir = "final_data"
contourSubDir = "i-contours"
cwd = os.getcwd()
pairs = gettingPairedMriContour(dataDir, contourSubDir, cwd)
displayBlendMriMask(90, 95, pairs)

numEpochs = 1
batchSize = 8
numBatchesPerEpoch = int((len(pairs))/batchSize)
maskList = []

for i in range(numEpochs):
    train()

#2412 96


