from matplotlib import colors
import numpy as np
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import copy as copy

"""Clase contenedora, Laberinto"""
class Laberinto(object):
    
    """
    Constructor del objeto Laberinto
    """ 
    def __init__(self):
        
        """
        Atributos clase laberinto:
        data: arreglo que almacena dos valores posibles 0 o 1. Donde 0 realmacena los elementos del arreglo laberinto
        filas:Un escalar entero que representa la .... almacena el numero de filas del arreglo laberinto
        columnas: almacena el numero de columnas del arreglo laberinto
        """
        self.data = []
        self.filas = 0
        self.columnas = 0
    
    """
    Metodo existelaberinto: pregunta si el laberinto es un arreglo vacio. Su argumento es:
    objeto laberinto
    """
    def existelaberinto(self):

        if self.data ==[]:
	    return 'FALSE'
	else:
	    return 'TRUE'
    
    """
    Metodo generarlaberinto: pregunta si el laberinto es un arreglo vacio y si es asi genera un arreglo,si no imprime error.
    Sus argumentos son:
    objeto laberinto
    columnas
    filas
    complejidad: Parametro que controla la dificultad del laberinto generado.
    densidad:Parametro que controla la cantidad de paredes generadas.
    """
<<<<<<< HEAD
    def generarlaberinto(self,columnas=100, filas=50, complejidad=0.95, densidad=0.75):
        if self.existelaberinto() == 'FALSE':
            
            """
            Para generar solo matrices de dimensiones impares. Tupla que indican el numero de filas y columnas
=======
    def generarlaberinto(self,columnas=100, filas=100, complejidad=0.95, densidad=4.75):
        if self.existelaberinto() == 'FALSE':
            
            """
            Para generar solo matrices de dimensiones impares
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
            """   
            forma = ((filas // 2) * 2 + 1, (columnas // 2) * 2 + 1)
            
            """
<<<<<<< HEAD
            Ajusta complejidad y densidad de acuerdo al tamano del laberinto.
=======
            Ajusta complejidad y densidad de acuerdo al tamano del laberinto
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
            """
            complejidad = int(complejidad * (5 * (forma[0] + forma[1])))
            densidad    = int(densidad * ((forma[0] // 2) * (forma[1] // 2)))
            

            """ 
            Crear el arreglo laberinto
            """
            self.data = np.zeros(forma, dtype=int )
            
            """ 
            Genero los bordes
            """
            self.data[0, :] = self.data[-1, :] = 1
            self.data[:, 0] = self.data[:, -1] = 1
            self.data[1, 1] = 3 
	    self.data[25, 0] = 5
            
            """
            Genero los pasillos
            """
            for i in range(densidad):
                x, y = rand(0, forma[1] // 2) * 2, rand(0, forma[0] // 2) * 2
                self.data[y, x] = 1
                for j in range(complejidad):
                    vecinos = []
                    if x > 1:             vecinos.append((y, x - 2))
                    if x < forma[1] - 2:  vecinos.append((y, x + 2))
                    if y > 1:             vecinos.append((y - 2, x))
                    if y < forma[0] - 2:  vecinos.append((y + 2, x))
                    if len(vecinos):
                        y_,x_ = vecinos[rand(0, len(vecinos) - 1)]
                        if self.data[y_, x_] == 0:
                            self.data[y_, x_] = 1
                            self.data[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                            x, y = x_, y_
            return  self.data     
        else:
            print "error"
	
      
"""
Clase Obstaculo, contenida en Laberinto
"""
class Obstaculo(object):
     
    """
<<<<<<< HEAD
    Metodos clase obstaculo. 
=======
    Metodos clase obstaculo
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
    """   
    def __init__(self,pos,tipo): 
       
        """
<<<<<<< HEAD
        Atributos del objeto Obstaculo. Posicion y tipo
