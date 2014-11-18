def q1():
    import math
    m=int(raw_input("Digite o valor do numero a ser verificado: "))
    n=int(raw_input("Digite o valor da base numerica: "))
    if math.fmod(m,n)==0:
        print ("O numero %i é multiplo do numero %i ") %(m,n)
    else:
        print ("O numero %i não é multiplo do numero %i ") %(m,n)

def q2():
    import math
    x=int(raw_input("Digite o valor do numero a ser verificado: "))
    if x<=0:
        y=x*-1
        print ("O valor absoluto do numero %i é: %i ") %(x,y)
    else:
        print ("O valor absoluto do numero %i é o próprio numero %i ") %(x,x)

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
    print ("O menor numero é: %i ") %menor
    print ("O numero do meio é: %i ") %meio
    print ("O maior numero é: %i ") %maior

def q4():
    import math
    print ("Seguindo o formato de equação do 2º Grau Ax²+Bx+C=0.")
    A=int(raw_input("Digite o valor de A: "))
    B=int(raw_input("Digite o valor de B: "))
    C=int(raw_input("Digite o valor de C: "))
    print ("Serão calculadas a raiz da equação a seguir: %ix²+%ix+%i=0.") %(A,B,C)
    D=(B**2)-(4*A*C)
    if D<0:
        print ("Não existem raízes reais para essa equação.")
    else:
        X1=(-B+(D**0.5))/(2*A)
        X2=(-B-(D**0.5))/(2*A)
        print ("As raízes reais da equação %ix²+%ix+%i=0 são: %.2f e %.2f ") %(A,B,C,X1,X2)

def q5():
    import math
    S=(raw_input("Digite o seu sexo, sendo M para Masculino e F para Feminino: "))
    if S=='M':
        H=float(raw_input("Digite a sua altura em m: "))
        P=(72.7*H)-58
        print ("O peso ideal para esse individuo do sexo Masculino é: %.2f ") %P
    elif S=='F':
        H=float(raw_input("Digite a sua altura em cm: "))
        P=(62.1*H)-44.7
        print ("O peso ideal para esse individuo do sexo Feminino é: %.2f ") %P
    else:
        print ("Sexo inválido tente novamente.")

def q6():
    import math
    A=int(raw_input("Digite o comprimento do lado A: "))
    B=int(raw_input("Digite o comprimento do lado B: "))
    C=int(raw_input("Digite o comprimento do lado C: "))
    if A>=B+C:
        print ("Nenhum triângulo foi formado.")
    elif A==(B**2+C**2)**0.5:
        print ("Foi formado um Triângulo Retângulo.")
    elif A>(B**2+C**2)**0.5:
        print ("Foi formado um Triângulo Obtusângulo.")
    elif A<(B**2+C**2)**0.5:
        print ("Foi formado um Triângulo Acutângulo.")
    else:
        print ("ERROR")

def q7():
    import math
    A=int(raw_input("Digite o valor do Ângulo a ser verificado: "))
    if A==0 or A==90 or A==180 or A==270 or A==360:
        print ("O angulo está na linha de um dos 4 Quadrantes.")
    elif A<90:
        print ("O angulo está no 1º Quadrante. ")
    elif A>90 and A<180:
        print ("O angulo está no 2º Quadrante. ")
    elif A>180 and A<270:
        print ("O angulo está no 3º Quadrante. ")
    elif A>270 and A<360:
        print ("O angulo está no 4º Quadrante. ")
    else:
        print ("ERROR")

def q8():
    mes=int(raw_input("Digite o mês a ser verificado: "))
    if mes>0 and mes<4:
        print("Este mês pertence ao 1º Trimestre")
    elif mes>3 and mes<7:
        print("Este mês pertence ao 2º Trimestre")
    elif mes>6 and mes<10:
        print("Este mês pertence ao 3º Trimestre")
    elif mes>9 and mes<13:
        print("Este mês pertence ao 4º Trimestre")
    else:
        print ("ERROR MÊS INVÁLIDO")
    
    
    
    
    
    
    
    
