import numpy as np

class Polynome():

    derivee = {}
    integrales = {}

    def __init__(self, poly):
        self.poly = poly
        self.coef = poly[1:]
        self.deg  = len(self.coef) - 1
        self.poly1d = np.poly1d(self.coef)
        self.o_o = self.coef[-1]
    
    def add(self, poly2):
        return (self.poly1d + poly2.poly1d).c
    
    def mult(self, poly2):
        return (self.poly1d * poly2.poly1d).c
    
    def racines(self, around=None):
        self.roots = self.poly1d.r
        if not around == None:
            self.roots = np.around(self.roots, around)
        return self.roots
    
    def ddx(self, n=1):
        self.derivee[str(n)] = Polynome(['poly'] + list(self.poly1d.deriv(n).c))
        return self.derivee[str(n)].coef
    
    def integrale(self, n=1):
        self.integrales[str(n)] = Polynome(['poly'] + list(self.poly1d.integ(n).c))
        return self.integrales[str(n)].coef