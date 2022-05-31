n=input()
word=n.split()
revwords=[w[::-1]for w in word]
ns=" ".join(revwords)
print(ns)
    