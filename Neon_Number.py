a=int(input())
c=0
n=a**2
while n!=0:
    s=n%10
    c+=s
    n=n//10
if c==a:
    print("Neon Number")
else:
    print("Not Neon Number")
    