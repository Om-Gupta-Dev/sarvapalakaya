from django.shortcuts import render
from main.forms import QueryForm
from main.models import *


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def images(request):
    return render(request, 'main/images.html')


def donate(request):
    return render(request, 'main/donate.html')


def contact(request):
    cSubmit = False
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            cSubmit = True
        else:
            return render(request, 'main/contact.html', {'form': form, 'errors': form.errors})
    else:
        form = QueryForm()
    return render(request, 'main/contact.html', {'form': form, 'csubmit': cSubmit})


def bmember(request):
    return render(request, 'main/bmember.html')
