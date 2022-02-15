import matplotlib.pyplot as plt

from plotD2excitationLinear import *


def getFilePathD2AnglePhase(rabi, pol, theta, phi, phase=[100, -100], alpha=[-40, 0]):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'

    # folderName = f'D2_range3000/theta={theta:.2f}-phi={phi:.2f}-pol={pol}/theta={theta:.2f}-{theta:.2f}_phi={phi:.2f}-{phi:.2f}_pol={pol}-{-pol}'
    folderName = f'/home/laima/Documents/Pētījumi/AOC Rb (2018-)/D2_range3000/Pump_D2-Cs133_Probe_D2-Cs133/gamma=0.0190-DSteps=150-DScan=2.00sigma-lWidth=2.0/Pump_4-4-theta={theta:.2f}-phi={phi:.2f}-pol={pol}-det=25_Probe_4-4-det=25/Absorption_theta={theta:.2f}-{theta:.2f}_phi={phi:.2f}-{phi:.2f}_pol={pol}-{-pol}_ph=90--90_a=0-0_gammaprobe=0.0190_lWidthpr=2.0'

    directory = os.path.relpath(folderName)
    theorPath = os.path.join(directory, fileName)

    # theorPath = folderName + '/' + fileName

    return theorPath


def importAndCombineDataAnglePhase(rabi, pol, theta, phi):
    filePath1 = getFilePathD2AnglePhase(rabi, pol[0], theta[0], phi[0])
    filePath2 = getFilePathD2AnglePhase(rabi, pol[1], theta[1], phi[1])

    theorData1 = importData(filePath1)
    theorData2 = importData(filePath2)

    compinedDataframe = combineTheorData(theorData1, theorData2)

    return compinedDataframe


if __name__ == '__main__':
    rabi = 0.1
    pol = [1, -1]
    theta = [1.57, 1.57]
    phi = [0.00, 0.00]

    filepath = getFilePathD2AnglePhase(rabi=rabi, pol=pol[0], theta=theta[0], phi=phi[0])
    print(filepath)

    combinedDataframe = importAndCombineDataAnglePhase(rabi=rabi, pol=pol, theta=theta, phi=phi)
    print(combinedDataframe)

    #####################################

    rabi_list = [0.1, 1, 10]

    fig = plt.figure(1)
    axs = []
    for i in range(4):
        axs.append(fig.add_subplot(2, 2, i + 1))
    fig.suptitle(f'D2 excitation pol={pol}, theta={theta}, phi={phi}')

    fig2 = plt.figure(2)
    ax2 = plt.gca()
    plt.title(f'D2 excitation pol={pol}, theta={theta}, phi={phi}')
    plt.xlabel('Magnetic field, G')
    plt.ylabel('Absorption intensity, arb. units')

    for rabi in rabi_list:
        combinedDataframe = importAndCombineDataAnglePhase(rabi=rabi, pol=pol, theta=theta, phi=phi)
        plotData(combinedDataframe, axs, label=f'D2 Rabi = {rabi} MHz')
        ax2.plot(combinedDataframe['B'], combinedDataframe['comp1'], label=f'D2 Rabi = {rabi} MHz')
        ax2.set_xlim(0, 3000)
        ax2.legend()

    fig2.tight_layout()
    fig2.savefig('/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Figures_AOC_Cs_20220112/comp1_D2_rabi.png')

    # fig = plt.figure(2)
    # axs = []
    # for i in range(4):
    #     axs.append(fig.add_subplot(2, 2, i + 1))
    #
    # fig.suptitle(f'D2 excitation rabi={rabi} MHz')
    # pol_list = [[1, 0], [1, 0], [-1, 0], [-1, 0]]
    # theta_list = [[1.57, 0.79], [1.57, 0.79], [1.57, 0.79], [1.57, 0.79]]
    # phi_list = [[0.00, 1.57], [0.00, -1.57], [0.00, 1.57], [0.00, -1.57]]
    # for idx, pol in enumerate(pol_list):
    #     theta=theta_list[idx]
    #     phi = phi_list[idx]
    #     print(pol, theta, phi)
    #     combinedDataframe = importAndCombineDataAnglePhase(rabi=rabi, pol=pol, theta=theta, phi=phi)
    #     plotData(combinedDataframe, axs, label=f'pol={pol}, theta={theta}, phi={phi}')
    plt.show()
