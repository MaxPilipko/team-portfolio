from django.shortcuts import render

# Create your views here.
def egor(request):
    return render(request, "egor/egor.html")