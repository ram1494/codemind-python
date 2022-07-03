import math
n=int(input())
a=list(map(int,input().split()))
I=[]
for i in range(0,len(a)):
    sq=int(math.sqrt(a[i]))
    if sq*sq==a[i]:
        I.append(a[i])
print(sum(I))