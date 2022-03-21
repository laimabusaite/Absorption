
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from plotElliptic import importData, plotData, plotPhaseList

def getAbsorptionFilePath(rabi):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
    foldername0 = f'/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Absorption/Pump_D1-Cs133_Probe_D2-Cs133/gamma=0.0190-DSteps=300-DScan=4.00sigma-lWidth=2.0/Pump_4-3-theta=0.79-phi=1.57-pol=0-det=0_Probe_4-4-det=25/Absorption_theta=1.57-1.57_phi=0.00-0.00_pol=1--1_gammaprobe=0.0190_lWidthpr=2.0'

    directory = os.path.relpath(foldername0)
    theorPath = os.path.join(directory, fileName)

    return theorPath


if __name__ == '__main__':

    rabi = 100

    theor_path = getAbsorptionFilePath(rabi)
    print(theor_path)

    theorData = importData(theor_path)

    fig = plt.figure()
    # fig.canvas.set_window_title(folderName)
    # plt.suptitle(Bdirection)
    nrows = 2  # 2
    ncols = 2  # len(pumpTransitionList) // 2

    ax1 = fig.add_subplot(nrows, ncols, 1)
    ax1.set_title('comp1')
    ax1.plot(theorData['B'], theorData['comp1'], label=f'Rabi={rabi} MHz')
    ax1.set_xlabel('Magnetic field, G')
    ax1.set_ylabel('Absorption intensity, arb. units')
    ax1.legend()

    ax2 = fig.add_subplot(nrows, ncols, 2)
    ax2.set_title('comp2')
    ax2.plot(theorData['B'], theorData['comp2'], label=f'Rabi={rabi} MHz')
    ax2.set_xlabel('Magnetic field, G')
    ax2.set_ylabel('Absorption intensity, arb. units')
    ax2.legend()

    ax3 = fig.add_subplot(nrows, ncols, 3)
    ax3.set_title('diff')
    ax3.plot(theorData['B'], theorData['diff'], label=f'Rabi={rabi} MHz')
    ax3.set_xlabel('Magnetic field, G')
    ax3.set_ylabel('Absorption difference, arb. units')
    ax3.legend()

    ax4 = fig.add_subplot(nrows, ncols, 4)
    ax4.set_title('circ')
    ax4.plot(theorData['B'], theorData['circ'], label=f'Rabi={rabi} MHz')
    ax4.set_xlabel('Magnetic field, G')
    ax4.legend()

    plt.show()

