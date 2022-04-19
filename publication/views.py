from django.shortcuts import render

def publications(request):
    return render(request, 'publication/publications.html')
