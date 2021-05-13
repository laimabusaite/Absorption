import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def importData(filename):
    names = ['B', 'Total', 'comp1', 'comp2', 'diff']
    theorData = pd.read_csv(filename, header=None, delimiter=' ', names=names)
    if 'linear' in filename:
        theorData['diff'] *= -1
    theorData['circ'] = theorData['diff'] / theorData['Total']

    return theorData


def getFilePath(rabi, pol, phase=None, alpha = None):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'

    if pol == 0:
        folderName = 'Test_linear_polarization/linear'
    elif pol == 1:
        folderName = 'Circular'
    elif pol == 4:
        folderName = f'Test_circular_components/Absorption_theta=1.57-1.57_phi=0.00-0.00_pol=4--4_ph={phase[0]}-{phase[1]}_a={alpha[0]}-{alpha[1]}_gammaprobe=0.0190_lWidthpr=2.0'
    directory = os.path.relpath(folderName)
    theorPath = os.path.join(directory, fileName)

    return theorPath


def plotData(theorData, axs, label=None, nrows=2, ncols=2):
    # ax1 = fig.add_subplot(nrows, ncols, 1)
    axs[0].set_title('comp1')
    axs[0].plot(theorData['B'], theorData['comp1'])#, label=label)
    # ax1.legend()

    # ax2 = fig.add_subplot(nrows, ncols, 2)
    axs[1].set_title('comp2')
    axs[1].plot(theorData['B'], theorData['comp2'], label=label)
    axs[1].legend()

    # ax3 = fig.add_subplot(nrows, ncols, 3)
    axs[2].set_title('diff')
    axs[2].plot(theorData['B'], theorData['diff'])#, label=label)
    # ax3.legend()

    # ax4 = fig.add_subplot(nrows, ncols, 4)
    axs[3].set_title('circ')
    axs[3].plot(theorData['B'], theorData['circ'])#, label=label)
    # ax4.legend()


def plotRabiList(fig, axs, rabiList, pol, phase=None, alpha=None, title = None):
    if not title:
        if pol == 4:
            title = f'Rabi dependence\npol={pol}, phase={phase}, alpha={alpha}'
        else:
            title = f'Rabi dependence\npol={pol}'

    fig.canvas.set_window_title(title)
    plt.suptitle(f'{title}')

    for rabi in rabiList:
        filePath = getFilePath(rabi, pol, phase, alpha)
        theorData = importData(filePath)
        plotData(theorData, axs, label=f'pol={pol}, rabi={rabi}')


def plotPhaseList(fig, axs, phaseList, pol, rabi, alphaList, title=None):

    if not title:
        if pol == 4:
            title = f'Phase dependence\npol={pol}, rabi={rabi},\n alpha={alphaList}'
    fig.canvas.set_window_title(title.replace('\n', ''))
    plt.suptitle(f'{title}')

    for idx, phase in enumerate(phaseList):
        if len(np.array(alphaList).flatten()) > 2:
            alpha = alphaList[idx]
        else:
            alpha = np.array(alphaList).flatten()
        filePath = getFilePath(rabi, pol, phase, alpha)
        theorData = importData(filePath)
        plotData(theorData, axs, label=f'pol={pol}, phase={phase}, alpha={alpha}')





if __name__ == '__main__':
    alpha = [-40, 0]
    phase = [-100, 100]
    pol = 4
    rabi = 20
    rabiList = [1,20,50,100]
    phaseList = [[100, -100], [95, -95], [91, -91], [90, -90]]
    alphaList = [[-40, 0], [-40, 0], [-40, 0], [0, 0]]

    # phaseList = [[95, -95], [91, -91], [90, -90]]
    # alphaList = [[0, 0], [0, 0], [0, 0]]
    #
    # phaseList = [[-100, 100], [-95, 95], [-91, 91]]#, [90, -90]]
    # alphaList = [[-40, 0], [-40, 0], [-40, 0]]#, [0, 0]]

    fig1 = plt.figure(1)
    axs1 = []
    for i in range(4):
        axs1.append(fig1.add_subplot(2, 2, i+1))

    # filePath = getFilePath(rabi, pol, phase, alpha)
    # print(filePath)
    # theorData = importData(filePath)
    # print(theorData)
    # plotData(theorData, fig=fig)

    plotRabiList(fig1, axs1, rabiList[1:2], 0)
    # plt.show()
    # fig = plt.figure()
    fig2 = plt.figure(2)
    axs2 = []
    for i in range(4):
        axs2.append(fig2.add_subplot(2, 2, i + 1))
    plotRabiList(fig2, axs2, rabiList[1:2], 1)
    plotPhaseList(fig2, axs2, phaseList, pol, rabi, alphaList)
    # plotPhaseList(fig, phaseList, 1, rabi, alphaList)



    plt.show()

    # print(len(np.array(alpha).flatten()))