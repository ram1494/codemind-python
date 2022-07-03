n=input()
a=len(n)
for i in range(0,a):
    b=n.count(n[i])
    if(b==1):
        print(i)
        break
else:
    print("-1")