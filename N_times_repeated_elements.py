n=int(input())
a=list(map(int,input().split()))
x=int(input())
s=0
for i in range(n):
    c=0
    for j in range(n):
        if a[i]==a[j]:
            c+=1
            if i!=j:
                a[j]=0
    if x==c and a[i]!=0:
        print(a[i],end=' ')
        s+=1
if s==0:
    print('-1')