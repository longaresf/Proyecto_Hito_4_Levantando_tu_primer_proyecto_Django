from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader


# Create your views here.

def principal(request):
    return render(request=request, template_name='principal.html', context={})