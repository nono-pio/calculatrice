'''
Objectif: Transphormer input str en language python
Exemple: 'sin(x)x' ==> 'np.sin(x)*x'
'''


def formPython(data):
    data = str(data)
    contient = []
    result = ''

    translate = {
        'sin': 'np.sin',
        'cos': 'np.cos',
        'tan': 'np.tan',
        '^': '**',
    }       

    return contient, result, data

data = 'sin(x) * x * cos(y)'
print(formPython(data))