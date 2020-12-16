import tablero
import ajedrez_parser
from stockfish import Stockfish
stockfish = Stockfish("stockfish_20090216_x64.exe")


class Chess():
    cont = 0
    filas = 8
    columnas = 8
    # color1 = "#DDB88C"    #es la casilla blanca
    "color2 = "  # A66D4F"    #es la casilla oscura
    color1 = "#45e7a5"
    color2 = "#e75445"
    sombra_color1 = "#696969"
    sombra_color2 = "#A9A9A9"
    color_casillas_tablero = {}
    dim_casilla = 48  # 64
    imagenes = {}
    posibles_jugadas = []
    # para ejecutar los movimientos
    casilla_origen = None
    casilla_destino = None
    stockfish = Stockfish("stockfish_20090216_x64.exe")
    #stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 30})

    def __init__(self,posicion):
        self.tablero = posicion



    def moverse(self):
        while(True):
            print(juego.turno())
            print(juego.fen())
            self.imprimir()

            #Negras


            #Blancas
            if juego.turno() == 'w':
                self.casilla_origen = input('Origen: ')
                self.casilla_destino = input('Destino: ')
            else:
                print("negris")
                #self.stockfish.set_position(["e2e4", "e7e6"])
                self.stockfish.set_fen_position(juego.fen())
                print(self.stockfish.get_best_move())
                self.casilla_origen = input('Origen: ')
                self.casilla_destino = input('Destino: ')
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

    def imprimir(self):
        tablero= (['a8','b8','c8','d8','e8','f8','g8','h8'],['a7','b7','c7','d7','e7','f7','g7','h7'],
                       ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
                       ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
                       ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
                       ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
                       ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
                       ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
                       )

        for i in tablero:
            #print(i)
            for key in self.tablero:
                if (key, ":", self.tablero[key])[0] in i:
                    if (key, ":", self.tablero[key])[2]['color'] == 'w':
                        i[i.index((key, ":", self.tablero[key])[0])] =i[i.index((key, ":", self.tablero[key])[0])] +(key, ":", self.tablero[key])[2]['type']
                    else:
                        i[i.index((key, ":", self.tablero[key])[0])] = i[i.index((key, ":", self.tablero[key])[0])]+(key, ":", self.tablero[key])[2]['type'].upper()
            for j in range(8):
                if i[j][-1].isnumeric():
                    i[j] = i[j][1]+' -'
            print(i)

        """
        print(self.tablero)
        for key in self.tablero:
            print((key, ":", self.tablero[key])[2])
        """


def inicia_programa(posic_tablero):
    chess = Chess(posic_tablero)
    chess.moverse()



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


