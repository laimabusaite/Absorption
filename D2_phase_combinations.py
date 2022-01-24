from plotD2excitationLinear import *


def getFilePathD2Phase(rabi, pol, theta, phi, phase=90, alpha = 0):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'


    # folderName = f'D2_range3000/theta={theta:.2f}-phi={phi:.2f}-pol={pol}/theta={theta:.2f}-{theta:.2f}_phi={phi:.2f}-{phi:.2f}_pol={pol}-{-pol}'
    folderName = f'D2_phase/Absorption_theta={theta:.2f}-{theta:.2f}_phi={phi:.2f}-{phi:.2f}_pol={pol}-{-pol}_ph={phase}-{abs(phase)}_a={alpha}-0_gammaprobe=0.0190_lWidthpr=2.0'
    directory = os.path.relpath(folderName)
    theorPath = os.path.join(directory, fileName)

    # theorPath = folderName + '/' + fileName

    return theorPath

if __name__ == '__main__':
    rabi = 0.1
    pol = [4, 4]
    theta = [1.57, 1.57]
    phi = [0.00, 0.00]
    rabiList = [0.1,1,5]


    phase = [90, -100]
    alpha = [0, 0]

    fig = plt.figure(1)
    axs = []
    for i in range(4):
        axs.append(fig.add_subplot(2, 2, i + 1))

    fig.suptitle(f'D2 excitation phase={phase}, alpha={alpha}')
    for rabi in rabiList:
        filepath1 = getFilePathD2Phase(rabi=rabi, pol=pol[0], theta=theta[0], phi=phi[0], phase=phase[0],
                                       alpha=alpha[0])
        print(filepath1)
        filepath2 = getFilePathD2Phase(rabi=rabi, pol=pol[1], theta=theta[1], phi=phi[1], phase=phase[1],
                                       alpha=alpha[1])
        print(filepath1)

        names = ['B', 'Total', 'comp1', 'comp2', 'diff']
        theorData1 = pd.read_csv(filepath1, header=None, delimiter=' ', names=names)
        theorData2 = pd.read_csv(filepath2, header=None, delimiter=' ', names=names)

        combinedDataframe = combineTheorData(theorData1, theorData2)
        plotData(combinedDataframe, axs, label=f'D2 Rabi = {rabi} MHz')
    #
    # phase = [100, -80]
    # alpha = [45, -45]
    #
    # fig = plt.figure(2)
    # axs = []
    # for i in range(4):
    #     axs.append(fig.add_subplot(2, 2, i + 1))
    #
    # fig.suptitle(f'D2 excitation phase={phase}, alpha={alpha}')
    # for rabi in rabiList:
    #     filepath1 = getFilePathD2Phase(rabi=rabi, pol=pol[0], theta=theta[0], phi=phi[0], phase=phase[0],
    #                                    alpha=alpha[0])
    #     print(filepath1)
    #     filepath2 = getFilePathD2Phase(rabi=rabi, pol=pol[1], theta=theta[1], phi=phi[1], phase=phase[1],
    #                                    alpha=alpha[1])
    #     print(filepath1)
    #
    #     names = ['B', 'Total', 'comp1', 'comp2', 'diff']
    #     theorData1 = pd.read_csv(filepath1, header=None, delimiter=' ', names=names)
    #     theorData2 = pd.read_csv(filepath2, header=None, delimiter=' ', names=names)
    #
    #     combinedDataframe = combineTheorData(theorData1, theorData2)
    #     plotData(combinedDataframe, axs, label=f'D2 Rabi = {rabi} MHz')
    plt.show()