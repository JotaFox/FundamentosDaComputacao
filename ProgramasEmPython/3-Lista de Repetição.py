def q1():
    import math
    s=0
    for i in range (1,101):
        s=s+i
        print ("O programa est� rodando pela %i vez.") %i
        print ("A soma atual dos n�meros est� em %i") %s

def q2():
    import math
    s=0
    a=0
    for i in range (1,201):
        if i%2==0:
            s=s+i
            a=a+1
            print ("O programa est� rodando pela %i vez.") %a
            print ("A soma atual dos n�meros est� em %i") %s
        else:
            print (".")

def q3():
    import math
    s=0
    a=0
    for i in range (1,151):
        if i%5==0:
            s=s+i
            a=a+1
            print ("O numero %i � m�ltiplo de 5 e est� sendo somado.") %i
            print ("O programa est� rodando pela %i vez.") %a
            print ("A soma est� atualmente em %i.") %s
        else:
            print (".")

def q4():
    import math
    t=0
    ch=0
    sh=0
    maior=0
    for i in range (1,6):
        m=int(raw_input("Digite o mes de aniversario da pessoa: "))
        h=int(raw_input("Digite a altura dessa pessoa: "))
        if m==1 or m==2 or m==3:
            t=t+1
        if h<150:
            ch=ch+1
        if h>maior:
           maior=h
        sh=sh+h
    med=sh/5 
    print ("O numero de pessoas que fazem niver no primeiro trimestre �: %i")%t
    print ("O numero de pessoas maiores do que 150cm �: %.2f")%ch
    print ("A m�dia das alturas inseridas �: %.2f")%med
    print ("A maior altura informada �: %.2f")%maior

def q5():
    import math
    n=int(raw_input("Digite quantos alunos ir�o usar o sistema: "))
    for i in range (1,n+1):
        mat=int(raw_input("Digite a matr�cula de 12 n�meros: "))
        n1=float(raw_input("Digite a primeira nota do aluno: "))
        n2=float(raw_input("Digite a segunda nota do aluno: "))
        med=(n1+n2)/2
        if med>=7:
            print(" ")
            print ("O aluno de matricula %i foi APROVADO com m�dia igual a: %.2f") %(mat,med)
            print(" ")
        elif med<4:
            print(" ")
            print ("O aluno de matricula %i foi REPROVADO com m�dia igual a: %.2f") %(mat,med)
            print(" ")
        else:
            print(" ")
            print ("O aluno de matricula %i foi  para a PROVA FINAL com m�dia igual a: %.2f") %(mat,med)
            print(" ")

def q6():
    import math
        
            
            
        
        
    
        
    
