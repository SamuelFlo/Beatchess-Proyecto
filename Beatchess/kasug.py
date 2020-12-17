import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

import chess.pgn
from google.colab import drive

model0 = train_1_neuron()


model1 = train_2_neuron(0)
model2 = train_2_neuron(1)
model3 = train_2_neuron(2)
model4 = train_2_neuron(3)
model5 = train_2_neuron(4)
model6 = train_2_neuron(5)

    #pawn    
    #knight    
    #bishop    
    #king    
    #queen    
    #rook


#fen = "r2qkbnr/npp3pp/5p2/p2Pp3/3P2b1/2NB1N1P/PPP2PP1/R1BQK2R w KQkq e6 0 8"

for _ in range(2):
  fen = input("FEN: ")  
  Y = np.array(VectorizeFen(fen),"float32")
  actual = model0.predict(Y.reshape(1,64))
  actual_coord = manrique(actual)
  pieza = getPieceIn(actual_coord,fen)
  print("NICOLLE",actual_coord)
  print("NICOLLE",fen)
  if pieza == 0:
    code = piece_encoded([Y],0)
    dest = model1.predict(Y.reshape(1,64))
  elif pieza == 1:
    code = piece_encoded([Y],1)
    dest = model2.predict(Y.reshape(1,64))
  elif pieza == 2:
    code = piece_encoded([Y],2)
    dest = model3.predict(Y.reshape(1,64))
  elif pieza == 3:
    code = piece_encoded([Y],3)
    dest = model4.predict(Y.reshape(1,64))
  elif pieza == 4:
    code = piece_encoded([Y],4)
    dest = model5.predict(Y.reshape(1,64))
  elif pieza == 5:
    code = piece_encoded([Y],5)
    dest = model6.predict(Y.reshape(1,64))
  else:
    pass
  dest_coord = manrique(dest)

  print(dest_coord)
  #code = piece_encoded([Y],2)
  #hola = model2.predict(np.array(code,"float32").reshape(1,64))
#model2.fix()

#model0




def manrique(matriz):
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

    lista=[]
    for i in range(len(matriz)) :
        for j in range(len(matriz[0])):
            lista.append(matriz[i][j])

    mayor=max(lista)
    #print(mayor)
    #print(matriz.index(mayor))

    for i in range(len(matriz)) :
        for j in range(len(matriz[0])):
            if matriz[i][j] == mayor:                
                return tablero[i][j]
                
def getPieceIn(position, fen):
    i, j = toNumeric(position)
    j = 7 - j
    trim = fen.split()
    board = trim[0].split('/')
    for _, char in enumerate(board[j]):
        if char.isnumeric():
            if i == 0:
                return getPieceVal(char)
            i -= int(char)
            if i < 0:
                return 0
        if i == 0:
            return getPieceVal(char)
        i -= 1

def getPieceVal(char):
    if char == 'P':
        return 0
    if char == 'p':
        return 0
    if char == 'N':
        return 1
    if char == 'n':
        return 1
    if char == 'B':
        return 2
    if char == 'b':
        return 2
    if char == 'K':
        return 3
    if char == 'k':
        return 3
    if char == 'Q':
        return 4
    if char == 'q':
        return 4
    if char == 'R':
        return 5
    if char == 'r':
        return 5
    return 0

def toNumeric(position):
    i = -1
    if position[0] == 'a':
        i = 0
    elif position[0] == 'b':
        i = 1
    elif position[0] == 'c':
        i = 2
    elif position[0] == 'd':
        i = 3
    elif position[0] == 'e':
        i = 4
    elif position[0] == 'f':
        i = 5
    elif position[0] == 'g':
        i = 6
    elif position[0] == 'h':
        i = 7
    return i, int(position[1]) - 1

def train_1_neuron():
  X,Y = load_data("Fischer.pgn",0)

  model = Sequential()
  model.add(Dense(16, input_dim=64, activation='relu'))
  model.add(Dense(64, activation='relu'))

  model.compile(loss='mean_squared_error',
                optimizer='adam',
                metrics=['binary_accuracy'])
  X = np.array(X,"float32")
  Y = np.array(Y,"float32")

  #print(X.shape)

  model.fit(X, Y, epochs=100)

  #print(model.predict(X[0].reshape(1,64)))
  return model

