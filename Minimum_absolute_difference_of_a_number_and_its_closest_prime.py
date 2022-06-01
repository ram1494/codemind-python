def prime(n):
    i=2
    c=0
    while i!=n:
        if n%i==0:
            c=1
        i+=1
    if c==0:
        return n
n=int(input())
temp=n
for i in range(n,2-1,-1):
    if prime(i):
        b=i
        break
while temp!=0:
    if prime(temp):
        p=temp
        break
    temp+=1
if (n-b)<(p-n):
    print(abs(b-n))
elif (n-b)==(p-n):
    print(abs(b-n))
else:
    print(abs(p-n))
        