a=int(input())#1124
p=1
s=0
while a>0:
    x=a%10    
    a=a//10
    s+=x
    p*=x
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')
