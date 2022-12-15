from django.shortcuts import render


def tracker_index(request):
    return render(request, 'tracker/index.html')


def tracker_dashboard(request):
    return render(request, 'tracker/dashboard.html')
