def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if prime(a[i]):
        c+=1
print(c)