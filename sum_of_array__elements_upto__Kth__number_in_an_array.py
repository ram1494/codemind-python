n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in range(k):
    s=s+a[i]
print(s)