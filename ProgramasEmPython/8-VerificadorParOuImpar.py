def vet():
    vet=[0]*5
    i=0
    while i<=4:
        x=0
        while x==0:
            n=input("digite um numero impar")
            x=n % 2
            if x==0:
                print("tem q ser impar")
            else:
                vet[i]=n
        i=i+1
    k=3
    i=0
    while i<=4:
        j=0
        while j<=k:
            if vet[j]<vet[j+1]:
                aux=vet[j]
                vet[j]=vet[j+1]
                vet[j+1]=aux
            j=j+1
        i=i+1
    print vet
    


def par():
    vet=[0]*5
    i=0
    while i<=4:
        x=1
        while x!=0:
            n=input("digite um numero par")
            x=n % 2
            if x!=0:
                print("tem q ser par")
            else:
                vet[i]=n
        i=i+1
    print vet
        
