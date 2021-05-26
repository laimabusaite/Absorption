from plotD2excitationLinear import *

def getFilePathD2Angle(rabi, pol, theta, phi, phase=[100,-100], alpha = [-40,0]):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'


    folderName = f'Test_D2_excitation_circular_angle/theta={theta:.2f}-phi={phi:.2f}-pol={pol}/theta={theta:.2f}-{theta:.2f}_phi={phi:.2f}-{phi:.2f}_pol=1--1'

    directory = os.path.relpath(folderName)
    theorPath = os.path.join(directory, fileName)

    # theorPath = folderName + '/' + fileName

    return theorPath

def importAndCombineDataAngle(rabi, pol, theta, phi):


    filePath1 = getFilePathD2Angle(rabi, pol[0], theta[0], phi[0])
    filePath2 = getFilePathD2Angle(rabi, pol[1], theta[1], phi[1])



    theorData1 = importData(filePath1)
    theorData2 = importData(filePath2)

    compinedDataframe = combineTheorData(theorData1, theorData2)

    return compinedDataframe

if __name__ == '__main__':
    rabi = 0.1
    pol = [1, -1]
    theta = [1.66, 1.66]
    phi = [0.09, 0.09]

    filepath = getFilePathD2Angle(rabi=rabi, pol=pol[0], theta=theta[0], phi=phi[0])
    print(filepath)
    fln = 'Test_D2_excitation_circular_angle/Pump_4-4-theta=1.66-phi=0.09-pol=1-det=25_Probe_4-4-det=25/Absorption_theta=1.66-1.66_phi=0.09-0.09_pol=1--1_ph=100--100_a=-40-0_gammaprobe=0.0190_lWidthpr=2.0/Absorption_Cs133-D2-PumpRabi=0.10-shift=24.9-Ge=0'
    print(fln)
    print(filepath==fln)

    combinedDataframe = importAndCombineDataAngle(rabi=rabi, pol=pol, theta=theta, phi=phi)

    fig = plt.figure()
    axs = []
    for i in range(4):
        axs.append(fig.add_subplot(2, 2, i + 1))

    fig.suptitle(f'D2 excitation pol={pol}, theta={theta}, phi={phi}')
    rabi_list = [0.1, 1, 5, 20]
    for rabi in rabi_list:
        combinedDataframe = importAndCombineDataAngle(rabi=rabi, pol=pol, theta=theta, phi=phi)
        plotData(combinedDataframe, axs, label=f'D2 Rabi = {rabi} MHz')

    plt.show()