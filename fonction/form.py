from django.forms import *

class myForm(Form):
    fonction_graph = CharField(label='fonction_graph', max_length=100)
    x_deb = FloatField(label='x_deb')
    x_fin = FloatField(label='x_fin')