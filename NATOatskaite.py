from plotElliptic import *

def plotComponents(axs):
    rabiList = [20] * 3
    polList = [0, 1, 4]
    phaseList = [None, None, [100, -100]]
    alphaList = [None, None, [-40, 0]]

    for idx, rabi in enumerate(rabiList):
        pol = polList[idx]
        phase = phaseList[idx]
        alpha = alphaList[idx]
        filePath = getFilePath(rabi, pol, phase, alpha)
        theorData = importData(filePath)

        axs.plot(theorData['B'], theorData['comp1'])  # , label=label)
        if pol==0:
            axs.plot(theorData['B'], theorData['comp2'])


if __name__ == '__main__':
    fig3 = plt.figure(1, figsize=(3,2))
    axs3 = fig3.add_subplot(1, 1, 1)
    plotComponents(axs3)
    axs3.set_xlabel('Megnetic field, G')
    axs3.set_ylabel('Absorption, arb. units')

    plt.show()