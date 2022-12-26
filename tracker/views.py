from django.shortcuts import render


def tracker_index(request):
    return render(request, 'tracker/index.html')


def tracker_dashboard(request):
    values = {1: '175.5', 2: '177.0', 3: '176.4', 4: '175.2', 5: '175.4', 6: '176.8', 7: '177.0'}
    return render(request, 'tracker/dashboard.html', {'values': values})
