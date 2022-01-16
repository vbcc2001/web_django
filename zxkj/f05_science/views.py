from django.shortcuts import render

def index(request):
    return render(request, 'f06_science/f01_index.html')
