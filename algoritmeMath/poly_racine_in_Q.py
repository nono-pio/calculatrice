import numpy as np

def diviseur(n):
    result = []

    for i in range(1,n//2 + 1):
        if n%i == 0:
            result.append(i)
    result.append(n)

    return result

def racineInQ(poly):

    #initialisation variable
    coef = list(poly.c)

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

    return result, poly