import numpy as np

salida=[10,10]

derecha=[0.1]

izquierda=[0,-1]

arriba=[1,0]

abajo=[-1,0]

class Laberinto(object):

   def __init__(self,largo,alto):
       
       self.largo= largo
       self.ancho= ancho
   
class Obstaculo(object):
    
   def __init__(self,posicion,tipo):
      self.posicion=posicion
      self.tipo=tipo

class Robot(object):
   '''Clase generadora del objeto robot '''
   def __init__(self,posicion,frente):
      '''Constructor del objeto robot, con los atributos posicion, frente (a donde mira), memoria '''
      self.posicion = posicion
      self.frente = frente

   def avanzar(self):
      '''Metodo avanzar'''
      self.posicion = posicion + frente                   
      self.memoria = np.add[(t,posicion)]

#  def girarDerecha(self):
#     '''Metodo girarDerecha, la notacion [x,y] esta en notacion matricial y no es un vector cartesiano'''
#     '''Ejemplo: Si ponemos [0,1] significa que el robot mira en la direccion en la que aumento el # de columnas'''
#     if self.frente == [0,1]:
#        self.frente = [1,0]
#     if self.frente == [1,0]:
#        self.frente = [0,-1]
#     if self.frente == [0,-1]:
#        self.frente = [-1,0]
#     if self.frente == [-1,0]:
#        self.frente = [0,1]
#     
#  def girarIzquierda(self):
#     '''Metodo girarIzquierda, la notacion [x,y] esta en notacion matricial y no es un vector cartesiano !!!!!!!'''
#     '''Ejemplo: Si ponemos [-1,0] significa que el robot mira en la direccion en la que disminuyo el # de filas'''
#     if self.frente == [0,1]:
#        self.frente = [-1,0]
#     if self.frente == [-1,0]:
#        self.frente = [0,-1]
#     if self.frente == [0,-1]:
#        self.frente = [1,0]
#     if self.frente == [1,0]:
#        self.frente = [0,1]
       
if __name__ == "__main__":
   r=Robot([1,1],[0,1])
   '''Asignacion de la posicion inicial (en forma matricial) y frente inicial (en forma cartesiana) del robot'''
   while (r.posicion != salida):
      ''' Criterios para tomar decicionens y buscar la salida'''
      while(l.posicion(r.posicion+arriba) == 1 and l.posicion(r.posicion + derecha) == 0 and r.frente = derecha):
         r.avanzar()
      else:
         while(l.posicion(r.posicion+derecha) == 1 and l.posicion(r.posicion + abajo) == 0 and r.frente = abajo):
            r.avanzar()
      else:
         while(l.posicion(r.posicion+abajo) == 1 and l.posicion(r.posicion + izquierda) == 0 and r.frente = izquierda):
            r.avanzar()
      else:
         while(l.posicion(r.posicion+izquierda) == 1 and l.posicion(r.posicion + arriba) == 0 and r.frente = arriba):
            r.avanzar()
      else:
         if (l.posicion(r.posicion+arriba) == 1 and l.posicion(r.posicion + derecha) == 1 and r.frente = derecha):
            self.frente = abajo 

         else if: (l.posicion(r.posicion+derecha) == 1 and l.posicion(r.posicion + abajo) == 1 and r.frente = abajo):
            self.frente = izquierda
   
         else if: (l.posicion(r.posicion+abajo) == 1 and l.posicion(r.posicion+izquierda) == 1 and r.frente=izquierda):
            self.frente = arriba

         else if: (l.posicion(r.posicion+izquierda) == 1 and l.posicion(r.posicion + arriba) == 1 and r.frente = arriba):
            self.frente = derecha

