def q1():
    x=int(raw_input("Digite um numero: "))
    z=x*2
    print ("O dobro desse numero é: %i") %z

def q2():
    r=int(raw_input("Digite o valor do Raio da Circunferencia: "))
    C=2*3.14*r
    print ("O valor do Comprimento da Circunferencia de Raio %.2f é: %.2f") %(r,C)

def q3():
    x=int(raw_input("Digite o valor do 1º angulo: "))
    y=int(raw_input("Digite o valor do 2º angulo: "))
    z=180-(x+y)
    print("O valor do 3º angulo eh: %i") %z

def q4():
    r=int(raw_input("Digite o valor do Raio da Esfera: "))
    V=((4*3.14)*r**3)/3
    print ("O valor do Volume da Esfera de Raio %.2f é: %.2f m³") %(r,V)

def q5():
    C=int(raw_input("Digite o valor da temperatura em graus Celsius: "))
    F=(180*(C+32))/100
    print ("A temperatura de %i graus Celsius equivale a %.2f graus Fahrenheit.") %(C,F)

def q6():
    x=int(raw_input("Digite o valor do 1 numero: "))
    y=int(raw_input("Digite o valor do 2 numero: "))
    z=int(raw_input("Digite o valor do 3 numero: "))
    med=(x+y+z)/3
    print ("A media aritmetica dos numeros %i, %i e %i é: %.2f") %(x,y,z,med)

def q7():
    n1=float(raw_input("Digite o valor da 1º Nota: "))
    n2=float(raw_input("Digite o valor da 2º Nota: "))
    m=((n1*4)+(n2*6))/10
    print(" A media ponderada eh: %.2f ") %m

def q8():
    x1=float(raw_input("Digite o valor da coordenada x1: "))
    x2=float(raw_input("Digite o valor da coordenada x2: "))
    y1=float(raw_input("Digite o valor da coordenada y1: "))
    y2=float(raw_input("Digite o valor da coordenada y2: "))
    d=(((x2-x1)**2+(y2-y1)**2)**0.5)
    print(" A distancia entre esses pontos eh: %.2f ") %d

def q9():
    c1=int(raw_input("Digite o valor do 1º Cateto: "))
    c2=int(raw_input("Digite o valor do 2º Cateto: "))
    h=((c1**2)+(c2**2))**0.5
    print ("O valor da hipotenusa é: %.2f") %h

def q10():
    x=input("Digite se deseja usar o tipo 1 ou 2: ")
    if x==1:
        sal=float(raw_input("Digite o valor do salário atual do funcionario: "))
        nsal=sal+(sal*0.25)
        print ("O Salario com aumento de 25 por cento do funcionario é: %.2f") %nsal
    elif x==2:
        sal=float(raw_input("Digite o valor do salário atual do funcionario: "))
        au=float(raw_input("Digite o percentual de aumento do salario do funcionario: "))
        nsal=sal+(sal*(au/100))
        print ("O Salario com aumento de %i por cento do funcionario é: %.2f") %(au,nsal)
    else:
        print ("Tipo invalido tente novamente.")
