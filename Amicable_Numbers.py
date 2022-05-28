n=int(input())
n1=int(input())
s=0
s1=0
for i in range(1,n):
    if n%i==0:
        s+=i
for j in range(1,n1):
    if n1%j==0:
        s1+=i
if s==n1 or s1==n :
    print('Amicable')
else:
    print('Not Amicable')