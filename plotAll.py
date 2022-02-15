import matplotlib.pyplot as plt
import pandas as pd

from plotTheory import plotRabiDependence
import os

if __name__ == "__main__":
    rabiList = [0, 1, 5, 20, 50, 100]

    folderNameList = [
        # 'Test_circular_components/ellipse1',
        # 'Test_circular_components/ellipse2',
        'Test_linear_polarization/linear',
        'Test_linear_polarization/linear_45',
        '/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Absorption_linear/Pump_D1-Cs133_Probe_D2-Cs133/gamma=0.0019-DSteps=150-DScan=2.00sigma-lWidth=2.0/Pump_4-3-theta=0.79-phi=1.57-pol=0-det=0_Probe_4-4-det=25/Absorption_theta=0.00-1.57_phi=0.00-1.57_pol=0-0_gammaprobe=0.0190_lWidthpr=2.0',
        '/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Absorption_linear/Pump_D1-Cs133_Probe_D2-Cs133/gamma=0.0002-DSteps=150-DScan=2.00sigma-lWidth=2.0/Pump_4-3-theta=0.79-phi=1.57-pol=0-det=0_Probe_4-4-det=25/Absorption_theta=0.00-1.57_phi=0.00-1.57_pol=0-0_gammaprobe=0.0190_lWidthpr=2.0',
        'Circular',
    ]

    titleList = [
        # 'Ellipse1 \n theta = 90 deg, phi = 0 deg \n comp1: phase = -100 deg, alpha = -40 deg, \n comp2: phase=100 deg, alpha = 0 deg',
        # 'Ellipse2 \n theta = 90 deg, phi = 0 deg \n comp1: phase = 100 deg, alpha = -40 deg, \n comp2: phase=-100 deg, alpha = 0 deg',
        'Linear gamma=0.019 \n comp1: pol = 0, theta = 0 deg, phi = 0 deg (z-dir), \n comp2: pol = 0, theta = 90 deg, phi = 90 deg (y-dir)',
        'Linear 45 \n comp1: pol = 0, theta = 45 deg, phi = 90 deg, \n comp2: pol = 0, theta = 45 deg, phi = -90 deg',
        'Linear gamma=0.0019 \n comp1: pol = 0, theta = 0 deg, phi = 0 deg (z-dir), \n comp2: pol = 0, theta = 90 deg, phi = 90 deg (y-dir)',
        'Linear gamma=0.00019 \n comp1: pol = 0, theta = 0 deg, phi = 0 deg (z-dir), \n comp2: pol = 0, theta = 90 deg, phi = 90 deg (y-dir)',
        'Circular \n comp1: pol = 1, theta = 90 deg, phi = 0 deg, \n comp2: pol = -1, theta = 90 deg, phi = 0 deg',
        # 'Circular2 comp1 - 0.95 comp2 \n comp1: pol = 1, theta = 90 deg, phi = 0 deg, \n comp2: pol = -1, theta = 90 deg, phi = 0 deg'
    ]

    names = ['B', 'Total', 'comp1', 'comp2', 'diff']

    # fig = plt.figure()
    for idx, folderName in enumerate(folderNameList[:4]):
        title = titleList[idx]

        directory = os.path.relpath(folderName)
        fig = plt.figure()
        fig.canvas.set_window_title(folderName)
        plt.title('Rabi=pump - Rabi=0 ' + title)
        rabi = 0
        fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
        theorPath = os.path.join(directory, fileName)
        theorData1 = pd.read_csv(theorPath, header=None, delimiter=' ', names=names)

        for rabi in rabiList[1:]:
            fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
            theorPath = os.path.join(directory, fileName)
            if not os.path.exists(theorPath):
                continue
            theorData = pd.read_csv(theorPath, header=None, delimiter=' ', names=names)
            theorData['diff_on_1'] = theorData1['diff'] - theorData['diff']
            plt.plot(theorData['B'], theorData['diff_on_1'], label = rabi)
        # plotRabiDependence(rabiList, folderName=folderName, title=title)
    plt.legend()

    for idx, folderName in enumerate(folderNameList[:]):
        title = titleList[idx]

        # directory = os.path.relpath(folderName)
        # fig = plt.figure()
        # fig.canvas.set_window_title(folderName)
        # rabi = 1
        # fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
        # theorPath = os.path.join(directory, fileName)
        # theorData1 = pd.read_csv(theorPath, header=None, delimiter=' ', names=names)
        #
        # for rabi in rabiList[1:]:
        #     fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'
        #     theorPath = os.path.join(directory, fileName)
        #     theorData = pd.read_csv(theorPath, header=None, delimiter=' ', names=names)
        #     theorData['diff_on_1'] = theorData1['diff'] - theorData['diff']
        #     plt.plot(theorData['B'], theorData['diff_on_1'], label = rabi)
        plotRabiDependence(rabiList[:], folderName=folderName, title=title)
    plt.legend()


    plt.show()

