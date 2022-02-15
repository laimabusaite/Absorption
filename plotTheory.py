import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def plotRabiDependence(rabiList, folderName = '', title = None):
    rabiList = np.array(rabiList)

    if folderName:
        print(folderName)
        # directory = os.path.relpath(os.path.join('.', os.path.normpath(folderName)))
        directory = os.path.relpath(folderName)
    else:
        directory = os.path.relpath(os.path.normpath(folderName))



    fig = plt.figure()
    fig.canvas.set_window_title(folderName)
    # plt.suptitle(Bdirection)
    nrows = 2 #2
    ncols = 2 #len(pumpTransitionList) // 2
    # idx = 0

    names = ['B', 'Total', 'comp1', 'comp2', 'diff']
    # if 'linear' in folderName:
    #     names = ['B', 'Total', 'comp2', 'comp1', 'diff']

    # plt.subplot(nrows,ncols,idx+1)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(2, 2)
    if title:
        plt.suptitle(f'{title}')
    for rabi in rabiList:
        fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
        theorPath = os.path.join(directory, fileName)
        if not os.path.exists(theorPath):
            continue
        theorData = pd.read_csv(theorPath, header=None, delimiter=' ', names=names)
        if 'linear' in folderName:
            theorData['diff'] *= -1
        if 'Circular2' in folderName:
            theorData['diff'] = theorData['comp1'] - 0.95 * theorData['comp2']
            theorData['Total'] = theorData['comp1'] + 0.95 * theorData['comp2']
        theorData['circ'] = theorData['diff']/theorData['Total']
        print(theorData)

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

if __name__ == '__main__':
    rabiList = [1, 20, 50, 100]
    # transitionList = ['4-3']
    # probeList = ['4-4']
    # plotRabiDependence()

    folderName = 'Test_circular_components/ellipse1'
    # print(os.path.normpath(folderName))
    #
    # directory = os.path.join('.', os.path.normpath(folderName))
    # print(directory)
    title = 'Ellipse1 \n comp1: phase = -100 deg, alpha = 40 deg, \n comp2: phi=100 deg, alpha = 0 deg'

    # parameters = {'ellipse1': }

    plotRabiDependence(rabiList, folderName=folderName, title=title)
    plt.show()