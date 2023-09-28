from django.shortcuts import render

# Create your views here.
def taisia(request):
    return render(request, "taisia/taisia.html")