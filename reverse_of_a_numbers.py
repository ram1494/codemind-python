N=int(input())
re=0
t=N
while(t!=0):
    r=t%10
    re=re*10+r
    t=t//10
print(re)