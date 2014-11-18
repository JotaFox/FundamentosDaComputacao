def calculaDobro():
    x=int(raw_input("Digite o valor ao qual deseja dobrar: "))
    y=x*2
    return y


def areaCircunferencia():
    r=int(raw_input("Digite o valor do RAIO da circunferencia: "))
    C=(2*3.14*r)
    return C


def angulosTriangulo():
    x=int(raw_input("Digite o valor do 1º angulo: "))
    y=int(raw_input("Digite o valor do 2º angulo: "))
    z=180-(x+y)
    print("O valor do 3º angulo eh: %i") %z


def volumeEsfera():
    x=int(raw_input("Digite o valor do raio da esfera: "))
    V=(4*3.14*x**3)/3
    print ("O volume da esfera e: %r") %V


def conversorCelsiusToHeit():
    print("Este programa eh um conversor de temperatura CELSIUS para HEIT")
    C=float(raw_input("Digite a temperatura em graus CELSIUS: "))
    F=(180*(C+32))/100
    print("A temperatura de %.2f  equivale a %.2f  graus HEIT. ") %(C, F)

def calculaDist():
    print("Este programa calcula a distancia entre dois pontos.")
    x1=float(raw_input("Digite o valor da coordenada x1: "))
    x2=float(raw_input("Digite o valor da coordenada x2: "))
    y1=float(raw_input("Digite o valor da coordenada y1: "))
    y2=float(raw_input("Digite o valor da coordenada y2: "))
    d=(((x2-x1)**2+(y2-y1)**2)**0.5)
    print(" A distancia entre esses pontos eh: %.2f ") %d


def mediaPonderada():
    print("Este programa calcula a MEDIA PONDERADA de dois valores.")
    n1=float(raw_input("Digite o valor da 1º Nota: "))
    n2=float(raw_input("Digite o valor da 2º Nota: "))
    m=((n1*4)+(n2*6))/10
    print(" A media ponderada eh: %.2f ") %m


      


