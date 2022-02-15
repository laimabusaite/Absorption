import matplotlib.pyplot as plt

from plotElliptic import *


if __name__ == '__main__':
    rabiList = [20] * 2
    polList = [0, 4]
    phaseList = [None, [100, -100]]
    alphaList = [None, [-40, 0]]

    rabi = 20

    pol_lin = 0
    filePathLinear = getFilePath(rabi, pol_lin)
    theorDataLinear = importData(filePathLinear)

    pol_ellipse = 4
    phase_ellipse = [100, -100]
    alpha_ellipse = [-40, 0]

    filePathEllipse = getFilePath(rabi, pol_ellipse, phase=phase_ellipse, alpha=alpha_ellipse)
    theorDataEllipse = importData(filePathEllipse)

    pol_circ = 1
    filePathCirc = getFilePath(rabi, pol_circ)
    theorDataCirc = importData(filePathCirc)

    plt.figure(1)
    plt.plot(theorDataLinear['B'], theorDataLinear['diff']/min(theorDataLinear['diff']), label='linear diff H - V')
    plt.plot(theorDataEllipse['B'], theorDataEllipse['diff']/min(theorDataEllipse['diff']), label= f'ellipse diff phase={phase_ellipse} alpha={alpha_ellipse}')
    plt.xlabel('Magnetic field, G')
    plt.ylabel('Absorption diff., arb. units')
    plt.xlim(0, 3000)
    plt.legend()
    plt.savefig('phase_comparison_figures/ellipse_lin_diff_norm.png', bbox_inches='tight')

    diffdiff = theorDataEllipse['diff'] - min(theorDataEllipse['diff'])*theorDataLinear['diff']/min(theorDataLinear['diff'])
    plt.figure(2)
    plt.plot(theorDataEllipse['B'], diffdiff, label=f'ellipse diff phase={phase_ellipse} alpha={alpha_ellipse} - linear diff')
    plt.plot(theorDataCirc['B'], theorDataCirc['diff'], label='circular diff')
    plt.xlabel('Magnetic field, G')
    plt.ylabel('Absorption diff., arb. units')
    # plt.xlim(0, 3000)
    plt.legend()

    plt.savefig('phase_comparison_figures/ellipse-lin_diff_full.png', bbox_inches='tight')

    plt.ylim(-5e-6, 5e-6)
    plt.savefig('phase_comparison_figures/ellipse-lin_diff_full_zoom1.png', bbox_inches='tight')

    plt.ylim(-3e-7, 3e-7)
    plt.savefig('phase_comparison_figures/ellipse-lin_diff_full_zoom2.png', bbox_inches='tight')

    plt.show()


