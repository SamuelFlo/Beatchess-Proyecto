import chess
from tkinter import *
import tablero
import ajedrez_parser
from tkinter import messagebox as MessageBox
from AlphaBetaPruning import ABPruningAI
import random
import MCTS

#Clase Principal
class BeatChess():
    cont = 0
    flag=0
    filas = 8
    columnas = 8
    color1 = "#45e7a5"
    color2 = "#e75445"
    sombra_color1 = "#696969"
    sombra_color2 = "#A9A9A9"
    color_casillas_tablero = {}
    dim_casilla = 48  #64
    imagenes = {}
    posibles_jugadas = []
    #para ejecutar los movimientos
    casilla_origen = None
    casilla_destino = None
    verificar_checkMate = False
    verificar_check = False
    verificar_draw = False

    #AlphaBetaPruning
    AI = ABPruningAI(3)
    

    #Constructor de la clase
    def __init__(self, raiz, posicion):
        self.raiz = raiz
        self.tablero = posicion
        canvas_width = self.columnas * self.dim_casilla
        canvas_height = self.filas * self.dim_casilla
        panes = PanedWindow(raiz, bg='grey', width=2.5*canvas_width)
        panes.pack()
        self.canvas = Canvas(panes, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.ventana_derecha = Canvas(panes, width=canvas_width, height=canvas_height)
        self.ventana_derecha.pack(padx=12, pady=12)
        panes.add(self.canvas)
        panes.add(self.ventana_derecha)
        self._drag_data = {"x": 0, "y": 0, "item": None}

     #Funcion para dibujar el tablero en la interfaz grafica
    def dibuja_tablero(self):
        self.canvas.delete("area")
        color = self.color1
        for r in range(self.filas):
            color = self.color1 if color == self.color2 else self.color2 
            num_casilla = str(r+1)
            for c in range(self.columnas):
                letra_casilla = chr(97 + c)
                x1 = (c * self.dim_casilla)
                y1 = ((7-r) * self.dim_casilla)
                x2 = x1 + self.dim_casilla
                y2 = y1 + self.dim_casilla
                id_casilla = str(x1) + '-' + str(y1) + '-' + str(x2) + '-' + str(y2)
                self.canvas.create_rectangle(x1, y1, x2, y2,  fill=color, tags=(id_casilla,"area"))
                color = self.color1 if color == self.color2 else self.color2
                color_sombreado = None
                if color == self.color1 :
                    color_sombreado = self.sombra_color1
                else:
                    color_sombreado = self.sombra_color2
                estruct_casilla = {'color_sin_sombra': color, 'color_con_sombra': color_sombreado, 
                                'x1':x1, 'y1':y1, 'x2':x2, 'y2':y2}
                self.color_casillas_tablero[letra_casilla + num_casilla] = estruct_casilla
                self.cont = self.cont +1


                
    #Funcion para dibujar las piezas en la interfaz grafica
    def dibuja_piezas(self):
        self.canvas.delete("ocupada")
        for xycoord, valor in self.tablero.items():
            #sacamos las coordenadas de cada casilla : c8 será --> 7,2 ; a8 --> 7,0 y asi sucesivamente
            x,y = self.tablero.num_notacion(xycoord)
            if valor is not None:
                nom_fichero = "./piezas/%s%s.png" % (valor['color'], valor['type'])
                if valor['color'] == 'w' :
                    nom_pieza = "%s%s%s" % (valor['type'].upper(), x, y)
                else:
                    nom_pieza = "%s%s%s" % (valor['type'], x, y)
                if(nom_fichero not in self.imagenes):
                    self.imagenes[nom_fichero] = PhotoImage(file=nom_fichero)
                self.obj_imagen = self.canvas.create_image(0,0, image=self.imagenes[nom_fichero], tags=(nom_pieza, "ocupada"), anchor="c")
                x0 = (y * self.dim_casilla) + int(self.dim_casilla/2)
                y0 = ((7-x) * self.dim_casilla) + int(self.dim_casilla/2)
                self.canvas.coords(nom_pieza, x0, y0)
                self.canvas.tag_bind(self.obj_imagen, "<Enter>", self.entra_mouse_over)
                self.canvas.tag_bind("ocupada", "<ButtonPress-1>", self.on_pieza_presionada)
                self.canvas.tag_bind("ocupada", "<ButtonRelease-1>", self.on_pieza_soltada)
                self.canvas.tag_bind("ocupada", "<B1-Motion>", self.on_pieza_moviendo)
        self.empezar()

    #Funcion para empezar turnos
    def empezar(self):
        if juego.turno() == 'b' and self.verificar_checkMate != True and self.verificar_draw != True:
            self.on_pieza_soltada_1()
        """
        elif juego.turno() == 'w' and self.verificar_checkMate != True and self.verificar_draw != True:
            self.on_pieza_soltada_2()
        """


    #Alphabeta
    def on_pieza_soltada_1(self):
        self.flag=1
        ai_move = self.AI.BestMove(chess.Board(juego.fen()))

        if self.flag ==0:
            listentrance=['e7e5','d7d5','b7b6','c7c5','f7f5','g7g6','a7a6','a7a5','c7c6','d7d6','e7e6','f7f6','g7g5','h7h6','h7h5']
            pos = random.randint(0,len(listentrance)-1)
            temp=listentrance[pos]
            self.casilla_origen = temp[0] + temp[1]
            self.casilla_destino = temp[2] + temp[3]
        else:
            temp = str(ai_move)
            self.casilla_origen = temp[0] + temp[1]
            self.casilla_destino = temp[2] + temp[3]

        movimiento = juego.move({'from': self.casilla_origen, 'to': self.casilla_destino, 'promotion': 'q'})


        self.flag = 1

        if movimiento:
            promocion = movimiento['promotion']
            pieza = movimiento['piece']
            san = movimiento['san']
            color = movimiento['color']
            flags = movimiento['flags']
            """
            El campo flags puede contener uno o mas de los valores siguientes:
            - 'n' - a non-capture
            - 'b' - a pawn push of two squares
            - 'e' - an en passant capture
            - 'c' - a standard capture
            - 'p' - a promotion
            - 'k' - kingside castling
            - 'q' - queenside castling
            """
            # O-O
            if '#' in movimiento['san']:
                self.verificar_checkMate = True
            elif '+' in movimiento['san']:
                self.verificar_check = True
            elif '~' in movimiento['san']:
                self.verificar_draw = True
            else:
                self.verificar_check = False

            # ahora vamos a arreglar el tablero interno
            # este primer del es para borrar la pieza de la casilla origen. Ocurre siempre
            del self.tablero[self.casilla_origen]  # borramos la pieza en el tablero interno
            # ahora vamos con los enroques
            if 'k' in movimiento['flags']:
                if movimiento['color'] == 'w':
                    del self.tablero['h1']
                elif movimiento['color'] == 'b':
                    del self.tablero['h8']
            if 'q' in movimiento['flags']:
                if movimiento['color'] == 'w':
                    del self.tablero['a1']
                elif movimiento['color'] == 'b':
                    del self.tablero['a8']
            # ahora vamos con la captura al paso
            if 'e' in flags:
                if movimiento['color'] == 'w':
                    numero = int(movimiento['to'][1]) - 1
                    numstr = str(numero)
                    casilla_a_borrar = movimiento['to'][0] + numstr
                    del self.tablero[casilla_a_borrar]
                elif movimiento['color'] == 'b':
                    numero = int(movimiento['to'][1]) + 1
                    numstr = str(numero)
                    casilla_a_borrar = movimiento['to'][0] + numstr
                    del self.tablero[casilla_a_borrar]
            self.tablero.procesa_notacion(juego.fen())
            self.dibuja_tablero()
            self.dibuja_piezas()

            # pyglet.font.add_file('./fuentes/ChessSansUscf.ttf') --> se tiene que poner en directorio de SO
            # fuente_ajedrez = pyglet.font.load('ChessSansUscf')
            depositLabel = Message(self.ventana_derecha, text=juego.pgn(), width=300, padx=2,
                                   justify=LEFT)  # , font_name='ChessSansUscf')
            depositLabel.grid(column=0, row=0)

        else:
            self.dibuja_tablero()
            self.dibuja_piezas()

    #Monte Carlo
    def on_pieza_soltada_3(self):
        MCT = MCTS.MCTSRoot(chess.Board(juego.fen()), 100)
        temp2 = (str)(MCT.getMostVisitedChild().move)
        self.casilla_origen = temp2[0] + temp2[1]
        self.casilla_destino = temp2[2] + temp2[3]
        movimiento = juego.move({'from': self.casilla_origen, 'to': self.casilla_destino, 'promotion': 'q'})

        if movimiento:
            promocion = movimiento['promotion']
            pieza = movimiento['piece']
            san = movimiento['san']
            color = movimiento['color']
            flags = movimiento['flags']
            """
            El campo flags puede contener uno o mas de los valores siguientes:
            - 'n' - a non-capture
            - 'b' - a pawn push of two squares
            - 'e' - an en passant capture
            - 'c' - a standard capture
            - 'p' - a promotion
            - 'k' - kingside castling
            - 'q' - queenside castling
            """

            # O-O
            if '#' in movimiento['san']:
                self.verificar_checkMate = True
            elif '+' in movimiento['san']:
                self.verificar_check = True
            elif '~' in movimiento['san']:
                self.verificar_draw = True
            else:
                self.verificar_check = False

            # ahora vamos a arreglar el tablero interno
            # este primer del es para borrar la pieza de la casilla origen. Ocurre siempre
            del self.tablero[self.casilla_origen]  # borramos la pieza en el tablero interno
            # ahora vamos con los enroques
            if 'k' in movimiento['flags']:
                if movimiento['color'] == 'w':
                    del self.tablero['h1']
                elif movimiento['color'] == 'b':
                    del self.tablero['h8']
            if 'q' in movimiento['flags']:
                if movimiento['color'] == 'w':
                    del self.tablero['a1']
                elif movimiento['color'] == 'b':
                    del self.tablero['a8']
            # ahora vamos con la captura al paso
            if 'e' in flags:
                if movimiento['color'] == 'w':
                    numero = int(movimiento['to'][1]) - 1
                    numstr = str(numero)
                    casilla_a_borrar = movimiento['to'][0] + numstr
                    del self.tablero[casilla_a_borrar]
                elif movimiento['color'] == 'b':
                    numero = int(movimiento['to'][1]) + 1
                    numstr = str(numero)
                    casilla_a_borrar = movimiento['to'][0] + numstr
                    del self.tablero[casilla_a_borrar]
            self.tablero.procesa_notacion(juego.fen())
            self.dibuja_tablero()
            self.dibuja_piezas()

            # pyglet.font.add_file('./fuentes/ChessSansUscf.ttf') --> se tiene que poner en directorio de SO
            # fuente_ajedrez = pyglet.font.load('ChessSansUscf')
            depositLabel = Message(self.ventana_derecha, text=juego.pgn(), width=300, padx=2,
                                   justify=LEFT)  # , font_name='ChessSansUscf')
            depositLabel.grid(column=0, row=0)

        else:
            self.dibuja_tablero()
            self.dibuja_piezas()



    # empezamos el drag &drop de las piezas
    def on_pieza_presionada(self, event):
        '''Comienza el arrastre de una pieza'''
        #para averiguar la casilla de inicio
        col_tamano = fila_tamano = self.dim_casilla
        seleccionada_columna = event.x // col_tamano
        seleccionada_fila = 7 - (event.y // fila_tamano)
        pos = self.tablero.alfa_notacion((seleccionada_fila, seleccionada_columna))
        if pos in self.tablero:
            if juego.turno() != self.tablero[pos]['color']:
                self.casilla_origen = None
            else:
                self.casilla_origen = pos
        else:
            self.casilla_origen = None
        if (self.verificar_checkMate == True):
            MessageBox.showinfo("Game Over!", "Jaque Mate!")
        elif self.verificar_draw == True:
            MessageBox.showinfo("Draw", "Empate!")
        #registramos el tema y su localizacion
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y



    def on_pieza_soltada(self, event):
        '''Final del arrastre de la pieza'''
        # reseteamos la informacion del arrastre
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        #ahora obtenemos la casilla destino
        col_tamano = fila_tamano = self.dim_casilla
        seleccionada_columna = event.x // col_tamano
        seleccionada_fila = 7 - (event.y // fila_tamano)
        self.casilla_destino = self.tablero.alfa_notacion((seleccionada_fila, seleccionada_columna))
        movimiento = juego.move({ 'from': self.casilla_origen, 'to': self.casilla_destino, 'promotion': 'q' })

        if movimiento:
            promocion = movimiento['promotion']
            pieza = movimiento['piece']
            san = movimiento['san']
            color = movimiento['color']
            flags = movimiento['flags']
            """
            El campo flags puede contener uno o mas de los valores siguientes:
            - 'n' - a non-capture
            - 'b' - a pawn push of two squares
            - 'e' - an en passant capture
            - 'c' - a standard capture
            - 'p' - a promotion
            - 'k' - kingside castling
            - 'q' - queenside castling
            """
            # O-O
            if '#' in movimiento['san']:
                self.verificar_checkMate = True
            elif '+' in movimiento['san']:
                self.verificar_check = True
            elif '~' in movimiento['san']:
                self.verificar_draw = True
            else:
                self.verificar_check = False

            #ahora vamos a arreglar el tablero interno
            # este primer del es para borrar la pieza de la casilla origen. Ocurre siempre
            del self.tablero[self.casilla_origen]   # borramos la pieza en el tablero interno
            #ahora vamos con los enroques
            if 'k' in movimiento['flags']:
                if movimiento['color'] == 'w':
                    del self.tablero['h1']
                elif movimiento['color'] == 'b':
                    del self.tablero['h8']
            if 'q' in movimiento['flags']:
                if movimiento['color'] == 'w':
                    del self.tablero['a1']
                elif movimiento['color'] == 'b':
                    del self.tablero['a8']
            #ahora vamos con la captura al paso
            if 'e' in flags:
                if movimiento['color'] == 'w':
                   numero = int(movimiento['to'][1]) - 1
                   numstr = str(numero)
                   casilla_a_borrar = movimiento['to'][0] + numstr
                   del self.tablero[casilla_a_borrar]
                elif movimiento['color'] == 'b':
                   numero = int(movimiento['to'][1]) + 1
                   numstr = str(numero)
                   casilla_a_borrar = movimiento['to'][0] + numstr
                   del self.tablero[casilla_a_borrar]
            self.tablero.procesa_notacion(juego.fen())
            self.dibuja_tablero()
            self.dibuja_piezas()
            if self.verificar_checkMate == True:
                MessageBox.showinfo("Game Over!", "Jaque Mate!")
            elif self.verificar_check==True:
                MessageBox.showinfo("Check", "Check!")
            elif self.verificar_draw==True:
                MessageBox.showinfo("Draw", "Empate!")
            depositLabel = Message(self.ventana_derecha, text=juego.pgn(), width=300, padx=2,
                                   justify=LEFT)  # , font_name='ChessSansUscf')
            depositLabel.grid(column=0, row=0)


        else:
            self.dibuja_tablero()
            self.dibuja_piezas()
            if self.verificar_check == True:
                MessageBox.showinfo("Check", "Check!")

    def on_pieza_moviendo(self, event):
        '''Maneja el arrastre de la pieza'''
        if self.casilla_origen == None:
            # reseteo la información del drag
            self._drag_data["item"] = None
            self._drag_data["x"] = 0
            self._drag_data["y"] = 0
        else:
            # calcula cuanto se ha movido el raton
            delta_x = event.x - self._drag_data["x"]
            delta_y = event.y - self._drag_data["y"]
            # muevo el objeto la distancia adecuada
            self.canvas.move(self._drag_data["item"], delta_x, delta_y)
            # guardo la posicion nueva
            self._drag_data["x"] = event.x
            self._drag_data["y"] = event.y

    # -----------------terminamos el drag & drop de las piezas -------

    # ----------- eventos del raton on/out over------------------------
    def pieza_esta_raton(self, coord_x, coord_y):
        col_tamano = fila_tamano = self.dim_casilla
        seleccionada_columna = coord_x // col_tamano
        seleccionada_fila = 7 - (coord_y // fila_tamano)
        pos = self.tablero.alfa_notacion((seleccionada_fila, seleccionada_columna))
        try:
            posibles_destinos = []
            for i in juego.moves({ 'verbose': True }):
                if i['from'] == pos:
                    posibles_destinos.append(i)
            return(posibles_destinos)
        except:
            pass
            
    #Funcion para casillas grises del tablero
    def entra_mouse_over(self, event):
        def casillas_grises(casilla):
            x1 = self.color_casillas_tablero[casilla]['x1']
            y1 = self.color_casillas_tablero[casilla]['y1']
            x2 = self.color_casillas_tablero[casilla]['x2']
            y2 = self.color_casillas_tablero[casilla]['y2']
            color = self.color_casillas_tablero[casilla]['color_con_sombra']
            #self.canvas.create_rectangle(x1, y1, x2, y2,  fill=color, tags="area")
            id_casilla = str(x1) + '-' + str(y1) + '-' + str(x2) + '-' + str(y2)
            self.canvas.itemconfig(id_casilla,  fill=color)
            #hemos quitado la pieza y ahora la ponemos
            x,y = self.tablero.num_notacion(self.posibles_jugadas[0]['from'])
            nom_fichero = "./piezas/%s%s.png" % (self.posibles_jugadas[0]['color'], self.posibles_jugadas[0]['piece'])
            if self.posibles_jugadas[0]['color'] == 'w' :
                nom_pieza = "%s%s%s" % (self.posibles_jugadas[0]['piece'].upper(), x, y)
            else:
                nom_pieza = "%s%s%s" % (self.posibles_jugadas[0]['piece'], x, y)
            self.canvas.delete(nom_pieza)
            if(nom_fichero not in self.imagenes):
                self.imagenes[nom_fichero] = PhotoImage(file=nom_fichero)
            self.obj_imagen = self.canvas.create_image(0,0, image=self.imagenes[nom_fichero], tags=(nom_pieza, "ocupada"), anchor="c")
            x0 = (y * self.dim_casilla) + int(self.dim_casilla/2)
            y0 = ((7-x) * self.dim_casilla) + int(self.dim_casilla/2)
            self.canvas.coords(nom_pieza, x0, y0)
            
        self.posibles_jugadas = self.pieza_esta_raton(event.x, event.y)
        if len(self.posibles_jugadas) > 0 :
            origen = self.posibles_jugadas[0]['from']
            casillas_grises(origen)
            for i in range(len(self.posibles_jugadas)):
                casillas_grises(self.posibles_jugadas[i]['to'])
            self.canvas.tag_bind(self.obj_imagen, "<Leave>", self.sale_mouse_over)
                    

    def sale_mouse_over(self, event):
        self.dibuja_tablero()
        self.dibuja_piezas()
        
    #---------------------------- fin de raton on/out over ------------------

#Funcion para iniciar interfaz grafica
def inicia_programa(posic_tablero):
    root = Tk()
    root.title("BeatChess")
    gui = BeatChess(root, posic_tablero)
    gui.dibuja_tablero()
    gui.dibuja_piezas()
    root.mainloop()


if __name__ == "__main__":
    #primero la posición inicial del tablero
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    # inicio el validador de jugadas con la posición inicial
    juego = ajedrez_parser.Chess(fen)
    if not juego:
        fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    # inicio el tablero interno grafico. El real se controla con ajedrez_parser
    partida = tablero.TableroAjedrez(fen, juego)

    inicia_programa(partida)
