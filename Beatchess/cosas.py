import numpy as np



def manrique(matriz):

    tablero = [['a8','b8','c8','d8','e8','f8','g8','h8'],
               ['a7','b7','c7','d7','e7','f7','g7','h7'],
               ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
               ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
               ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
               ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
               ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
               ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]

    lista=[]
    for i in range(len(matriz)) :
        for j in range(len(matriz[0])):
            lista.append(matriz[i][j])

    mayor=max(lista)
    print(mayor)
    #print(matriz.index(mayor))

    for i in range(len(matriz)) :
        for j in range(len(matriz[0])):
            if matriz[i][j] == mayor:
                print(tablero[i][j])


tabla = [0.0,0.0,10.081891,0.0,1.0717113,6.5872235,1.2839801,0.0,0.2597109,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.740542,0.0,9.780632,0.0,9.16845,0.0,0.0,0.0,9.106034,11.39261,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.105505,0.0,0.0,0.0,0.0,1.0692577,0.0,0.0,7.7582064,13.645159,0.0,0.0,0.0,0.0,5.8120003,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.38639724,0.0,0.0]
tabla = np.array(tabla)
tabla=np.reshape(tabla, (8, 8))
tabla2= [0.017370926,0.01746935,0.013658523,0.013658523,0.013658523,0.013658523,0.017509738,0.017373424,0.017394653,0.01741622,0.013658523,0.013658523,0.013658523,0.013658523,0.013658523,0.01742359,0.0175301,0.018773364,0.013658523,0.01717045,0.013658523,0.013658523,0.013658523,0.01736059,0.01741218,0.018218346,0.017473226,0.013658523,0.017509576,0.013658523,0.017132394,0.017085196,0.017514238,0.017437417,0.013658523,0.013658523,0.013658523,0.013658523,0.017385833,0.018780282,0.017584823,0.013658523,0.017030263,0.013658523,0.017192885,0.018342866,0.017253814,0.01744257,0.018347744,0.01758658,0.013658523,0.017354771,0.013658523,0.013658523,0.013658523,0.018568767,0.013658523,0.013658523,0.017481137,0.013658523,0.013658523,0.013658523,0.013658523,0.013658523]
print(len(tabla[0]))
tabla2 = np.array(tabla2)
tabla2=np.reshape(tabla2, (8,8))

manrique(tabla2)