def train_2_neuron(piece):
  X,Y = load_data("Fischer.pgn",1)
  if piece == 0:
    #pawn
    X = piece_encoded(X,1)  
  elif piece == 1:
    #knight
    X = piece_encoded(X,2)  
  elif piece == 2:
    #bishop
    X = piece_encoded(X,3)  
  elif piece == 3:
    #king
    X = piece_encoded(X,100)  
  elif piece == 4:
    #queen
    X = piece_encoded(X,9)  
  elif piece == 5:
    #rook
    X = piece_encoded(X,5)

  model = Sequential()
  model.add(Dense(16, input_dim=64, activation='relu'))
  model.add(Dense(64, activation='softmax'))
  #optimizer = runai.ga.keras.optimizers.Adam(steps=STEPS)
  model.compile(loss='mean_squared_error',
                optimizer='adam',
                metrics=['binary_accuracy'])
  X = np.array(X,"float32")
  Y = np.array(Y,"float32")


  #print(X.shape)

  model.fit(X, Y, epochs=100)  
  #model.fit(X1, Y1, epochs=2)

  #print(model.predict(X[0].reshape(1,64)))
  return model

def load_data(file_name,flag):
  pgn = open("/content/gdrive/My Drive/chess/"+file_name)
  games = []
  cont = 0
  while chess.pgn.read_game(pgn):
    game = chess.pgn.read_game(pgn)
    games.append(game)
      
    #for move in game.main_line():
    board = game.board()
    dataset_X = []
    dataset_Y = []
    for move in game.main_line():
      temp = code_board(board)
      
      board.push(move)
      if flag:
        val = code_output(move,0)
      else:
        val = code_output(move,1)
      dataset_X.append(temp)
      dataset_Y.append(val)
                            
    cont += 1
    if cont == 5:
      break
  return dataset_X,dataset_Y

def VectorizeFen(fen):
    ret_val = []
    fen = fen.replace('/', '')
    for char in fen.split()[0]:
        if char.isnumeric():
            ret_val += [0 for _ in range(int(char))]
            continue
        ret_val += [f'{getPieceVal(char)}']
    return ret_val

def getPieceVal(char):
  if char == 'P':
      return 1
  if char == 'p':
      return -1
  if char == 'N':
      return 2
  if char == 'n':
      return -2
  if char == 'B':
      return 3
  if char == 'b':
      return -3
  if char == 'K':
      return 100
  if char == 'k':
      return -100
  if char == 'Q':
      return 9
  if char == 'q':
      return -9
  if char == 'R':
      return 5
  if char == 'r':
      return -5
  return 0
    
def piece_encoded(data,value):
  
  temp = []
  for val in data:
    temp1 = []
    for i in range(len(val)):
      if val[i] == value:
        temp1.append(1)
      elif val[i] == -value:
        temp1.append(-1)
      else:
        temp1.append(0)
    temp.append(temp1)
  return temp

def code_board(board):  
  temp = VectorizeFen(str(board.fen()))
  return np.array(temp).reshape(64)
  

def code_output(move,flag):  
  board = []
  if flag == 0:
    pos1 = str(move)[:1]
    pos2 = str(move)[1:2]
  else:
    pos1 = str(move)[2:3]
    pos2 = str(move)[3:4]

  pos1 = get_val(pos1)
  pos2 = get_val(pos2)

  for i in range(8):
    board.append([0,0,0,0,0,0,0,0])
  board[pos1][pos2] = 200
  return np.array(board).reshape(64)

def get_val(pos):
  
  if pos == 'a':
    temp = 0
  elif pos == 'b':
    temp = 1
  elif pos == 'c':
    temp = 2
  elif pos == 'd':
    temp = 3
  elif pos == 'e':
    temp = 4
  elif pos == 'f':
    temp = 5
  elif pos == 'g':
    temp = 6
  elif pos == 'h':
    temp = 7
  else:
    temp = 8-int(pos)
  
  return int(temp)