def vetor():
    print ("Inicializando.")
    exemplo=[7,8,8,9,9]
    for i in range (0,5):
        print exemplo[i]
    print ("Finalizado.")

def vetor2():
    print ("Inicializando.")
    vet1=[]
    for i in range (5):
        vet1.append(1)
    print vet1
    print ("Finalizado.")

def vetor3():
    print ("Inicizalizando.")
    vet2=[0]*5
    print vet2
    print ("Finalizado.")

def vetor4():
    n=5
    print ("Inicializando.")
    vet4=[None for i in range (n)]
    print vet4
    print ("Finalizado.")

def matriz():
    print ("Inicializando.")
    mat1=[]
    for i in range (4):
        mat1.append([0]*5)
    print mat1    
    print ("Finalizado.")

## NAO FUNCIONA ESSE MÉTODO
def matriz2():
    mat2=0
    for i in range (m):
        for j in range (n):
            mat2[i][j]=0
    print mat2
## BEM MELHOR UTILIZAR ESSE MÉTODO
def matriz3(lin,col):
    mat1=[[0 for j in range(col)] for i in range(lin)]
    print mat1

def matriz4():
    mat[i,j]=int(raw_input("Entre com o valor: "))
    print mat

def matrix(lin,col):
    matrix=[[0 for j in range(col)]for i in range(lin)]
    for i in range(0,lin):
        for j in range (0,col):
            matrix[i][j]=int(raw_input("Digite o valor: "))
    print matrix
    
    
