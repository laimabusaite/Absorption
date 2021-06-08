import glob

import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

def import_database(filenames):
    # names = ['B', 'Total', 'comp1', 'comp2', 'diff']
    # theorData = pd.read_csv(filenames[0], header=None, delimiter=' ', names=names)
    phaseDatabase = pd.DataFrame(
        index=np.arange(-500, 510, 10),
        columns=[('alpha=-45', 'phase=90'), ('alpha=0', 'phase=90'), ('alpha=45', 'phase=90'),
                 ('alpha=-45', 'phase=80'), ('alpha=0', 'phase=80'), ('alpha=45', 'phase=80'),
                 ('alpha=-45', 'phase=100'), ('alpha=0', 'phase=100'), ('alpha=45', 'phase=100'),
                 ('alpha=-45', 'phase=-90'), ('alpha=0', 'phase=-90'), ('alpha=45', 'phase=-90'),
                 ('alpha=-45', 'phase=-80'), ('alpha=0', 'phase=-80'), ('alpha=45', 'phase=-80'),
                 ('alpha=-45', 'phase=-100'), ('alpha=0', 'phase=-100'), ('alpha=45', 'phase=-100')
                 ]
    )
    # print(phaseDatabase)
    for filename in filenames:
        # print(filename)
        split_filename = re.split('-alpha_|_|-phase_|.txt', filename)
        # print(split_filename)
        alpha1 = int(split_filename[1])
        alpha2 = int(split_filename[2])
        phase1 = int(split_filename[3])
        phase2 = int(split_filename[4])
        # print(f'alpha1={alpha1}; alpha2={alpha2}; phase1={phase1}; phase2={phase2}')
        names = ['B', 'Total', 'comp1', 'comp2', 'diff']
        theorData = pd.read_csv(filename, header=None, delimiter=' ', names=names, index_col='B')
        # print(theorData['comp1'])
        phaseDatabase[f'alpha={alpha1}', f'phase={phase1}'] = theorData['comp1']
        phaseDatabase[f'alpha={alpha2}', f'phase={phase2}'] = theorData['comp2']

    # print(phaseDatabase)

    return phaseDatabase

def calculate_difference(phaseDatabase, alpha = [0,0], phase=[90,-90]):
    diff = phaseDatabase[f'alpha={alpha[0]}', f'phase={phase[0]}'] - phaseDatabase[f'alpha={alpha[1]}', f'phase={phase[1]}']

    return diff

if __name__ == '__main__':


    filenames = sorted(glob.glob("*.txt"))
    print(filenames)

    phaseDatabase = import_database(filenames)

    print(phaseDatabase)

    alpha_list = [-45,0,45]
    phase1_list = [80, 90, 100]
    phase2_list = [-80, -90, -100]

    fig1 = plt.figure(1, figsize=(9,6))
    axs = []
    for i in range(9):
        axs.append(fig1.add_subplot(3, 3, i + 1))
    # plt.show()

    min_diff = 100
    max_diff = -100

    img_idx = 0
    for alpha1 in alpha_list:
        for alpha2 in alpha_list:
            print(img_idx)
            axs[img_idx].set_title(f'alpha=[{alpha1}, {alpha2}]')
            for phase1 in phase1_list:
                for phase2 in phase2_list:
                    alpha = [alpha1, alpha2]
                    phase = [phase1, phase2]
                    # print(f'alpha={alpha}, phase={phase}')
                    diff = calculate_difference(phaseDatabase, alpha = alpha, phase=phase)
                    if min_diff > min(diff):
                        min_diff = min(diff)
                    if max_diff < max(diff):
                        max_diff = max(diff)
                    axs[img_idx].plot(diff.index, diff, label=f'phase={phase}')
                    if img_idx == 4:
                        axs[img_idx].legend()
                    diff_0 = (diff==0).all()
                    if not diff_0:
                        print(f'alpha={alpha}, phase={phase}')
                        print(sum(diff))
            img_idx += 1
    fig1.tight_layout(pad=0., w_pad=0., h_pad=.0)
    fig1.savefig(f'rabi_0_all_combinations.png')
    # plt.tight_layout()
    # plt.legend()
    # plt.show()
    print(min_diff, max_diff)

    fig_list = []
    axs_list = []
    for idx_fig in range(9):
        fig = plt.figure(idx_fig+2, figsize=(9,6))
        fig_list.append(fig)
        axs = []
        for i in range(9):
            axs.append(fig.add_subplot(3, 3, i + 1))
        axs_list.append(axs)
        # print(axs_list)
    # plt.show()


    img_idx = 0
    for alpha1 in alpha_list:
        for alpha2 in alpha_list:
            print(img_idx)
            fig_list[img_idx].canvas.set_window_title(f'alpha_{alpha1}_{alpha2}')
            fig_list[img_idx].suptitle(f'alpha=[{alpha1}, {alpha2}]')
            axs_idx = 0
            for phase1 in phase1_list:
                for phase2 in phase2_list:
                    alpha = [alpha1, alpha2]
                    phase = [phase1, phase2]
                    # print(f'alpha={alpha}, phase={phase}')
                    axs_list[img_idx][axs_idx].set_title(f'phase={phase}')
                    diff = calculate_difference(phaseDatabase, alpha=alpha, phase=phase)
                    axs_list[img_idx][axs_idx].plot(diff.index, diff, label=f'phase={phase}', color=f'C{axs_idx}')
                    axs_list[img_idx][axs_idx].set_ylim(min_diff*1.1, max_diff*1.1)
                    # if axs_idx == 4:
                    #     axs_list[img_idx][axs_idx].legend()
                    diff_0 = (diff == 0).all()
                    if not diff_0:
                        print(f'alpha={alpha}, phase={phase}')
                        print(sum(diff))
                    axs_idx += 1
            fig_list[img_idx].tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
            fig_list[img_idx].savefig(f'rabi_0_alpha_{alpha1}_{alpha2}.png')
            img_idx += 1
    # plt.tight_layout()
    # plt.legend()
    plt.show()