n=int(input())
a=list(map(int,input().split()))
s=0
l=[]
for i in range(n):
    c=0
    for j in range(n):
        if a[i]==a[j]:
            c+=1
            if i!=j:
                a[j]=0
    if a[i]==c:
        print(a[i],end=' ')
        s+=1
if s==0:
    print('-1')