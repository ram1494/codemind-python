import math
a,b,c=list(map(int,input().split()))
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
m=math.sqrt(d)
print(format(m,".2f"))