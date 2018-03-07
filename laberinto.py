import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot

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
    def generarlaberinto(self,columnas=7, filas=7, complexity=.85, density=.75):
        if self.existelaberinto() == 'FALSE':
            # Only odd shapes
            shape = ((filas // 2) * 2 + 1, (columnas // 2) * 2 + 1)
            # Adjust complexity and density relative to maze size
            complexity = int(complexity * (5 * (shape[0] + shape[1])))
            density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
            """ Crear el arreglo laberinto"""
            Z = np.zeros(shape, dtype=int )
            """ Genero los bordes"""
            Z[0, :] = Z[-1, :] = 1
            Z[:, 0] = Z[:, -1] = 1
            Z[1, 0] = Z[-1, -2] = 0
            """ Genero los pasillos"""
            for i in range(density):
                x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
                Z[y, x] = 1
            for j in range(complexity):
                neighbours = []
                if x > 1:             neighbours.append((y, x - 2))
                if x < shape[1] - 2:  neighbours.append((y, x + 2))
                if y > 1:             neighbours.append((y - 2, x))
                if y < shape[0] - 2:  neighbours.append((y + 2, x))
                if len(neighbours):
                    y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                    if Z[y_, x_] == 0:
                        Z[y_, x_] = 1
                        Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                        x, y = x_, y_

            return  Z     
            #self.data=Z 
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
    
#def figura(posicion=(0, 1)):
    #robot.posicion = posicion
    
    
    a=Laberinto()

    a.data=a.generarlaberinto()
    a.data[[1], [0]] = 2
    print a.data 
    
    pyplot.figure(figsize=(10, 10))
    pyplot.imshow(a.data, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()



