def q1():
    import math
    m=int(raw_input("Digite o valor do numero a ser verificado: "))
    n=int(raw_input("Digite o valor da base numerica: "))
    if math.fmod(m,n)==0:
        print ("O numero %i � multiplo do numero %i ") %(m,n)
    else:
        print ("O numero %i n�o � multiplo do numero %i ") %(m,n)

def q2():
    import math
    x=int(raw_input("Digite o valor do numero a ser verificado: "))
    if x<=0:
        y=x*-1
        print ("O valor absoluto do numero %i �: %i ") %(x,y)
    else:
        print ("O valor absoluto do numero %i � o pr�prio numero %i ") %(x,x)

def q3():
    import math
    a=int(raw_input("Digite o valor do primeiro numero: "))
    b=int(raw_input("Digite o valor do segundo numero: "))
    c=int(raw_input("Digite o valor do terceiro numero: "))
    maior, menor , meio = a, a, a
    if b > maior:
        maior = b
    if b < menor:
        menor = b
    if c > maior:
        maior = c
    if c < menor:
        menor = c
    if a <> maior and a <> menor:
        meio = a
    elif b <> maior and b <> menor:
        meio = b
    else:
        meio = c
    print ("O menor numero �: %i ") %menor
    print ("O numero do meio �: %i ") %meio
    print ("O maior numero �: %i ") %maior

def q4():
    import math
    print ("Seguindo o formato de equa��o do 2� Grau Ax�+Bx+C=0.")
    A=int(raw_input("Digite o valor de A: "))
    B=int(raw_input("Digite o valor de B: "))
    C=int(raw_input("Digite o valor de C: "))
    print ("Ser�o calculadas a raiz da equa��o a seguir: %ix�+%ix+%i=0.") %(A,B,C)
    D=(B**2)-(4*A*C)
    if D<0:
        print ("N�o existem ra�zes reais para essa equa��o.")
    else:
        X1=(-B+(D**0.5))/(2*A)
        X2=(-B-(D**0.5))/(2*A)
        print ("As ra�zes reais da equa��o %ix�+%ix+%i=0 s�o: %.2f e %.2f ") %(A,B,C,X1,X2)

def q5():
    import math
    S=(raw_input("Digite o seu sexo, sendo M para Masculino e F para Feminino: "))
    if S=='M':
        H=float(raw_input("Digite a sua altura em m: "))
        P=(72.7*H)-58
        print ("O peso ideal para esse individuo do sexo Masculino �: %.2f ") %P
    elif S=='F':
        H=float(raw_input("Digite a sua altura em cm: "))
        P=(62.1*H)-44.7
        print ("O peso ideal para esse individuo do sexo Feminino �: %.2f ") %P
    else:
        print ("Sexo inv�lido tente novamente.")

def q6():
    import math
    A=int(raw_input("Digite o comprimento do lado A: "))
    B=int(raw_input("Digite o comprimento do lado B: "))
    C=int(raw_input("Digite o comprimento do lado C: "))
    if A>=B+C:
        print ("Nenhum tri�ngulo foi formado.")
    elif A==(B**2+C**2)**0.5:
        print ("Foi formado um Tri�ngulo Ret�ngulo.")
    elif A>(B**2+C**2)**0.5:
        print ("Foi formado um Tri�ngulo Obtus�ngulo.")
    elif A<(B**2+C**2)**0.5:
        print ("Foi formado um Tri�ngulo Acut�ngulo.")
    else:
        print ("ERROR")

def q7():
    import math
    A=int(raw_input("Digite o valor do �ngulo a ser verificado: "))
    if A==0 or A==90 or A==180 or A==270 or A==360:
        print ("O angulo est� na linha de um dos 4 Quadrantes.")
    elif A<90:
        print ("O angulo est� no 1� Quadrante. ")
    elif A>90 and A<180:
        print ("O angulo est� no 2� Quadrante. ")
    elif A>180 and A<270:
        print ("O angulo est� no 3� Quadrante. ")
    elif A>270 and A<360:
        print ("O angulo est� no 4� Quadrante. ")
    else:
        print ("ERROR")

def q8():
    mes=int(raw_input("Digite o m�s a ser verificado: "))
    if mes>0 and mes<4:
        print("Este m�s pertence ao 1� Trimestre")
    elif mes>3 and mes<7:
        print("Este m�s pertence ao 2� Trimestre")
    elif mes>6 and mes<10:
        print("Este m�s pertence ao 3� Trimestre")
    elif mes>9 and mes<13:
        print("Este m�s pertence ao 4� Trimestre")
    else:
        print ("ERROR M�S INV�LIDO")
    
    
    
    
    
    
    
    
