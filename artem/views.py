from django.shortcuts import render

# Create your views here.
def artem(request):
    return render(request, "artem/artem.html")