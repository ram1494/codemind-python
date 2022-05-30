n=int(input())
a=list(map(int,input().split()))
s=0
sum=0
l=[]
for i in range(n):
    c=0
    x=a[i]
    for j in range(n):
        if a[i]==a[j]:
            c+=1
    if c==x:
        l.append(a[i])
        s+=1
if s==0:
    print('-1')
else:
    print(min(l),max(l),end=' ')