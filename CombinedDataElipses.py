import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from plotElliptic import importData


def getFilePath_full_phase(rabi, phase, alpha):
    fileName = f'Absorption_Cs133-D2-PumpRabi={rabi:.2f}-shift=24.9-Ge=0'

    foldername0 = f'/home/laima/Documents/Pētījumi/AOC Rb (2018-)/' \
                  f'Circular_polarization_angle_phase/Pump_D1-Cs133_Probe_D2-Cs133'

    foldername1 = f'gamma=0.0019-DSteps=300-DScan=4.00sigma-lWidth=2.0/'\
                  f'Pump_4-3-theta=0.79-phi=1.57-pol=0-det=0_Probe_4-4-det=25/'\
                  f'Absorption_theta=1.57-1.57_phi=0.00-0.00_pol=4--4_'\
                  f'ph={phase[0]}-{phase[1]}_a={alpha[0]}-{alpha[1]}_gammaprobe=0.0190_lWidthpr=2.0'

    directory = os.path.join(foldername0, foldername1) #os.path.relpath(foldername0)
    theorPath = os.path.join(directory, fileName)

    return theorPath

def combineTheorData(dataframe1, dataframe2, comp='comp2'):
    compinedDataframe = pd.DataFrame(dataframe1['B'])
    compinedDataframe['comp1'] = dataframe1['comp1']
    compinedDataframe['comp2'] = dataframe2[comp]
    compinedDataframe['Total'] = compinedDataframe['comp1'] + compinedDataframe['comp2']
    compinedDataframe['diff'] = compinedDataframe['comp1'] - compinedDataframe['comp2']
    # compinedDataframe['circ'] = (compinedDataframe['comp1'] - compinedDataframe['comp2']) / (compinedDataframe['comp1'] + compinedDataframe['comp2'])
    compinedDataframe.dropna(inplace=True)
    print(compinedDataframe.head())
    compinedDataframe = compinedDataframe[['B', 'Total', 'comp1', 'comp2', 'diff']]
    print(compinedDataframe.head())
    return compinedDataframe

if __name__ == '__main__':
    rabi = 20

    phase1 = [90, -90]
    alpha1 = [0, -45]

    phase2 = [-89, -88]
    alpha2 = [-45, -45]
    phase2_list = [[-89, -88], [-87, -86], [-85, -80], [-70, -60], [-50, -40], [-20, 0]]

    # filepath1 = getFilePath_full_phase(rabi, phase1, alpha1)
    # print(filepath1)
    # theorData1 = importData(filepath1)
    # print(theorData1)

    for phase2 in phase2_list:

        filepath1 = getFilePath_full_phase(rabi, phase1, alpha1)
        print(filepath1)
        theorData1 = importData(filepath1)
        # print(theorData1)

        filepath2 = getFilePath_full_phase(rabi, phase2, alpha2)
        print(filepath2)
        theorData2 = importData(filepath2)
        # print(theorData2)

        for idx_comp, comp in enumerate(['comp1', 'comp2']):
            combined_data = combineTheorData(theorData1, theorData2, comp=comp)
            # print(combined_data)
            new_phase = [phase1[0], phase2[idx_comp]]
            new_alpha = [alpha1[0], alpha2[idx_comp]]
            new_filepath = getFilePath_full_phase(rabi, new_phase, new_alpha)
            print(new_filepath)
            new_directory = os.path.split(new_filepath)[0]
            print(new_directory)
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)

            combined_data.to_csv(new_filepath, header=False, index=False, sep=" ")