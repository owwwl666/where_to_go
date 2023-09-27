from django.shortcuts import render


def display_message(request):
    return render(request, 'index.html')
