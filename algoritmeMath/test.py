from Fonction.classFonction import *
from equation import equation

mg = add('x',4)
md = 6

print(equation(mg, md)['x'])

x = add(6,product(-1,4))
print(x.reduce())