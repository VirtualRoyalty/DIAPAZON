import numpy as np
import sys

x_len=y_len=3

board = np.zeros((x_len,y_len)) 
sample_board=np.zeros((x_len,y_len))
sample_board[0][0]=1 #д
sample_board[0][1]=2 #и
sample_board[0][2]=3 #а
sample_board[1][0]=4 #п
sample_board[1][1]=3 #а
sample_board[1][2]=5 #з
sample_board[2][0]=6 #о
sample_board[2][1]=7 #н
sample_board[2][2]=0 #_
print(sample_board)
print("  ")

board=copy.copy(sample_board)
mov=     ['d','u','r','l']
for x in range(100):
    i=np.random.randint(0,4)
    if(movepossbl(board,mov[i])):
        board=move_to(board,mov[i])
    else:
        continue
#board[0][0]=0 #д
#board[0][1]=7 #и
#board[0][2]=6 #а
#board[1][0]=5 #п
#board[1][1]=3 #а
#board[1][2]=4 #з
#board[2][0]=3 #о
#board[2][1]=2 #н
#board[2][2]=1 #_

print(board)
print("start___________")
def BFS(sample_board_,board_):#поиск в ширину
    V=copy.copy(sample_board_)
    open_=[['NULL',[],V]]
    close_=[]
    last_mov=''
    if(EQUEL(board_,sample_board_)):
        print("WE DID IT!in just",len(close_),"moves")
        return
    while (len(open_)>0): 
        print(len(close_))
        V=open_.pop(0)
        listofmovs=movsOF(V,inversmov(V[0]))
        close_.append(V[-1])
        for v in listofmovs:
            if(isthere(close_,v[-1])==False):
                if(EQUEL(board_,v[-1])):
                    print("WE DID IT!!!")
                    print(v[-1])
                    count=0
                    while(v[0]!='NULL'):
                        print(v[1][-1], "______")
                        v=v[1]
                        count+=1
                    print("in just",count,"moves")
                    return
                open_.append([v[0],V,v[-1]])
    print('There is no solution :(')
    return False

            
EQUEL(sample_board,board)   
BFS(sample_board,board)


import collections
import copy


def swap(board_,i,j): #меняет два элемента местами
    ix,iy=find_elem(board_,i)
    jx,jy=find_elem(board_,j)
    board_[ix][iy]=j
    board_[jx][jy]=i
    return
    
 


def EQUEL(sample_board_,board_): 
    for i in range(len(board_)):
         for j in range(len(board_)):
            if(sample_board_[i][j]!=board_[i][j]):
                return False
    return True 

def find_elem(board_,elem_):  #ищет данный элемент и возвращает координаты
    for x in range(len(board_)):
        for y in  range(len(board_)):
            if board_[x][y]==elem_:
                elem_x=x
                elem_y=y
                break
    return elem_x,elem_y


   

def movepossbl(board_,where): #проверяет возможен ли данный ход
    zery,zerx=find_elem(board_,0)
    if(zerx==len(board_)-1)&(where=='r'):
        return False
    if(zerx==0)&(where=='l'):
        return False
    if(zery==len(board_)-1)&(where=='d'):
        return False
    if(zery==0)&(where=='u'):
        return False
    return True


def isthere(lst,elem):#проверяет принадлежность вершины(данной доски) к списку
    for x in lst:
        if(EQUEL(x,elem)):
            return True
    return False
    
def movsOF(board_,last_mov):#создает массив возвожных ходов
    mov=['d','u','r','l']
    stop_mov=['u','d','l','r']
    moveslst=[]
    for i in [0,1,2,3]:
        if(movepossbl(board_[-1],mov[i])):
            if(mov[i]!=last_mov):
                moveslst.append([mov[i],board_,move_to(board_[-1],mov[i])])
    return moveslst       


  
    
def move_to(l,where):#двигаем ноль вверх или вниз или влево или вправо
    board_=copy.copy(l)
    zerox,zeroy=find_elem(board_,0)
    movex=[1,-1,0,0]
    movey=[0,0,1,-1]
    board_=copy.copy(l)
    if (zerox!=0)&(where == 'u'):
        swap(board_,0,board_[zerox+movex[1],zeroy+movey[1]])
        #print('U')
        return board_
    if (zerox!=len(board_)-1)&(where == 'd'):
        swap(board_,0,board_[zerox+movex[0],zeroy+movey[0]])
       # print('D')
        return board_
    if (zeroy!=0)&(where == 'l'):
        swap(board_,0,board_[zerox+movex[3],zeroy+movey[3]])
      #  print('L')
        return board_
    if (zeroy!=len(board_)-1)&(where == 'r'):
        swap(board_,0,board_[zerox+movex[2],zeroy+movey[2]])
       # print('R')
        return board_
    print('imposible move')
    return []

def inversmov(mov_): #"переворачивает" ход
    if(mov_=='u'):
        return 'd'
    if(mov_=='d'):
        return 'u'
    if(mov_=='l'):
        return 'r'
    if(mov_=='r'):
        return 'l'
    return mov_
