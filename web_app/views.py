from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from web_app.forms import ContactoForm2, ContactFormForm, ContactFormModelForm
from web_app.models import Flan, ContactForm, ContactFormModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request=request, template_name='index.html', context={'flanes_publicos':flanes_publicos})

def acerca(request):
    return render(request=request, template_name='about.html', context={})

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request=request, template_name='welcome.html', context={'flanes_privados':flanes_privados})

def base(request):
#    return render(request=request, template_name='base.html', context={})
    return render(request=request, template_name='contenedor.html', context={})

def contacto(request):
    if request.method == 'POST':
        contacto_form = ContactFormForm(request.POST)
        if contacto_form.is_valid():
            data_contacto = contacto_form.cleaned_data
            #Guardemos el contacto
            return render(request, "custom/mensaje.html", {"mensaje":"Gracias por contactarte con OnlyFlans, te responderemos en breve"})
    
    contacto_form = ContactFormForm()
    return render(request, "contacto.html", { 'form':contacto_form })

def contacto2(request):
    if request.method == 'POST':
        contacto_form = ContactFormModelForm(request.POST)
        if contacto_form.is_valid():
            data_contacto = contacto_form.cleaned_data
            #Guardemos el contacto
            return render(request, "custom/mensaje.html", {"mensaje":"Gracias por contactarte con OnlyFlans, te responderemos en breve"})
    
    contacto_form = ContactFormModelForm()
    return render(request, "contacto.html", { 'form':contacto_form })
    
def obtener_flanes(request):
    flanes = Flan.objects.all()
    return render(request, "index.html", {'flanes': flanes})
    
def salir(request):
    logout(request)
    return redirect('/')

