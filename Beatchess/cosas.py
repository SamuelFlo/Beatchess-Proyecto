import numpy as np
import chess
import ajedrez_parser



def manrique(matriz,flag,fen,actual_coord):
    matriz = np.array(matriz)
    matriz= np.reshape(matriz, (8, 8))


    tablero = [['a8','b8','c8','d8','e8','f8','g8','h8'],
               ['a7','b7','c7','d7','e7','f7','g7','h7'],
               ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
               ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
               ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
               ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
               ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
               ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]

    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista.append(matriz[i][j])
    mayor = max(lista)

    destino =""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == mayor:
                destino = tablero[i][j]
                print(tablero[i][j])

    if flag == False:
        validar = chess.Board(fen)
        while True:
            lista2=[]
            for i in range(len(matriz)):
                for j in range(len(matriz[0])):
                    lista2.append(matriz[i][j])
            if validar.piece_at(lista2.index(mayor)) == None:
                lista.remove(mayor)
                mayor = max(lista)
            else:
                break

        destino = ""
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == mayor:
                    destino = tablero[i][j]
        return destino

    else:
        validar = chess.Board(fen)
        temp=actual_coord+destino

        while(True):

            if temp in list(validar.legal_moves):
                return destino
            else:
                print(lista)
                lista.remove(mayor)
                mayor = max(lista)
                destino = ""
                for i in range(len(matriz)):
                    for j in range(len(matriz[0])):
                        if matriz[i][j] == mayor:
                            destino = tablero[i][j]
                temp = actual_coord + destino





fen ='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
validar = chess.Board(fen)


#print(validar.is_valid())
#print(list(validar.legal_moves)[0])



tabla = [0.0,0.0,10.081891,0.0,1.0717113,6.5872235,1.2839801,0.0,0.2597109,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.740542,0.0,9.780632,0.0,9.16845,0.0,0.0,0.0,9.106034,11.39261,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.105505,0.0,0.0,0.0,0.0,1.0692577,0.0,0.0,7.7582064,13.645159,0.0,0.0,0.0,0.0,5.8120003,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.38639724,0.0,0.0]
tabla = np.array(tabla)
tabla=np.reshape(tabla, (8, 8))

#matriz
tabla2= [0.017370926,0.01746935,0.013658523,0.013658523,0.013658523,0.013658523,0.017509738,0.017373424,0.017394653,0.01741622,0.013658523,0.013658523,0.013658523,0.013658523,0.013658523,0.01742359,0.0175301,0.018773364,0.013658523,0.01717045,0.013658523,0.013658523,0.013658523,0.01736059,0.01741218,0.018218346,0.017473226,0.013658523,0.017509576,0.013658523,0.017132394,0.017085196,0.017514238,0.017437417,0.013658523,0.013658523,0.013658523,0.013658523,0.017385833,0.018780282,0.017584823,0.013658523,0.017030263,0.013658523,0.017192885,0.018342866,0.017253814,0.01744257,0.018347744,0.01758658,0.013658523,0.017354771,0.013658523,0.013658523,0.013658523,0.018568767,0.013658523,0.013658523,0.017481137,0.013658523,0.013658523,0.013658523,0.013658523,0.013658523]

#Fen
fen ='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

#flag
flag = True

#actual_coordenada
actual_coordenada = "e2"


#manrique(tabla2,flag,fen,actual_coordenada)




