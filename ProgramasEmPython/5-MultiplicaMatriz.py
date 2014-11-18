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

def vetor():
    global vetor
    global n
    n=int(raw_input("Digite o tamanho do vetor: "))
    vetor=[]
    for i in range (n):
        A=int(raw_input("Digite o valor de i: "))
        vetor.append(A)
    print ("Finalizado.")
    return vetor
def busca():
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
        
    
    
