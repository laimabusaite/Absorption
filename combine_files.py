import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from plotElliptic import importData
from plotElipseDependence import getFilePath
# from plotD2excitationLinear import combineTheorData

# def combine_files(file_path1, file_path2):
#     theorData1 = importData(file_path1)
#     theorData2 = importData(file_path2)
#
#     combined_data = combineTheorData(theorData1, theorData2)

def combineTheorData(dataframe1, dataframe2):
    compinedDataframe = pd.DataFrame(dataframe1['B'])
    compinedDataframe['comp1'] = dataframe1['comp1']
    compinedDataframe['comp2'] = dataframe2['comp2']
    compinedDataframe['Total'] = compinedDataframe['comp1'] + compinedDataframe['comp2']
    compinedDataframe['diff'] = compinedDataframe['comp1'] - compinedDataframe['comp2']
    # compinedDataframe['circ'] = (compinedDataframe['comp1'] - compinedDataframe['comp2']) / (compinedDataframe['comp1'] + compinedDataframe['comp2'])
    compinedDataframe.dropna(inplace=True)
    compinedDataframe = compinedDataframe[['B', 'Total', 'comp1', 'comp2', 'diff']]
    return compinedDataframe

if __name__ == '__main__':

    rabi = 20

    phase1 = [60, -60]
    alpha1 = [0, -15]

    phase2 = [90, -60]
    alpha2 = [0, 0]

    filepath1 = getFilePath(rabi, phase1, alpha1)
    theorData1 = importData(filepath1)
    print(theorData1)

    filepath2 = getFilePath(rabi, phase2, alpha2)
    theorData2 = importData(filepath2)
    print(theorData2)

    combined_data = combineTheorData(theorData1, theorData2)
    print(combined_data)

    new_phase = [phase1[0], phase2[1]]
    new_alpha = [alpha1[0], alpha2[1]]
    new_filepath = getFilePath(rabi, new_phase, new_alpha)
    print(new_filepath)
    combined_data.to_csv(new_filepath, header=False, index=False, sep=" ")


