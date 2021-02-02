from django.shortcuts import render


def index(request):
    """The Home Page for Learning Log"""

    return render(request, 'learning_logs/index.html')
