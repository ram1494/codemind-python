def pal(n):
    rev=0
    while n!=0:
        i=n%10
        rev=rev*10+i
        n=n//10
    return rev
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if pal(a[i]):
        print(pal(a[i]),end=' ')