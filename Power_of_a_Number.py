a,b,c=map(int,input().split())
m=1
for i in range(0,b):
    m=m*a
print(m%c)