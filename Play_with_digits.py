def dig(n):
    if n==0:
        return 1
    s=0
    while n!=0:
        i=n%10
        n=n//10
        s=s+i
    return s
n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s=s+dig(a[i])
print(s)