from django.shortcuts import render, redirect
import numpy as np
from algoritmeMath.classPolynome import Polynome

def createPolynome(poly):
    poly = ['poly'] + list(np.array(poly.split('-')).astype(float))
    poly = Polynome(poly)
    poly.racines(around=2)
    poly.ddx()
    poly.integrale()
    return poly


def polynome_view(request):
    context = {}
    
    if request.method == 'POST':
        input = request.POST['input']
        if input != "":
            return redirect('./returnpolynome/' + input)

    return render(request,'polynome/polynome.html', context=context)

#polynome: '1-2-1'  -->  ['poly',1,2,1]
def returnpolynome_view(request, polynome):
    polynome = createPolynome(polynome)

    context = {'polynome':polynome}
    return render(request, 'polynome/returnpolynome.html', context=context)

