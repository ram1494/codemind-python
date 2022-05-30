n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    if a[i]%2!=0:
        c=0
        for j in range(n):
            if a[i]==a[j]:
                c+=1
                if i!=j:
                    a[j]=0
        if a[i]%2!=0:
            s+=1
print(s)
            