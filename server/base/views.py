from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def navigate(request):
    context = {}
    return render(request, "base/index.html", context)


# Create your views here.
