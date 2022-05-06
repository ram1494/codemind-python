x=input()
c=0
v=0
s=0
n=0
for i in x:
    if i=='A' or i=='E' or i=='I' or i =='O' or i=='U' or i=='a' or i=='e' or i=='i' or i =='o' or i=='u':
        c+=1
    elif i>='0' and i<='9' :
        n+=1
    elif i==" ":
        s+=1
    else:
        v+=1
print('Vowels:',c)
print('Consonants:',v)
print('Digits:',n)
print('White spaces:',s)
