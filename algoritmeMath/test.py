from Fonction.classFonction import *
from collections import Counter

a = add(1,2).reduce()
b = product(1,0).reduce()
c = divide('x',0).reduce()
d = power(8,8).reduce()

print(a,b,c,d)