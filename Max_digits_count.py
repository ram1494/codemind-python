def dig(n):
    if n==0:
        return 1
    s=0
    while n!=0:
        i=n%10
        n=n//10
        s+=1
    return s
n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(dig(a[i]))
k=max(l)
print(l.count(k))