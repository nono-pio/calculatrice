import numpy as np
import math
import fractions
from poly_racine_in_Q import racineInQ
from racine import rac

def casSpecials(poly,coefs,deg):
    #racine de polynome de degrée 1: -b/a
    if deg == 1:
        return -poly[0]/poly[1]
    #racine de polynome de degrée 2: (-b+-rac(b^2-4ac))/2a
    elif deg == 2:
        a, b, c = coefs
        delta = pow(b,2) - 4*a*c
        _bsur2a = -b/(2*a)
        if delta > 0:
            return [_bsur2a+pow(delta,.5)/(2*a),_bsur2a-pow(delta,.5)/(2*a)]
        elif delta == 0:
            return [_bsur2a]*2
        else:
            return [_bsur2a+1j*pow(-delta,.5)/(2*a),_bsur2a-1j*pow(-delta,.5)/(2*a)]
    #racine d'un polynome de la forme x^n+a: rac_n(-a)
    elif ~np.any(coefs[1:-2]):
        return list(rac(-poly[0]/poly[deg], n=deg ))

def racine(poly):

    #initiation des variables
    coefs = list(poly.c)
    deg = len(coefs) - 1
    listDeg = np.nonzero(coefs[::-1])[0]

    listRacines = []

    #transformer coefs en coefs entiers
    listDenominator = []
    for coef in coefs:
        frac = fractions.Fraction(coef).limit_denominator()    
        listDenominator.append(frac.denominator)
    ppmc = np.lcm.reduce(listDenominator)
    poly = poly * ppmc

    poly = poly/np.gcd.reduce(poly.c.astype(int))
    coefs = list(poly.c)
    
    #si cas spécials x^10-2  x-2x+4 deg=1,2
    rac = casSpecials(poly,coefs,deg)
    if rac != None:
        listRacines.append()

    #réduction du polynome
    #polynome facteur x x^2+x
    if listDeg[0]!=0:
        listRacines += [0] * listDeg[0]
        poly = (poly/([1]+[0]*listDeg[0]))[0]
    #change world x --> y
    if np.gcd.reduce(listDeg)!=0:
        action = {'world y':np.gcd.reduce(listDeg)}
        new_poly = list(poly.c)[::np.gcd.reduce(listDeg)]
        poly = np.poly1d(new_poly)
        print(action)
    #Théormème 1 div x-a/b racines dans l'ensemble Q En cours de test
    #racineDansQ, poly = racineInQ(poly)

    return listRacines, poly #, racineDansQ

p = np.poly1d([])
print(racine(p))