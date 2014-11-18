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
