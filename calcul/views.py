from django.shortcuts import render

def calcul_view(request):
    context = {}

    return render(request,'calcul/calcul.html', context = context)
