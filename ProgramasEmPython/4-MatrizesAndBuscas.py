def mat1(m,p):
    global A
    A=[[0 for j in range(p)]for i in range(m)]
    for i in range (0,m):
        for j in range (0,p):
            print ("Estamos na posicao linha %i e coluna %i") %(i,j)
            A[i][j]=int(raw_input("Digite o valor da matriz: "))
    return A

def mat2(p,n):
    global B
    B=[[0 for j in range(n)]for i in range(p)]
    for i in range (0,p):
        for j in range (0,n):
            print ("Estamos na posicao linha %i e coluna %i") %(i,j)
            B[i][j]=int(raw_input("Digite o valor da matriz: "))
    return B

def mult(m,n):
    global A, B, C
    p=2
    C=[[0 for j in range(n)]for i in range(m)]
    for i in range (0,m):
        for j in range (0,n):
            C[i][j]=0
            for k in range (0,p):
                C[i][j]=C[i][j]+A[i][k]*B[k][j]
    return C
#############################################################
def vetor():                                                #
    global vetor                                            #
    global n                                                #
    n=int(raw_input("Digite o tamanho do vetor: "))         #
    vetor=[]                                                #
    for i in range (n):                                     #
        A=str(raw_input("Digite o valor de i: "))           #
        vetor.append(A)                                     #
    print ("Finalizado.")                                   #
    return vetor                                            #
#############################################################

##busca sequencial
def buscaS():
    valor=int(raw_input("Digite o valor a ser buscado: "))
    i=0
    achei=0
    while i<n and achei==0:
        if vetor[i]==valor:
            achei=1
        i=i+1
    if achei==0:
        print ("Valor não encontrado.")
    else:
        print ("Valor encontrado na posição %i") %i
        
##selection
def sel():
    for i in range (0,n):
        menor=i
        for j in range (i+1,n):
            if vetor[j]<vetor[menor]:
                menor=j
        aux=vetor[menor]
        vetor[menor]=vetor[i]
        vetor[i]=aux
        print vetor

##inserction
def ins():
    for i in range(1,n):
        x=vetor[i]
        j=i
        while j>0 and vetor[j-2]>x:
            vetor[j]=vetor[j-2]
            j=j-2
        vetor[j]=x
        print vetor

##bubble
def bub():
    k=n-2
    for i in range(0,n):
        j=0
        while j<=k:
            if vetor[j]>vetor[j+1]:
                aux=vetor[j]
                vetor[j]=vetor[j+1]
                vetor[j+1]=aux
            j=j+1
    print vetor

##Criação de Matrizes
def matrix(lin,col):
    matrix=[[0 for j in range(col)]for i in range(lin)]
    for i in range(0,lin):
        for j in range (0,col):
            matrix[i][j]=int(raw_input("Digite o valor: "))
    print matrix
    
