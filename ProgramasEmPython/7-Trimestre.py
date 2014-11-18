def tri(mes):
        if mes>0 and mes<4:
            print("primeiro trimestre")
        elif mes>3 and mes<7:
            print("segundo trimestre")
        elif mes>6 and mes<10:
            print("terceiro trimestre")
        elif mes>9 and mes<13:
            print("quarto trimestre")
        else:
            print ("valor errado")
 
def chamar():
    for i in range(1,13):
        tri(i)

def fat():
    x=1
    y=1
    z=1
    n=input("digite n")
    for i in range(1,n+1):
        x=x*i
    p=input("digite p")
    for i in range(1,p+1):
        y=y*i
    for i in range(1,(n-p)+1):
        z=z*i
    c=x/(y*z)
    print x
    print y
    print z
    print c


def funcao(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    return x

def flat():
    n=input('digite n')
    p=input('digite p')
    d=n-p
    c=funcao(n)/(funcao(p)*funcao(d))
    print c
    

