def fx_isConstant(*args):
    for arg in args:
        ty = type(arg)
        if ty in (int,float):
            pass
        elif ty == str:
            if arg in ('x','y','t'):
                return False
        elif ty == list:
            if all([fx_isConstant(a) for a in arg]) == False:
                return False
        else:
            if arg.isConstant == False:
                return False
    return True

class baseFonction():
    def __add__(self,added):
        return add(self, added)

    def __iadd__(self, added):
        #self = add(self, added)
        pass

class add():
    def __init__(self, *args):
        result = []
        for arg in args:
            if type(arg) in (list,tuple):
                result += list(arg)
            else:
                result.append(arg)
        self.value = result

        self.isConstant = fx_isConstant(result)
    
    def __str__(self) -> str:
        result = [str(added) for added in self.value]
        return " + ".join(result)

class product():
    def __init__(self,*args):
        result = []
        for arg in args:
            if type(arg) in (list,tuple):
                result += list(arg)
            else:
                result.append(arg)
        self.value = result

        self.isConstant = fx_isConstant(result)
    
    def __str__(self) -> str:
        result = [str(prod) for prod in self.value]
        return " * ".join(result)

class divide():
    def __init__(self,nominator,denominator):
        self.nom = nominator
        self.den = denominator

        self.isConstant = fx_isConstant(nominator, denominator)
    
    def __str__(self) -> str:
        return str(self.nom) + "/" + str(self.den)

class power():
    def __init__(self, base, pow):
        self.pow = pow
        self.base = base

        self.isConstant = fx_isConstant(base, pow)
    
    def __str__(self) -> str:
        return str(self.base) + "^" + str(self.pow)

class exp(baseFonction):
    def __init__(self, x, base='e'):
        if base == 'e':
            self.x = x
        else:
            #return power(base,x)
            pass

        self.isConstant = fx_isConstant(x)
    
    def __str__(self) -> str:
        return "e ^ " + str(self.x)

class log(baseFonction):
    def __init__(self, x, base='e'):
        self.base = base
        self.x = x

        self.isConstant = fx_isConstant(base, x)
    
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