x=int(input())
for i in range(x):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for k in range(1,n):
        if a[k-1]>a[k]:
            c+=1
    if c==0:
        print(c)
    else:
        ma=max(a)
        mi=min(a)
        print(ma-mi)