#fen = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1', 'rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2', 'rnbqkb1r/pppppppp/5n2/4P3/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2', 'rnbqkb1r/pppppppp/8/4P3/4n3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 3', 'rnbqkb1r/pppppppp/8/4P3/4n3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 2 3', 'r1bqkb1r/pppppppp/2n5/4P3/4n3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 3 4', 'r1bqkb1r/pppppppp/2n5/4P3/4n3/5N2/PPPPBPPP/RNBQK2R b KQkq - 4 4', 'r1bqkb1r/pppp1ppp/2n1p3/4P3/4n3/5N2/PPPPBPPP/RNBQK2R w KQkq - 0 5', 'r1bqkb1r/pppp1ppp/2n1p3/4P3/4n3/5N2/PPPPBPPP/RNBQ1RK1 b kq - 1 5', 'r1bqk2r/pppp1ppp/2n1p3/2b1P3/4n3/5N2/PPPPBPPP/RNBQ1RK1 w kq - 2 6', 'r1bqk2r/pppp1ppp/2n1p3/2b1P3/4n3/3P1N2/PPP1BPPP/RNBQ1RK1 b kq - 0 6', 'r1bqk2r/pppp1ppp/2n1p3/4P3/4n3/3P1N2/PPP1BbPP/RNBQ1RK1 w kq - 0 7', 'r1bqk2r/pppp1ppp/2n1p3/4P3/4n3/3P1N2/PPP1BRPP/RNBQ2K1 b kq - 0 7', 'r1bqk2r/pppp1ppp/2n1p3/4P3/8/3P1N2/PPP1BnPP/RNBQ2K1 w kq - 0 8', 'r1bqk2r/pppp1ppp/2n1p3/4P3/8/3P1N2/PPP1BKPP/RNBQ4 b kq - 0 8', 'r1bq1rk1/pppp1ppp/2n1p3/4P3/8/3P1N2/PPP1BKPP/RNBQ4 w - - 1 9', 'r1bq1rk1/pppp1ppp/2n1p3/4P3/8/2NP1N2/PPP1BKPP/R1BQ4 b - - 2 9', 'r1bqr1k1/pppp1ppp/2n1p3/4P3/8/2NP1N2/PPP1BKPP/R1BQ4 w - - 3 10', 'r1bqr1k1/pppp1ppp/2n1p3/4P3/4N3/3P1N2/PPP1BKPP/R1BQ4 b - - 4 10', 'r1b1r1k1/ppppqppp/2n1p3/4P3/4N3/3P1N2/PPP1BKPP/R1BQ4 w - - 5 11', 'r1b1r1k1/ppppqppp/2n1p3/4P3/4N3/2PP1N2/PP2BKPP/R1BQ4 b - - 0 11', 'r1br2k1/ppppqppp/2n1p3/4P3/4N3/2PP1N2/PP2BKPP/R1BQ4 w - - 1 12', 'r1br2k1/ppppqppp/2n1p3/4P3/4N3/2PP1N2/PP2B1PP/R1BQK3 b - - 2 12', 'r1b1r1k1/ppppqppp/2n1p3/4P3/4N3/2PP1N2/PP2B1PP/R1BQK3 w - - 3 13', 'r1b1r1k1/ppppqppp/2n1p3/4P3/8/2PP1NN1/PP2B1PP/R1BQK3 b - - 4 13', 'r1b1r1k1/pppp1ppp/2n1p3/2q1P3/8/2PP1NN1/PP2B1PP/R1BQK3 w - - 5 14', 'r1b1r1k1/pppp1ppp/2n1p3/2q1P3/3P4/2P2NN1/PP2B1PP/R1BQK3 b - - 0 14', 'r1b1r1k1/pppp1ppp/2n1p3/3qP3/3P4/2P2NN1/PP2B1PP/R1BQK3 w - - 1 15', 'r1b1r1k1/pppp1ppp/2n1p3/3qP3/3P4/2P2NN1/PP2BKPP/R1BQ4 b - - 2 15', 'r1b1r1k1/ppp2ppp/2npp3/3qP3/3P4/2P2NN1/PP2BKPP/R1BQ4 w - - 0 16', 'r1b1r1k1/ppp2ppp/2npp3/3qP3/3P4/2P2NNP/PP2BKP1/R1BQ4 b - - 0 16', 'r1b1r1k1/ppp2ppp/2n1p3/3qp3/3P4/2P2NNP/PP2BKP1/R1BQ4 w - - 0 17', 'r1b1r1k1/ppp2ppp/2n1p3/3qP3/8/2P2NNP/PP2BKP1/R1BQ4 b - - 0 17', 'r1b1r1k1/ppp2ppp/4p3/3qn3/8/2P2NNP/PP2BKP1/R1BQ4 w - - 0 18', 'r1b1r1k1/ppp2ppp/4p3/3Qn3/8/2P2NNP/PP2BKP1/R1B5 b - - 0 18', 'r1b1r1k1/ppp2ppp/8/3pn3/8/2P2NNP/PP2BKP1/R1B5 w - - 0 19', 'r1b1r1k1/ppp2ppp/8/3pn3/5B2/2P2NNP/PP2BKP1/R7 b - - 1 19', 'r1b1r1k1/ppp2ppp/6n1/3p4/5B2/2P2NNP/PP2BKP1/R7 w - - 2 20', 'r1b1r1k1/ppB2ppp/6n1/3p4/8/2P2NNP/PP2BKP1/R7 b - - 0 20', 'r1b3k1/ppB1rppp/6n1/3p4/8/2P2NNP/PP2BKP1/R7 w - - 1 21', 'r1bB2k1/pp2rppp/6n1/3p4/8/2P2NNP/PP2BKP1/R7 b - - 2 21', 'r1bBr1k1/pp3ppp/6n1/3p4/8/2P2NNP/PP2BKP1/R7 w - - 3 22', 'r1b1r1k1/ppB2ppp/6n1/3p4/8/2P2NNP/PP2BKP1/R7 b - - 4 22', 'r1b3k1/ppB1rppp/6n1/3p4/8/2P2NNP/PP2BKP1/R7 w - - 5 23', 'r1b3k1/pp2rppp/3B2n1/3p4/8/2P2NNP/PP2BKP1/R7 b - - 6 23', 'r1b3k1/pp3ppp/3Br1n1/3p4/8/2P2NNP/PP2BKP1/R7 w - - 7 24', 'r1b3k1/pp3ppp/3Br1n1/3p1N2/8/2P2N1P/PP2BKP1/R7 b - - 8 24', 'r5k1/pp1b1ppp/3Br1n1/3p1N2/8/2P2N1P/PP2BKP1/R7 w - - 9 25', 'r5k1/pp1b1ppp/3Br1n1/3p1N2/6P1/2P2N1P/PP2BK2/R7 b - g3 0 25', 'r5k1/pp3ppp/2bBr1n1/3p1N2/6P1/2P2N1P/PP2BK2/R7 w - - 1 26', 'r5k1/pp3ppp/2bBr1n1/3p1N2/6P1/2P2N1P/PP2BK2/5R2 b - - 2 26', '4r1k1/pp3ppp/2bBr1n1/3p1N2/6P1/2P2N1P/PP2BK2/5R2 w - - 3 27', '4r1k1/pp3ppp/2bBr1n1/3p1N2/6P1/2P2N1P/PP2BK2/4R3 b - - 4 27', '4r1k1/pp3ppp/2bB2n1/3p1N2/6P1/2P2N1P/PP2rK2/4R3 w - - 0 28', '4r1k1/pp3ppp/2bB2n1/3p1N2/6P1/2P2N1P/PP2RK2/8 b - - 0 28', '3r2k1/pp3ppp/2bB2n1/3p1N2/6P1/2P2N1P/PP2RK2/8 w - - 1 29', '3r2k1/ppB2ppp/2b3n1/3p1N2/6P1/2P2N1P/PP2RK2/8 b - - 2 29', '2r3k1/ppB2ppp/2b3n1/3p1N2/6P1/2P2N1P/PP2RK2/8 w - - 3 30', '2r3k1/ppB1Nppp/2b3n1/3p4/6P1/2P2N1P/PP2RK2/8 b - - 4 30', '2r3k1/ppB1nppp/2b5/3p4/6P1/2P2N1P/PP2RK2/8 w - - 0 31', '2r3k1/ppB1Rppp/2b5/3p4/6P1/2P2N1P/PP3K2/8 b - - 0 31', '2r3k1/ppB1Rppp/2b5/8/3p2P1/2P2N1P/PP3K2/8 w - - 0 32', '2r3k1/pp2Rppp/2b5/8/3p1BP1/2P2N1P/PP3K2/8 b - - 1 32', '2r2k2/pp2Rppp/2b5/8/3p1BP1/2P2N1P/PP3K2/8 w - - 2 33', '2r2k2/pp3ppp/2b5/8/3p1BP1/2P2N1P/PP2RK2/8 b - - 3 33', '2r2k2/pp3ppp/8/8/3p1BP1/2P2b1P/PP2RK2/8 w - - 0 34', '2r2k2/pp3ppp/3B4/8/3p2P1/2P2b1P/PP2RK2/8 b - - 1 34', '2r3k1/pp3ppp/3B4/8/3p2P1/2P2b1P/PP2RK2/8 w - - 2 35', '2r3k1/pp3ppp/3B4/8/3p2P1/2P2K1P/PP2R3/8 b - - 0 35', '3r2k1/pp3ppp/3B4/8/3p2P1/2P2K1P/PP2R3/8 w - - 1 36', '3r2k1/pp3ppp/8/8/3p2P1/2P2KBP/PP2R3/8 b - - 2 36', '3r2k1/pp3ppp/8/8/6P1/2Pp1KBP/PP2R3/8 w - - 0 37', '3r2k1/pp3ppp/8/8/6P1/2Pp1KBP/PP4R1/8 b - - 1 37', '3r2k1/pp3ppp/8/8/6P1/2P2KBP/PP1p2R1/8 w - - 0 38', '3r2k1/pp3ppp/8/8/5KP1/2P3BP/PP1p2R1/8 b - - 1 38', '3r2k1/pp3ppp/8/8/5KP1/2P3BP/PP4R1/3q4 w - - 0 39', '3r2k1/pp3ppp/8/8/6P1/2P1K1BP/PP4R1/3q4 b - - 1 39', '6k1/pp3ppp/8/8/6P1/2PrK1BP/PP4R1/3q4 w - - 2 40', '6k1/pp3ppp/8/8/4K1P1/2Pr2BP/PP4R1/3q4 b - - 3 40', '6k1/pp3ppp/8/8/4K1P1/2Pr1qBP/PP4R1/8 w - - 4 41', '6k1/pp3ppp/8/4K3/6P1/2Pr1qBP/PP4R1/8 b - - 5 41', '6k1/pp3ppp/8/3qK3/6P1/2Pr2BP/PP4R1/8 w - - 6 42', '6k1/pp3ppp/8/3q4/5KP1/2Pr2BP/PP4R1/8 b - - 7 42', '6k1/pp3p1p/8/3q2p1/5KP1/2Pr2BP/PP4R1/8 w - g6 0 43', '6k1/pp3p1p/8/3q2p1/5KP1/2Pr2BP/PP4R1/8 w - g6 0 43']
fen ='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
validar = chess.Board(fen)
print(validar.piece_at(34))


#vector, tablero, flag true blancas
#blancas hace 0 negativas