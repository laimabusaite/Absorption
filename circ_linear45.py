import matplotlib.pyplot as plt
import pandas as pd

from plotTheory import plotRabiDependence
import os

def importTheordata(folderName, rabi):
    directory = os.path.relpath(folderName)

    names = ['B', 'Total', 'comp1', 'comp2', 'diff']
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
    theorPath = os.path.join(directory, fileName)
    theorData1 = pd.read_csv(theorPath, header=None, delimiter=' ', names=names)

    return theorData1

if __name__ == "__main__":

    rabi = 20

    titleList = [
        'Linear 45 \n comp1: pol = 0, theta = 45 deg, phi = 90 deg, \n comp2: pol = 0, theta = 45 deg, phi = -90 deg',
        'Circular \n comp1: pol = 1, theta = 90 deg, phi = 0 deg, \n comp2: pol = -1, theta = 90 deg, phi = 0 deg',
    ]

    title_dict_45 = {
        'comp1': 'Linear 45, pol = 0, theta = 45 deg, phi = 90 deg',
        'comp2': 'Linear 45, pol = 0, theta = 45 deg, phi = -90 deg'
    }

    title_dict_circ = {
        'comp1': 'Circular, pol = 1, theta = 90 deg, phi = 0 deg',
        'comp2': 'Circular, pol = -1, theta = 90 deg, phi = 0 deg'
    }

    folderName_lin45 = 'Test_linear_polarization/linear_45'
    theorData_lin45 = importTheordata(folderName_lin45, rabi)

    folderName_circ = 'Circular'
    theorData_circ = importTheordata(folderName_circ, rabi)

    # theorData = pd.DataFrame(theorData_circ['B'])
    # print(theorData)


    comp_list = ['comp1', 'comp2']

    for idx_circ, comp_circ in enumerate(comp_list):
        for idx_lin, comp_lin in enumerate(comp_list):


            title1 = title_dict_circ[comp_circ]
            title2 = title_dict_45[comp_lin]
            title = f'comp1: {title1}\n comp2: {title2}\n'

            theorData = pd.DataFrame(theorData_circ['B'])
            theorData['comp1'] = theorData_circ[comp_circ]
            theorData['comp2'] = theorData_lin45[comp_lin]
            theorData['diff'] = theorData['comp1'] - theorData['comp2']
            theorData['Total'] = theorData['comp1'] + theorData['comp2']
            theorData['circ'] = theorData['diff'] / theorData['Total']

            # comp1 = theorData_circ[comp_circ]
            # comp2 = theorData_lin45[comp_lin]
            # diff = comp1 - comp2
            # total = comp1 + comp2
            # circularity = diff/total

            fig = plt.figure()
            fig.canvas.set_window_title(f'circ{idx_circ + 1}_linear{idx_lin + 1}')
            plt.title(title)

            nrows = 2  # 2
            ncols = 2  # len(pumpTransitionList) // 2

            ax1 = fig.add_subplot(nrows, ncols, 1)
            ax1.set_title('comp1')
            ax1.plot(theorData['B'], theorData['comp1'], label=rabi)
            ax1.legend()

            ax2 = fig.add_subplot(nrows, ncols, 2)
            ax2.set_title('comp2')
            ax2.plot(theorData['B'], theorData['comp2'], label=rabi)
            ax2.legend()

            ax3 = fig.add_subplot(nrows, ncols, 3)
            ax3.set_title('diff')
            ax3.plot(theorData['B'], theorData['diff'], label=rabi)
            ax3.legend()

            ax4 = fig.add_subplot(nrows, ncols, 4)
            ax4.set_title('circ')
            ax4.plot(theorData['B'], theorData['circ'], label=rabi)
            ax4.legend()

    fig1 = plt.figure(figsize=(16,5))
    fig1.canvas.set_window_title(f'circdiff_lineardiff')
    plt.suptitle('Diff circ - diff linear 45\n')
    ax1 = fig1.add_subplot(1, 3, 1)
    ax1.set_title('Diff circ')
    ax1.plot(theorData_circ['B'], theorData_circ['diff'], label=rabi)
    ax1.legend()
    ax2 = fig1.add_subplot(1, 3, 2)
    ax2.set_title('Diff linear 45')
    ax2.plot(theorData_circ['B'], theorData_lin45['diff'], label=rabi)
    ax2.legend()
    ax3 = fig1.add_subplot(1, 3, 3)
    ax3.set_title('Diff diff')
    ax3.plot(theorData_circ['B'], theorData_circ['diff'] - theorData_lin45['diff'], label=rabi)
    ax3.legend()
    plt.tight_layout()

    plt.show()