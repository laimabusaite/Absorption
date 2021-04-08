import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from plotElliptic import *

def getFilePathD2(rabi, pol, theta, phi, phase=None, alpha = None):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'

    if pol == 0:
        folderName = f'Test_D2_excitation_linear/Absorption_theta={theta[0]:.2f}-{theta[1]:.2f}_phi={phi[0]:.2f}-{phi[1]:.2f}_pol=0-0_ph=100--100_a=-40-0_gammaprobe=0.0190_lWidthpr=2.0'
    elif pol == 4:
        # folderName = f'Test_circular_components/Absorption_theta=1.57-1.57_phi=0.00-0.00_pol=4--4_ph={phase[0]}-{phase[1]}_a={alpha[0]}-{alpha[1]}_gammaprobe=0.0190_lWidthpr=2.0'
        folderName = f'Test_D2_excitation/Absorption_theta=1.57-1.57_phi=0.00-0.00_pol=4--4_ph={phase[0]}-{phase[1]}_a={alpha[0]}-{alpha[1]}_gammaprobe=0.0190_lWidthpr=2.0'
    directory = os.path.relpath(folderName)
    theorPath = os.path.join(directory, fileName)

    return theorPath

def combineTheorData(dataframe1, dataframe2):
    compinedDataframe = pd.DataFrame(dataframe1['B'])
    compinedDataframe['comp1'] = dataframe1['comp1']
    compinedDataframe['comp2'] = dataframe2['comp1']
    compinedDataframe['diff'] = compinedDataframe['comp1'] - compinedDataframe['comp2']
    compinedDataframe['circ'] = (compinedDataframe['comp1'] - compinedDataframe['comp2']) / (compinedDataframe['comp1'] + compinedDataframe['comp2'])
    compinedDataframe.dropna(inplace=True)
    return compinedDataframe


def importAndCombineData(rabi, pol, theta, phi, phase=None, alpha=None):

    if pol==0:
        filePath1 = getFilePathD2(rabi, pol, [theta[0], theta[1]], [phi[0], phi[1]])
        filePath2 = getFilePathD2(rabi, pol, [theta[1], theta[0]], [phi[1], phi[0]])

    elif pol==4:
        if phase[0] == 90:
            filePath1 = getFilePathD2(rabi, pol, [theta[0], theta[1]], [phi[0], phi[1]], [phase[0], phase[0]],
                                      [alpha[0], 0])
        else:
            filePath1 = getFilePathD2(rabi, pol, [theta[0], theta[1]], [phi[0], phi[1]], [phase[0], -phase[0]], [alpha[0], 0])
        if phase[1] == 90:
            filePath2 = getFilePathD2(rabi, pol, [theta[0], theta[1]], [phi[0], phi[1]], [phase[1], phase[1]],
                                      [alpha[1], 0])
        else:
            filePath2 = getFilePathD2(rabi, pol, [theta[0], theta[1]], [phi[0], phi[1]], [phase[1], -phase[1]],
                                  [alpha[1], 0])

    theorData1 = importData(filePath1)
    theorData2 = importData(filePath2)

    compinedDataframe = combineTheorData(theorData1, theorData2)

    return compinedDataframe

if __name__ == '__main__':

    rabi = 0.1
    pol = 0
    theta = [np.pi/2, 0]
    phi = [np.pi/2, 0]

    # filePath = getFilePathD2(0.1, 0, [0, np.pi/2], [0, np.pi/2])
    # print(filePath)
    #
    # theorDataD2Lin1 = importData(filePath)
    # print(theorDataD2Lin1)
    #
    # filePath = getFilePathD2(0.1, 0, [np.pi / 2, 0], [np.pi / 2, 0])
    # print(filePath)
    #
    # theorDataD2Lin2 = importData(filePath)
    # print(theorDataD2Lin2)
    #
    # compinedDataframe = combineTheorData(theorDataD2Lin1, theorDataD2Lin2)

    compinedDataframe = importAndCombineData(rabi, pol, theta, phi, phase=None, alpha=None)


    fig = plt.figure()

    plotData(compinedDataframe,fig)

    plt.show()

