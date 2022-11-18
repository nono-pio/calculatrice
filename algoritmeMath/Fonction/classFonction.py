from .fonctionElementaire import *
from .function_annexe import *

class baseFonction():
    def __add__(self,added):
        return add(self, added)

    def __iadd__(self, added):
        return add(self, added)
    
    def __mul__(self, timed):
        return product(self, timed)
    
    def __imul__(self, timed):
        return product(self, timed)
    
    def __div__(self, divided):
        return divide(self, divided)
    
    def __idiv__(self, divided):
        return divide(self, divided)
    
    def __pow__(self, pow):
        return power(self, pow)
    
    def __ipow__(self, pow):
        return power(self, pow)
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return product(-1,self)

class exp(baseFonction):
    def __init__(self, x, base='e'):
        if base == 'e':
            self.x = x
        else:
            #return power(base,x)
            pass

        self.isConstant = isConstant(x)
    
    def __str__(self) -> str:
        return "e ^ " + str(self.x)

class log(baseFonction):
    def __init__(self, x, base='e'):
        self.base = base
        self.x = x

        self.isConstant = isConstant([base, x])
    
    def __str__(self) -> str:
        if self.base == 'e':
            return f"ln({ self.x })"
        else:
            return f"log_{self.base}({ self.x })"

class sin(baseFonction):
    def __init__(self, x):
        self.x = x
    
    def __str__(self) -> str:
        return f"sin({ self.x })"

class cos(baseFonction):
    def __init__(self, x):
        self.x = x
    
    def __str__(self) -> str:
        return f"cos({ self.x })"

class tan(baseFonction):
    def __init__(self, x):
        self.x = x
    
    def __str__(self) -> str:
        return f"tan({ self.x })"

class sinh(baseFonction):
    def __init__(self, x):
        self.x = x
    
    def __str__(self) -> str:
        return f"sinh({ self.x })"

class cosh(baseFonction):
    def __init__(self, x):
        self.x = x
    
    def __str__(self) -> str:
        return f"cosh({ self.x })"

class tanh(baseFonction):
    def __init__(self, x):
        self.x = x
    
    def __str__(self) -> str:
        return f"tanh({ self.x })"

class summa(baseFonction):
    def __init__(self, fonction, variable='k', start=None, end=None):
        self.fonction = fonction
        self.start = start
        self.end = end
        self.variable = variable
    
    def __init__(self):
        result = "sum"
        if self.start != None:
            result += f"_{self.variable}={self.start}"
        if self.end != None:
            result += f"^{self.end}"
        return result + " " + str(self.fonction)