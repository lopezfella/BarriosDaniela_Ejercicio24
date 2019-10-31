import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
data = np.loadtxt("datos.dat")
plt.hist(data, bins=25, color='g', label = 'gaussiana')
plt.legend()
plt.xlabel('X')
plt.ylabel('Histograma')
plt.savefig("gausiana.png")
