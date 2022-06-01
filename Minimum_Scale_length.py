n=int(input())
a=list(map(int,input().split()))
m=min(a)
while m!=0:
    c=0
    for i in range(n):
        if a[i]%m==0:
            c+=1
    if c==n:
        print(m)
        break
    m-=1
    