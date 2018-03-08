import numpy as np
import matplotlib.pyplot as pyplot 
import matplotlib.animation as animation

M = np.random.rand(5,5)       # Genera una matriz aleatoria

def func_variacion(frame):    
# Funcion animacion. Es llamada tantas veces como indique 'frames'. La variable 'frame' es muda (podría tener cualquier otro nombre) y va de 0 a 'frames'
    M = np.random.rand(5,5)   
    matriz.set_array(M)       # Controla el color del arreglo

fig, ax = pyplot.subplots()      # Primer argumento de FuncAnimation. Objeto de figura que se utiliza para obtener un grafico
matriz = ax.matshow(M)        # Muestra un arreglo como una matriz en una nueva figura


ani = animation.FuncAnimation(fig, func_variacion, frames=10, interval=500, repeat=False) 
# Funcion animacion. Esta funcion se llama recursivamente tantas veces como establezca 'frames'. FuncAnimation repite todo el proceso indefinidamente a menos que le indiquemos lo contrario, con repeat=False. 'Interval' determina el tiempo entre una imagen y la siguiente.

pyplot.show()                    # Para graficar