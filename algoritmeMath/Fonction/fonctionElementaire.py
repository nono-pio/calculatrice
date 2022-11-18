from collections import Counter
from .function_annexe import *

class add():
    def __init__(self, *args):
        result = []
        for arg in args:
            if type(arg) in (list,tuple):
                result += list(arg)
            else:
                result.append(arg)
        self.value = result

        self.isConstant = isConstant(result)
    
    def __str__(self) -> str:
        result = [str(added) for added in self.value]
        return " + ".join(result)

    def reduce(self):
        #cte = 1, 2, i   cte_func = 1/2, exp(3)   variable = x, x/exp(x)
        dict_value = {'cte':0,'cte_func':[],'variable':[]}
        
        #splits values
        for val in self.value:
            if type(val) in cte: dict_value['cte'] += val
            elif isConstant(val): dict_value['cte_func'].append(val)
            else: dict_value['variable'].append(val)
        
        #make coef of values
        dict_value['cte_func'] = Counter(dict_value['cte_func'])
        dict_value['variable'] = Counter(dict_value['variable'])
        
        #return in specials cases
        if len(dict_value['cte_func']) == 0 and len(dict_value['variable']) == 0:
            return dict_value['cte']

        #return to self
        self.dict_value = dict_value
        return dict_value

class product():
    def __init__(self,*args):
        result = []
        for arg in args:
            if type(arg) in (list,tuple):
                result += list(arg)
            else:
                result.append(arg)
        self.value = result

        self.isConstant = isConstant(result)
    
    def __str__(self) -> str:
        result = [str(prod) for prod in self.value]
        return " * ".join(result)

class divide():
    def __init__(self,nominator,denominator):
        self.nom = nominator
        self.den = denominator

        self.isConstant = isConstant([nominator, denominator])
    
    def __str__(self) -> str:
        return str(self.nom) + "/" + str(self.den)

class power():
    def __init__(self, base, pow):
        self.pow = pow
        self.base = base

        self.isConstant = isConstant([base, pow])
    
    def __str__(self) -> str:
        return str(self.base) + "^" + str(self.pow)