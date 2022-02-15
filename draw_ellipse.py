import numpy as np
import matplotlib.pyplot as plt

def ellipse(omega, phase, alpha):
    """
    alpha - deg, phase - deg
    """
    x = 1./np.sqrt(2.) * np.real(
        (np.cos(alpha * np.pi/180.) - np.exp(1.j*phase * np.pi/180.) * np.sin(alpha * np.pi/180.)) * np.exp(
            1.j*omega * np.pi/180.))

    y = 1. / np.sqrt(2.) * np.real(
        (np.sin(alpha * np.pi / 180.) - np.exp(1.j * phase * np.pi / 180.) * np.cos(alpha * np.pi / 180.)) * np.exp(
            1.j * omega * np.pi / 180.))

    return x, y

omega = np.linspace(0,360,101)

phase = 0
alpha = 0
x, y = ellipse(omega, phase, alpha)
print(x, y)

plt.figure(figsize=(3,3))
plt.plot(x, y)
plt.show()