=======
        Atributos del objeto Obstculo
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
        """      
        self.pos = pos
        self.tipo = tipo



class Robot(object):
   '''Clase generadora del objeto robot '''
   def __init__(self,pos):
<<<<<<< HEAD
      '''Constructor del objeto robot, con el atributo posicion que es una tupla que indica la posicion matricial del robot. (fila,columna)'''
=======
      '''Constructor del objeto robot, con los atributos posicion, frente (a donde mira), memoria '''
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
      self.pos = pos


   def avanzar(self,pos,front):
<<<<<<< HEAD
      '''Metodo avanzar. Sus argumentos son la posicion del robot y el frente. Hace que el robot avance cambiando de posicion'''
=======
      '''Metodo avanzar'''
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
     
      self.pos= np.add(pos,front)    
      return self.pos


        
if __name__ == "__main__":
     
<<<<<<< HEAD
    i=0
    L=Laberinto()
    Laberinto.generarlaberinto(L)
    a=[]
    copy.deepcopy(a)
    
=======
  
    L=Laberinto()
    Laberinto.generarlaberinto(L)
       # Sentencia que controla el color del arreglo
#######################################################
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
    r=Robot([1,1])
    right=[0,1]
    left=[0,-1]
    up=[-1,0]
    down=[1,0]
    front= [0,1]
<<<<<<< HEAD
    """Defino la posicion inicial del robot, la derecha, iaquierda arriba, abajo y frente como una tupla"""

=======
    '''Asignacion de la posicion inicial (en forma matricial) y frente inicial (en forma cartesiana) del robot'''
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b
    while (L.data[tuple(np.add(r.pos,up))] != 5 and L.data[tuple(np.add(r.pos,down))] != 5 and L.data[tuple(np.add(r.pos,right))] != 5 and L.data[tuple(np.add(r.pos,left))] != 5):
      ''' Criterios para tomar decicionens y buscar la salida'''
      if(L.data[tuple(np.add(r.pos,up))]==1 and (L.data[tuple(np.add(r.pos,right))]==0 or L.data[tuple(np.add(r.pos,right))]==3 or L.data[tuple(np.add(r.pos,right))]==5) and front == right):
           L.data[tuple(r.avanzar(r.pos,front))] = 3
      elif (L.data[tuple(np.add(r.pos,right))] == 1 and (L.data[tuple(np.add(r.pos , down))] == 0 or L.data[tuple(np.add(r.pos,down))]==3 or L.data[tuple(np.add(r.pos,down))]==5) and front == down):
           L.data[tuple(r.avanzar(r.pos,front))]=3
      elif(L.data[tuple(np.add(r.pos,down))] == 1 and (L.data[tuple(np.add(r.pos ,left))] == 0 or L.data[tuple(np.add(r.pos,left))]==3 or L.data[tuple(np.add(r.pos,left))]==5) and front == left):
           L.data[tuple(r.avanzar(r.pos,front))]=3
      elif(L.data[tuple(np.add(r.pos,left))] == 1 and (L.data[tuple(np.add(r.pos ,up))] == 0 or L.data[tuple(np.add(r.pos,up))]==3 or L.data[tuple(np.add(r.pos,up))]==5) and front == up):
           L.data[tuple(r.avanzar(r.pos,front))]=3
      elif (L.data[tuple(np.add(r.pos,up))] == 1 and L.data[tuple(np.add(r.pos,right))] == 1 and front == right):
            front = down 
      elif (L.data[tuple(np.add(r.pos,right))] == 1 and L.data[tuple(np.add(r.pos ,down))] == 1  and front ==down):
            front = left
      elif (L.data[tuple(np.add(r.pos,down))] == 1 and L.data[tuple(np.add(r.pos,left))] == 1 and front==left):
            front = up
      elif  (L.data[tuple(np.add(r.pos,left))] == 1 and L.data[tuple(np.add(r.pos, up))] == 1 and front == up):
            front = right
      elif ((L.data[tuple(np.add(r.pos,up))] == 0 or L.data[tuple(np.add(r.pos,up))] == 3 or L.data[tuple(np.add(r.pos,up))] == 5) and (L.data[tuple(np.add(r.pos,right))] == 1 or L.data[tuple(np.add(r.pos,right))]==0 or L.data[tuple(np.add(r.pos,right))]==3) and front == right):
            front = up 
            L.data[tuple(r.avanzar(r.pos,front))]=3
      elif ((L.data[tuple(np.add(r.pos,right))] == 0 or L.data[tuple(np.add(r.pos,right))] == 3 or L.data[tuple(np.add(r.pos,right))] == 5) and (L.data[tuple(np.add(r.pos,down))] == 1 or L.data[tuple(np.add(r.pos,down))] == 0 or L.data[tuple(np.add(r.pos,down))] == 3) and front == down):
            front = right 
            L.data[tuple(r.avanzar(r.pos,front))]=3
      elif ((L.data[tuple(np.add(r.pos,down))] == 0 or L.data[tuple(np.add(r.pos,down))] == 3 or L.data[tuple(np.add(r.pos,down))] == 5) and (L.data[tuple(np.add(r.pos,left))] == 1 or L.data[tuple(np.add(r.pos,left))] == 0 or L.data[tuple(np.add(r.pos,left))] == 3) and front == left):
            front = down 
            L.data[tuple(r.avanzar(r.pos,front))]=3
      elif ((L.data[tuple(np.add(r.pos,left))] == 0 or L.data[tuple(np.add(r.pos,left))] == 3 or L.data[tuple(np.add(r.pos,left))] == 5) and (L.data[tuple(np.add(r.pos,up))] == 1 or L.data[tuple(np.add(r.pos,up))] == 0 or L.data[tuple(np.add(r.pos,up))] == 3)   and front == up):
            front = left 
            L.data[tuple(r.avanzar(r.pos,front))]=3
<<<<<<< HEAD
      

      else: print "Esta todo considerado (?)"
      '''Metodo para que el robot encuentre la salida del laberinto, si a la hora de tomar la decision ocurre una circunstancia no considerada imprime error'''
      a.append(copy.deepcopy(L.data))




    def func_variacion(frame):
        matriz.set_array(a[frame])
    fig, ax = pyplot.subplots()
    matriz = ax.matshow(a[0])
    
    ani = animation.FuncAnimation(fig, func_variacion, frames=10000, interval=50, repeat=False)   

=======
###########################################################
#      elif (L.data[tuple(np.add(r.pos,right))] == 0 and (L.data[tuple(np.add(r.pos,left))] == 1 or L.data[tuple(np.add(r.pos,left))] == 3) and front == down):
#            front = right
#      elif (L.data[tuple(np.add(r.pos,left))] == 3 and (L.data[tuple(np.add(r.pos,up))] == 1 or L.data[tuple(np.add(r.pos,left))] == 3) and front == up):
#            front = left   
#      
###########################################################
      else: print "Esta todo considerado (?)"
      print L.data
      print r.pos, front 
      print L.data[tuple(np.add(r.pos,up))],L.data[tuple(np.add(r.pos,right))]
      #print L.data
      #print r.pos

  
########################################################

    def func_variacion(frame):    
        
        matriz.set_array(L.data)
    fig, ax = pyplot.subplots()
    matriz = ax.matshow(L.data)
    ani = animation.FuncAnimation(fig, func_variacion, frames=10, interval=1500, repeat=False)   

        # Muestra un arreglo como una matriz en una nueva figura
>>>>>>> 54d3f7a973226393c507e5d34885f86697a74d5b

          


    """animation.FuncAnimation: Funcion que genera la animacion. Sus argumentos son:
    fig: Objeto de figura que se utiliza para obtener un grafico.
    func_variacion: Esta funcion es la que genera la variacion en el objeto que queremos modificar. Es llamada tantas veces como indique la
    variable frames en animation.FuncAnimation. La variable frame es muda (podria tener cualquier otro nombre) y va de 0 a frames.
    frames: Establece el numero total de imagenes que se van a mostrar.
    interval: Tiempo trasncurrido entre un frame y el siguiente.
    repeat: Variable logica. La funcion animation.FuncAnimation repite todo el proceso indefinidamente a menos que establezcamos que repeat
    vale false."""

    pyplot.show() 




