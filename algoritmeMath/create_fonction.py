import plotly.graph_objects as go
import numpy as np

'''
listFonction:
- polynome: [{'polynome':polynome(poly1d), 'racineReel':[], 'o_o':<int>},ddx(poly1d),inte(poly1d)]
'''

def createFonction(type, listFonction ,parametre='default', x_deb=-10, x_fin=10, precision=200):
    
    dict_fig = {
        "data": [],
        "layout": {
            "title": {
                "text": "",
                "x": 0.5,
                "font":{
                    "size":30,
                },
            },
            "paper_bgcolor":"rgba(0,0,0,0)",
            "plot_bgcolor":"rgba(0,0,0,0)",
        }
    }

    if parametre != 'default':
        dict_fig["layout"]["paper_bgcolor"] = parametre.backgroud_color
        dict_fig["layout"]["plot_bgcolor"] = parametre.backgroud_color
    
    match type:
        case 'polynome':
            x = np.linspace(x_deb, x_fin, precision)
            y = listFonction[0]['polynome'](x)
            dict_fig["data"].append({'type':'scatter', 'x':x, 'y':y})

            y_ddx = listFonction[1](x)
            dict_fig["data"].append({'type':'scatter', 'x':x, 'y':y_ddx})

            y_integrale = listFonction[2](x)
            dict_fig["data"].append({'type':'scatter', 'x':x, 'y':y_integrale})

    fig = go.Figure(dict(dict_fig))
    #return fig.to_html()
    return fig

poly = np.poly1d([1,2,1])
listFonction = [{'polynome':poly},poly.deriv(),poly.integ()]

fig = createFonction('polynome',listFonction)
fig.show()