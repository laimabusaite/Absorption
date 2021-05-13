from plotElliptic import *
from plotD2excitationElliptic import *
from plotD2excitationLinear import *

if __name__ == '__main__':
    rabi = 20
    pol = 4
    phase = [-100, 100]
    alpha = [-40, 0]

    filePath1 = getFilePath(rabi=rabi, pol=pol, phase=phase, alpha=alpha)
    print(filePath1)
    theorData1 = importData(filePath1)
    print(theorData1)
    fig1 = plt.figure(1)
    axs1 = []
    for i in range(4):
        axs1.append(fig1.add_subplot(2, 2, i + 1))
    plotData(theorData1, axs1, label=f'rabi={rabi}, pol={pol}, phase={phase}, alpha={alpha}')

    pol = 0

    filePath2 = getFilePath(rabi=rabi, pol=pol, phase=phase, alpha=alpha)
    print(filePath2)
    theorData2 = importData(filePath2)
    print(theorData2)
    print(max(abs(theorData1['diff'])) / max(abs(theorData2['diff'])))
    plotData(theorData2, axs1, label=f'rabi={rabi}, pol={pol}, phase={phase}, alpha={alpha}')

    scale = max(abs(theorData1['diff'])) / max(abs(theorData2['diff']))
    print(scale)
    scale = max(abs(theorData1['diff'][theorData1['B']>2000])) / max(abs(theorData2['diff'][theorData2['B']>2000]))
    print(scale)
    theorData2['diff'] = theorData2['diff'] * scale
    print(theorData2)
    plotData(theorData2, axs1, label=f'diff scale = {scale:.3f}, rabi={rabi}, pol={pol}, phase={phase}, alpha={alpha}')

    pol = 1

    filePath3 = getFilePath(rabi=rabi, pol=pol, phase=phase, alpha=alpha)
    print(filePath3)
    theorData3 = importData(filePath3)
    print(theorData3)
    plotData(theorData3, axs1, label=f'rabi={rabi}, pol={pol}, phase={phase}, alpha={alpha}')

    fig2 = plt.figure(2)
    diffdiff = theorData2['diff'] - theorData1['diff']
    plt.plot(theorData1['B'], diffdiff, label=f'diff Elliptic - Linear*{scale:.3f}')
    plt.plot(theorData3['B'], theorData3['diff'], label=f'diff Circular')
    plt.legend()

    fig3 = plt.figure(3)
    plt.plot(theorData1['B'], diffdiff-theorData3['diff'], label=f'diff Elliptic - Linear*{scale:.3f} - Circular')
    plt.legend()

    plt.show()