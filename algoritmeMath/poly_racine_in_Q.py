import numpy as np
import fractions
import time

def diviseur(n):
    result = []

    for i in range(1,n//2 + 1):
        if n%i == 0:
            result.append(i)
    result.append(n)

    return result
'''
a faire:
-optimiser
'''
def racineInQ(poly):

    #initialisation variable
    coef = list(poly.c)
    if len(coef) == 1:
        return 'error'

    #ppmc des dénominateurs des float de coef
    listDenominator = []
    for c in coef:
        frac = fractions.Fraction(c).limit_denominator()    
        listDenominator.append(frac.denominator)
    ppmc = np.lcm.reduce(listDenominator)

    #mult poly par le ppmc pour que chaque coef soit des entier
    poly = poly * ppmc
    coef = list(poly.c.astype(int))

    #diviseur du premier et du dernier coefficient
    p = diviseur(abs(coef[-1]))
    q = diviseur(abs(coef[0]))

    #liste de tous les racine potancielle
    p,q = np.meshgrid(p,q)
    r = (p/q).flatten()
    r = np.concatenate((r,-r))

    #garder que les bonnes racines
    f_r = poly(r)
    racine = r[~f_r.astype(bool)]
    
    #trouver les multiplicités des racines
    result = {}
    enCours = True
    racine = list(set(racine))
    r = 0
    while enCours:
        rac = racine[r]
        test = poly/[1,-rac]
        if test[1][0] == 0:
            poly = test[0]
            if str(rac) in result:
                result[str(rac)] += 1
            else:
                result[str(rac)] = 1
        elif r >= len(racine)-1:
            enCours = False
        else:
            r += 1

    return result

t = time.time()
poly = np.poly1d([1,0,2,0])

poly_r = racineInQ(poly)
print(time.time()-t)
print(poly_r)