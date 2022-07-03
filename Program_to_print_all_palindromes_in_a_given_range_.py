m=int(input())
n=int(input())
for i in range(m,n+1):
    a=i
    b=0
    while(a!=0):
        rem=a%10
        a=int(a/10)
        b=b*10+rem
    if(i==b):
        print(i,end=' ')