s=input().lower()
I=s.split()
k=[]
w=list(I[0])
I.remove(I[0])
f=1
for i in w:
    for j in I:
        if i not in j:
            f=0
            break
    else:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    print(''.join(k))