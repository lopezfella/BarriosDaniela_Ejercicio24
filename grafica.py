plt.figure()
data = np.loadtxt("datos.dat")
plt.plot(data[:,0], data[:,1], label = 'Funcion gaussiana')
plt.hist(v, bins=25, color='g', label='Números que siguen una distribución gaussiana')
plt.legend()
plt.savefig("gausiana.png")
