from django.shortcuts import render
from django.http import HttpResponse
from django.forms import *

import numpy as np

import plotly.graph_objects as go

def createGraphique():
    f = lambda x: x**2
    fPrime = lambda x: 2*x

    x = np.linspace(-10,10,200)
    y = f(x)
    yPrime = fPrime(x)

    dict_fig = dict({
        "data": [{
                "type": "scatter",
                "x": x,
                "y": y},
            {
                "type": "scatter",
                "x": x,
                "y": yPrime
            }],
        
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
    })

    fig = go.Figure(dict_fig)
    chart = fig.to_html()
    return chart

def derivee_view(request):
    context = {}
    return render(request,'derivee/derivee.html',context=context)

def deriveeReturn_view(request):
    context = {
        'data': {}
    }
    
    fig = createGraphique()
    context['data']['graph'] = fig

    return render(request,'derivee/deriveereturn.html',context=context)
