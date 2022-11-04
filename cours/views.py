from django.shortcuts import render

def cours_view(request):
    return render(request,'cours/cours.html')
