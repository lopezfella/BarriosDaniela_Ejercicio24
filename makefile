gaussiana.png: grafica.py datos.dat
	python grafica.py 
	
datos.dat: metro.x
	./metro.x > datos.dat

metro.x: metropolis.cpp
	c++ metropolis.cpp -o metro.x
	
clean:
	rm metro.x datos.dat gaussiana.png
