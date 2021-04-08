import matplotlib.pyplot as plt
from plotTheory import plotRabiDependence

if __name__ == "__main__":
    rabiList = [1, 20, 50, 100]

    folderNameList = ['Test_circular_components/ellipse1',
                      'Test_circular_components/ellipse2',
                      'Test_linear_polarization/linear',
                      'Circular']

    titleList = ['Ellipse1 \n theta = 90 deg, phi = 0 deg \n comp1: phase = -100 deg, alpha = -40 deg, \n comp2: phase=100 deg, alpha = 0 deg',
                 'Ellipse2 \n theta = 90 deg, phi = 0 deg \n comp1: phase = 100 deg, alpha = -40 deg, \n comp2: phase=-100 deg, alpha = 0 deg',
                 'Linear \n comp1: pol = 0, theta = 0 deg, phi = 0 deg (z-dir), \n comp2: pol = 0, theta = 90 deg, phi = 90 deg (y-dir)',
                 'Circular \n comp1: pol = 1, theta = 90 deg, phi = 0 deg, \n comp2: pol = -1, theta = 90 deg, phi = 0 deg']

    for idx, folderName in enumerate(folderNameList):
        title = titleList[idx]
        plotRabiDependence(rabiList, folderName=folderName, title=title)
    plt.show()