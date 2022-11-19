from Fonction.classFonction import *

def equation(membre_gauche, membre_droite):
    result = {'x':[]}
    nb_variable = Counter(x=0)
    variable_gauche = False
    variable_droite = False

    if type(membre_gauche) not in cte:
        variable_gauche = True
        if membre_gauche == 'x':
            nb_variable.update('x')
        else:
            nb_variable.update(membre_gauche.nb_variable())
    
    if type(membre_droite) not in cte:
        variable_droite = True
        if membre_droite == 'x':
            nb_variable.update('x')
        else:
            nb_variable.update(membre_droite.nb_variable())

    if nb_variable['x'] == 1:
        if variable_droite == True:
            membre_droite, membre_gauche = membre_gauche, membre_droite
        
        while membre_gauche != 'x':
            print('en cours :', membre_gauche, '=', membre_droite)
            membre_gauche, membre_droite = membre_gauche.reciproque_one_variable(membre_droite)
        
        result['x'] = membre_droite

    return result