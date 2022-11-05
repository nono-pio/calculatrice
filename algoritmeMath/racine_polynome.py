import numpy as np
import math
import fractions
from poly_racine_in_Q import racineInQ

def casSpecials(poly,coefs,deg):
    if deg == 1: return -poly[0]/poly[1] # marche
    elif deg == 2: # marche pas
        delta = poly[1]**2 - 4*poly[2]*poly[0]
        x = []
        x.append((-poly[1]+delta**.5)/2*poly[2])
        x.append((-poly[1]-delta**.5)/2*poly[2])
        return x
    elif np.array(coefs[1:-2]).astype(bool).all() == False:# marche pas
        return pow(-poly[0]/poly[deg],1/deg)

    a = pow(poly[0],1/deg)
    if a != 'nan' and type(a) not in (int,float): # marche un peu
        patern = [math.comb(deg,i)*pow(a,i) for i in range(deg + 1)]
        if patern == coefs:
            return -a

def racine(poly):

    #initiation des variables
    coefs = list(poly.c)
    deg = len(coefs) - 1

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
    listRacines.append(casSpecials(poly,coefs,deg))


    return listRacines
print()
p = np.poly1d([1,2])
print(racine(p))