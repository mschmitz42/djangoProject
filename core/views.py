from django.shortcuts import render

def core_index(request):
    return render(request, 'core/index.html')

