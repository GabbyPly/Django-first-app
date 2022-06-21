from django.shortcuts import render

# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render


def goto(request):
    context = {}
    return render(request, "phonebook/goto.html", context)


def homepage(request):
    context = {}
    return render(request, "phonebook/index.html", context)
