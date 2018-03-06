//Grafico Laberinto  
 def GraficoLaberinto(self):
        for y in range(self.Filas):
            for x in range(self.Columnas):
                if self.Laberinto[y][x] == Pared:
                    color('black')






    def DibujarPared(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moverTortuga(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def tirarMigaDePan(self,color):
        self.t.dot(10,color)

    def actualizarPosicion(self,fila,columna,val=None):
        if val:
            self.listaLaberinto[fila][columna] = val
        self.moverTortuga(columna,fila)

        if val == PARTE_DEL_CAMINO:
            color = 'green'
        elif val == OBSTACULO:
            color = 'red'
        elif val == INTENTADO:
            color = 'black'
        elif val == CAJELLON_SIN_SALIDA:
            color = 'red'
        else:
            color = None

        if color:
            self.tirarMigaDePan(color)

    def esSalida(self,fila,columna):
        return (fila == 0 or
                fila == self.filasEnLaberinto-1 or
                columna == 0 or
                columna == self.columnasEnLaberinto-1 )

    def __getitem__(self,indice):
        return self.listaLaberinto[indice]

