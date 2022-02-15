from plotElliptic import *


def getFilePathGamma(gamma, rabi, sigma=2, gammaprobe=0.0190):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
    folderName0 = '/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Absorption'
    folderName = f'Pump_D1-Cs133_Probe_D2-Cs133/gamma={gamma:.4f}-DSteps={int(150/2*sigma)}-DScan={sigma:.2f}sigma-lWidth=2.0/' \
                 f'Pump_4-3-theta=0.79-phi=1.57-pol=0-det=0_Probe_4-4-det=25/' \
                 f'Absorption_theta=1.57-1.57_phi=0.00-0.00_pol=1--1_gammaprobe={gammaprobe:.4f}_lWidthpr=2.0'

    theorPath = os.path.join(folderName0, folderName, fileName)
    return theorPath


def plotDiff(theorData, ax, label=None, title=None):
    if title:
        ax.set_title(title)
    ax.plot(theorData['B'],theorData['diff'], label=label)
    #
    ax.set_xlabel('Magnetic field, G')
    ax.set_ylabel('Abs. diff.')

def plotComp(theorData, ax, label=None, title=None):
    if title:
        ax.set_title(title)
    ax.plot(theorData['B'], theorData['comp1'], label=label)
    #
    ax.set_xlabel('Magnetic field, G')
    ax.set_ylabel('Absorption, arb. units')
    xmin = theorData.loc[0, 'B']
    xmax = theorData.iloc[-1]['B']
    ax.set_xlim(xmin, xmax)

if __name__ == '__main__':
    gamma = 0.019
    rabi = 1
    # sigma = 4
    # sigma = 2

    gamma_list = [gamma, gamma/10, gamma/100]
    sigma_list = [4, 4, 4] #[4, 2, 2]
    rabi_list = [20] #[1, 5, 20]
    gamma_probe_coef_list = [1]#, 2, 5, 10]

    # fig = plt.figure(figsize=(15,5))
    for idx_r, rabi in enumerate(rabi_list):
        fig = plt.figure(idx_r+1, figsize=(5,4))
        ax = fig.add_subplot(1, 1, 1+idx_r)
        for idx_g, gamma in enumerate(gamma_list):
            # ax = fig.add_subplot(1, 3, 1 + idx_g)
            sigma = sigma_list[idx_g]
            for probe_coef in gamma_probe_coef_list:
                gammaprobe = gamma * probe_coef

                filename = getFilePathGamma(gamma, rabi, sigma, gammaprobe)
                print(filename)

                theorData = importData(filename)
                theorData_crop = theorData[(theorData['B'] >= 1500) & (theorData['B'] <= 2500)]

                # print(theorData_crop)
                # plotDiff(theorData_crop, ax, label=f'gamma={gamma:.5f} MHz', title=f'Rabi={rabi} MHz')
                # # plotComp(theorData_crop, ax, label=f'gamma={gamma:.5f} MHz', title=f'Rabi={rabi} MHz')
                # ax.set_xlim(1500, 2500)

                # plotDiff(theorData, ax, label=rf'$\gamma$={gamma:.5f} MHz', title=f'Rabi={rabi} MHz')
                plotComp(theorData, ax, label=rf'$\gamma$={gamma:.5f} MHz', title=f'Rabi={rabi} MHz')
                # plotComp(theorData, ax, label=f'gamma={gamma:.5f} MHz gammaprobe={gammaprobe:.5f} MHz', title=f'gamma={gamma:.5f} MHz Rabi={rabi} MHz')

            plt.legend()
    plt.tight_layout()
    plt.savefig('gamma_comparison/gamma_comparison20.png', bbox_inches='tight')
    plt.savefig('gamma_comparison/gamma_comparison20.pdf', bbox_inches='tight')
    # plt.savefig('gamma_comparison/gamma_comparison_diff_full.png', bbox_inches='tight')
    plt.show()
