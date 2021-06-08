from plotElliptic import *
from plotD2excitationLinear import *



def plotD2ellipticalList(axs, rabi, pol, theta, phi, phaseList, alphaList):
    plt.suptitle(f'Rabi = {rabi} MHz')
    for idx, phase in enumerate(phaseList):
        alpha = alphaList[idx]
        compinedDataframe = importAndCombineData(rabi, pol, theta, phi, phase=phase, alpha=alpha)
        plotData(compinedDataframe, axs=axs, label=f'pol={pol}, phase={phase}, alpha={alpha}')

def plotD2ellipticalRabiList(axs, rabiList, pol, theta, phi, phase, alpha):
    plt.suptitle(f'pol={pol}, phase={phase}, alpha={alpha}')
    for idx, rabi in enumerate(rabiList):
        # alpha = alphaList[idx]
        compinedDataframe = importAndCombineData(rabi, pol, theta, phi, phase=phase, alpha=alpha)
        plotData(compinedDataframe, axs=axs, label=f'Rabi = {rabi} MHz')
        # print(compinedDataframe)



if __name__ == '__main__':

    rabi = 0.1
    pol = 4
    theta = [np.pi/2, np.pi/2]
    phi = [0, 0]
    phase = [90, -90]
    alpha = [0, 0]

    # phaseList = np.array([[90, -90],
    #                       [100, -100],
    #                       [100, -100],
    #                       [-100, 100],
    #                       [100, -100]
    #                       ])
    # alphaList = np.array([[0, 0],
    #                       [0, 0],
    #                       [-40, 0],
    #                       [-40, 0],
    #                       [-40, -40]
    #                       ])

    phaseList = np.array([
                          [100, -100],
                          [100, -100],
                          [100, -100]
                          ])
    alphaList = np.array([
                          [0, 0],
                          [-40, 0],
                          [-40, -40]
                          ])

    # compinedDataframe = importAndCombineData(rabi, pol, theta, phi, phase=phase, alpha=alpha)

    fig = plt.figure()
    axs = []
    for i in range(4):
        axs.append(fig.add_subplot(2, 2, i + 1))

    # plotData(compinedDataframe, fig)

    # plotD2ellipticalList(axs, rabi, pol, theta, phi, phaseList, alphaList)

    rabiList = [0.1, 0.5, 1, 5]
    plotD2ellipticalRabiList(axs, rabiList, pol, theta, phi, phase, alpha)

    plt.show()


