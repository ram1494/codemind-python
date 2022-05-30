n=int(input())
a=list(map(int,input().split()))
s=0
sum=0
for i in range(n):
    c=0
    for j in range(n):
        if a[i]==a[j]:
            c+=1
            if i!=j:
                a[j]=0
    if a[i]==c:
        s+=1
else:
    print(s)