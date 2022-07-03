I=list(map(int,input().split()))
n=len(I)
max1=0
max2=0
for i in range(0,n):
    if(max1<I[i]):
        max1=I[i]
        a=i
for i in range(0,n):
    if(max2<I[i] and i!=a):
        max2=I[i]
max1-=1
max2-=1
print(max1*max2)