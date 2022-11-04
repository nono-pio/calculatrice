from django.shortcuts import render
from fonction.form import myForm

from compte.models import parametreGraph

import numpy as np

import plotly.graph_objects as go
def createDictFig(parametre, x, y):
    dict_fig = {
        "data": [{
                "type": "scatter",
                "x": x,
                "y": y}],
        
        "layout": {
            "title": {
                "text": "derivee de x^2",
                "x": 0.5,
                "font":{
                    "size":30,
                },
            },
            "paper_bgcolor":"rgba(0,0,0,0)",
            "plot_bgcolor":"rgba(0,0,0,0)",
        }
    }
    if parametre != 'defaut':
        dict_fig["layout"]["paper_bgcolor"] = parametre.backgroud_color
        dict_fig["layout"]["plot_bgcolor"] = parametre.backgroud_color

    return dict(dict_fig)

def create_graph(fx, x_deb, x_fin, precision=100, user=False):
    f = eval('lambda x: ' + str(fx))

    x = np.linspace(x_deb, x_fin, precision)
    y = f(x)
    
    if user.is_authenticated :
        try:
            paramGraph = parametreGraph.objects.get(user=user)
        except:
            dict_fig = createDictFig('defaut', x, y)
        else:
            dict_fig = createDictFig(paramGraph, x, y)
    else:
        dict_fig = createDictFig('defaut', x, y)

    fig = go.Figure(dict_fig)
    chart = fig.to_html()
    return chart



def fonction_view(request):

    user = request.user

    context = {
        'data':{}
    }

    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            x_deb = form.cleaned_data['x_deb']
            x_fin = form.cleaned_data['x_fin']
            fonction = form.cleaned_data['fonction_graph']

            context['data']['graph'] = create_graph(fonction, x_deb, x_fin, user=user)
    else :
        form = myForm()

    context['form'] = form

    return render(request,'fonction/fonction.html',context=context)
