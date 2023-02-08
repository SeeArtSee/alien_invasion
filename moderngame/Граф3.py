import numpy as np
import matplotlib.pyplot as plt
plt.subplot(111, polar=True)
phi = np.arange(0, 5*np.pi, 0.01)
rho = 6*phi
plt.plot(phi, rho, lw=2)
plt.show()