s=input()
x=s.split()
l=[]
for i in x:
    v=sum(letter in 'aeiou' for letter in i.lower())
    l.append(v)
print(l.count(min(l)))