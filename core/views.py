from django.shortcuts import render

def core_index(request):
    return render(request, 'core/index.html')


def core_about(request):
    return render(request, 'core/about.html')


def core_scheduler(request):
    return render(request, 'core/under-construction.html')


def core_profile(request):
    return render(request, 'core/under-construction.html')
