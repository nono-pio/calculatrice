from collections import Counter
from fractions import Fraction

from .roots_fonctions import *

class add(allFonction):
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
            elif isConstant([val]): dict_value['cte_func'].append(val)
            else: dict_value['variable'].append(val)
        
        #make coef of values
        dict_value['cte_func'] = Counter(dict_value['cte_func'])
        dict_value['variable'] = Counter(dict_value['variable'])
        
        #return in specials cases
        if len(dict_value['cte_func']) == 0 and len(dict_value['variable']) == 0:
            return dict_value['cte']

        #return to self
        self.dict_value = dict_value
        return self

    def reciproque_one_variable(self, membre_droite):
        membre_droite_temp = []
        for val in self.value:
            if not isConstant([val]):
                membre_gauche = val
            else:
                membre_droite_temp.append(val)
        membre_droite = add(membre_droite, product(-1,membre_droite_temp))
        return membre_gauche, membre_droite



class product(allFonction):
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
    
    def reduce(self):
        #cte = 1, 2, i   cte_func = 1/2, exp(3)   variable = x, x/exp(x)
        dict_value = {'cte':1,'cte_func':[],'variable':[]}
        
        #splits values
        for val in self.value:
            if type(val) in cte: dict_value['cte'] *= val
            elif isConstant([val]): dict_value['cte_func'].append(val)
            else: dict_value['variable'].append(val)
        
        #make coef of values
        dict_value['cte_func'] = Counter(dict_value['cte_func'])
        dict_value['variable'] = Counter(dict_value['variable'])
        
        #return in specials cases
        if len(dict_value['cte_func']) == 0 and len(dict_value['variable']) == 0:
            return dict_value['cte']
        elif dict_value['cte'] == 0:
            return 0

        #return to self
        self.dict_value = dict_value
        return self

class divide(allFonction):
    def __init__(self,nominator,denominator):
        self.nom = nominator
        self.den = denominator
        self.value = [nominator, denominator]

        self.isConstant = isConstant([nominator, denominator])
    
    def __str__(self) -> str:
        return str(self.nom) + "/" + str(self.den)
    
    def reduce(self):
        if self.den == 0: return ZeroDivisionError('Error n/0 is indefinded')
        elif self.den == 1: return self.nom
        elif self.isConstant:
            return Fraction(self.nom,self.den).limit_denominator().as_integer_ratio()

class power(allFonction):
    def __init__(self, base, pow):
        self.pow = pow
        self.base = base
        self.value = [base, pow]

        self.isConstant = isConstant([base, pow])
    
    def __str__(self) -> str:
        return str(self.base) + "^" + str(self.pow)
    
    def reduce(self):
        if self.base == self.pow == 0:
            return ArithmeticError('Error 0^0 is undefinded')
        elif self.base == 0:
            return 0
        elif self.base == 1:
            return 1
        elif self.pow == 0:
            return 1
        elif self.pow == 1:
            return self.base
        elif self.isConstant:
            return self.base ** self.pow