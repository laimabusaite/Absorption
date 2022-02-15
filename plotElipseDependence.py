import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from plotElliptic import importData, plotData, plotPhaseList


def getFilePath(rabi, phase, alpha):
    fileName = f'CsD1-43_D2-44-det25-rabi{rabi}-alpha_{alpha[0]}_{alpha[1]}-phase_{phase[0]}_{phase[1]}.txt'
    foldername0 = f'/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Circular_polarization_angle_phase/extracted_out_files'

    directory = os.path.relpath(foldername0)
    theorPath = os.path.join(directory, fileName)

    return theorPath


if __name__ == '__main__':

    pol = 4
    rabi = 20
    phaseList = [[90, -90], [90, -80], [90, -60], [90, -40], [90, -20], [90, 0]]
    alpha = [0, 0]

    fig1 = plt.figure(1)
    axs1 = []
    for i in range(4):
        axs1.append(fig1.add_subplot(2, 2, i + 1))

    fig11 = plt.figure(3)
    axs11 = fig11.add_subplot(1, 1, 1)

    for phase in phaseList:
        file_path = getFilePath(rabi, phase, alpha)
        print(file_path)
        theorData = importData(file_path)

        # title = f'Phase dependence\npol={pol}, rabi={rabi},\n alpha={alpha}'
        title = f'Phase dependence\n rabi={rabi}, alpha={alpha}'
        fig1.canvas.set_window_title(title.replace('\n', ''))
        fig1.suptitle(f'{title}')
        # label = f'pol={pol}, phase={phase}, alpha={alpha}'
        label = f'phase={phase}'

        plotData(theorData, axs1, label=label)

        axs11.plot(theorData['B'], theorData['diff'], label=label)
    axs11.set_title(title)
    axs11.set_xlabel('Magnetic field, G')
    axs11.set_ylabel('Absorption diff., arb. units')
    axs11.set_ylim(-1e-7, 1e-7)
    axs11.set_xlim(0, 3000)
    plt.legend()
    fig11.savefig('phase_comparison_figures/diff_phase_comparison.png', bbox_inches='tight')
    fig11.savefig('phase_comparison_figures/diff_phase_comparison.pdf', bbox_inches='tight')

    #################################################
    alphaList = [[0, 0], [0, -15], [0, -30], [0, -45]]
    phase = [60, -60]
    fig2 = plt.figure(2)
    axs2 = []
    for i in range(4):
        axs2.append(fig2.add_subplot(2, 2, i + 1))

    # plt.figure(4)
    # axs22 = fig22.add_subplot(1, 1, 1)
    # fig22, (axs21, axs22) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 4]})
    fig22, (axs22, axs21) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})

    axs_dummy = fig22.add_subplot(111, frameon=False)
    # hide tick and tick label of the big axis
    axs_dummy.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)

    for idx_alpha, alpha in enumerate(alphaList):
        print(alpha, phase)
        file_path = getFilePath(rabi, phase, alpha)
        print(file_path)
        theorData = importData(file_path)

        # title = f'Phase dependence\npol={pol}, rabi={rabi},\n phase={phase}'
        title = f'Alpha dependence\nrabi={rabi}, phase={phase}'
        fig2.canvas.set_window_title(title.replace('\n', ''))
        fig2.suptitle(f'{title}')

        # label = f'pol={pol}, phase={phase}, alpha={alpha}'
        label = f'alpha={alpha}'

        plotData(theorData, axs2, label=label)

        axs22.plot(theorData['B'], theorData['diff'], label=label)
        if idx_alpha == 0:
            axs21.plot(theorData['B'], theorData['diff'], label=label)

    axs22.set_title(title)
    # axs22.set_ylabel('Absorption diff., arb. units')
    # axs22.yaxis.set_label_coords(-0.15, .2)
    axs22.set_xlim(0, 3000)
    axs22.legend()
    axs21.legend()

    axs21.set_ylim(-1e-7, 1e-7)
    axs21.set_xlim(0, 3000)
    axs21.set_xlabel('Magnetic field, G')

    axs_dummy.set_ylabel('Absorption diff., arb. units')
    axs_dummy.yaxis.set_label_coords(-0.2, .5)
    # fig22.supylabel('Absorption diff., arb. units')
    fig22.tight_layout()




    fig22.savefig('phase_comparison_figures/diff_alpha_comparison_zoom.png', bbox_inches='tight')
    fig22.savefig('phase_comparison_figures/diff_alpha_comparison_zoom.pdf', bbox_inches='tight')

    plt.show()
