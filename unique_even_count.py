n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    c=0
    for j in range(i,n):
        if i!=j and a[i]==a[j]:
            c+=1
    if c==0:
        if a[i]%2==0:
            s+=1
else:
    print(s)
            