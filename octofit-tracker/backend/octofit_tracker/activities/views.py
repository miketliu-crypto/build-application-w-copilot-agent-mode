from django.shortcuts import render


# Placeholder views for activities app

def index(request):
    return render(request, 'activities/index.html', {})
