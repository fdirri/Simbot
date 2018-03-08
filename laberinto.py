from matplotlib import colors
import numpy as np
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

"""Clase contenedora, Laberinto"""
class Laberinto(object):
    
    """Constructor del objeto Laberinto""" 
    def __init__(self):
        
        """Atributos clase laberinto"""
        self.data = []
        self.filas = 0
        self.columnas = 0
    """Metodo existelaberinto: pregunta si el laberinto es un arreglo vacio"""
    def existelaberinto(self):

        if self.data ==[]:
	    return 'FALSE'
	else:
	    return 'TRUE'
    """Metodo generarlaberinto: pregunta si el laberinto es un arreglo vacio y si es asi genera un arreglo,sino imprime error"""
    def generarlaberinto(self,columnas=5, filas=5, complexity=105.95, density=.75):
        if self.existelaberinto() == 'FALSE':
            # Only odd shapes
            shape = ((filas // 2) * 2 + 1, (columnas // 2) * 2 + 1)
            # Adjust complexity and density relative to maze size
            complexity = int(complexity * (5 * (shape[0] + shape[1])))
            density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
            """ Crear el arreglo laberinto"""
            self.data = np.zeros(shape, dtype=int )
            """ Genero los bordes"""
            self.data[0, :] = self.data[-1, :] = 1
            self.data[:, 0] = self.data[:, -1] = 1
            self.data[1, 0] = 2 
	    self.data[-1, -2] = 0
            """ Genero los pasillos"""
            for i in range(density):
                x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
                self.data[y, x] = 1
                for j in range(complexity):
                    neighbours = []
                    if x > 1:             neighbours.append((y, x - 2))
                    if x < shape[1] - 2:  neighbours.append((y, x + 2))
                    if y > 1:             neighbours.append((y - 2, x))
                    if y < shape[0] - 2:  neighbours.append((y + 2, x))
                    if len(neighbours):
                        y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                        if self.data[y_, x_] == 0:
                            self.data[y_, x_] = 1
                            self.data[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                            x, y = x_, y_
            return  self.data     
        else:
            print "error"
	

            
        
      
"""Clase Obstaculo, contenida en Laberinto"""
class Obstaculo(object):
     
    """Metodos clase obstaculo"""   
    def __init__(self,posicion,tipo): 
       
        """Atributos del objeto Obstculo"""      
        self.posicion = posicion
        self.tipo = tipo
        
if __name__ == "__main__":
     
    
    L=Laberinto()
    Laberinto.generarlaberinto(L)

def func_variacion(frame):    
# Funcion animacion:. Es llamada tantas veces como indique 'frames'. La variable 'frame' es muda (podria tener cualquier otro nombre) y va de #0 a 'frames'
    matriz.set_array(L.data)       # Controla el color del arreglo

fig, ax = pyplot.subplots()      # Primer argumento de FuncAnimation. Objeto de figura que se utiliza para obtener un grafico
matriz = ax.matshow(L.data)        # Muestra un arreglo como una matriz en una nueva figura


ani = animation.FuncAnimation(fig, func_variacion, frames=10, interval=500, repeat=False) 
# Funcion animacion. Esta funcion se llama recursivamente tantas veces como establezca 'frames'. FuncAnimation repite todo el proceso #indefinidamente a menos que le indiquemos lo contrario, con repeat=False. 'Interval' determina el tiempo entre una imagen y la siguiente.

pyplot.show() 

#figura( [5,5] )


