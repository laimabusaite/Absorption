import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from plotElliptic import importData, plotData
from CombinedDataElipses import getFilePath_full_phase

if __name__ == '__main__':
    rabi = 20

    alpha = [0, -45]

    phase1 = 90
    phase2_list = [-90, -89, -88, -87, -86, -85, -80, -70, -60, -50, -40, -20, 0]
    phaseList = [[phase1, phase2] for phase2 in phase2_list]

    fig1 = plt.figure(1)
    axs1 = []
    for i in range(4):
        axs1.append(fig1.add_subplot(2, 2, i + 1))

    # fig11 = plt.figure(3)
    # axs11 = fig11.add_subplot(1, 1, 1)
    fig11, (axs11, axs12) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})

    axs_dummy = fig11.add_subplot(111, frameon=False)
    # hide tick and tick label of the big axis
    axs_dummy.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)

    for idx_phase, phase in enumerate(phaseList):
        file_path = getFilePath_full_phase(rabi, phase, alpha)
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

        if idx_phase == 0:
            axs12.plot(theorData['B'], theorData['diff'], label=label)

    axs11.set_title(title)
    # axs11.set_xlabel('Magnetic field, G')
    # axs11.set_ylabel('Absorption diff., arb. units')
    # axs11.set_ylim(-1e-7, 1e-7)
    axs11.set_xlim(0, 3000)
    axs11.legend()
    axs12.legend()

    axs12.set_ylim(-1e-7, 1e-7)
    axs12.set_xlim(0, 3000)
    axs12.set_xlabel('Magnetic field, G')

    axs_dummy.set_ylabel('Absorption diff., arb. units')
    axs_dummy.yaxis.set_label_coords(-0.2, .5)
    # fig22.supylabel('Absorption diff., arb. units')
    fig11.tight_layout()

    # fig11.savefig('phase_comparison_figures/diff_phase_comparison_vert_85_zoom.png', bbox_inches='tight')
    # fig11.savefig('phase_comparison_figures/diff_phase_comparison_vert_85_zoom.pdf', bbox_inches='tight')
    plt.show()