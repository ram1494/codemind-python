n=int(input())
I=list(map(int,input().split()))
b=[]
for i in I:
    if I.count(i)==1:
        b.append(i)
if len(b)!=0:
    print(*b)
else:
    print(-1)