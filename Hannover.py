def move(n,a,b,c):
    if(n==1):
        print(a,"-->",c,end='',)
        print(", next")
        return
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)

move(6,'a','b','c')