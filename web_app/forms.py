from django import forms
from django.forms import ModelForm
from web_app.models import ContactForm

class ContactoForm2(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=150, label='Apellido')
    email = forms.EmailField(help_text="Ej: a@b.com", label='Email')
    fec_nac = forms.DateField(help_text="yyyy-mm-dd", label='Fecha de Nacimiento')
    comentario = forms.CharField(widget=forms.Textarea({"size": 100}), label="Comentario")

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(help_text="Ej: a@b.com", label='Email', widget=forms.TextInput(attrs={'placeholder': 'Indique su Email'}))
    customer_name = forms.CharField(max_length=64, label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Indique su nombre'}))
    message = forms.CharField(widget=forms.Textarea({"size": 100}), label="Mensaje")
    
class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message'] 
form = ContactFormModelForm()
    
contactForm = ContactForm.objects.get(pk=1)
form = ContactFormModelForm(instance=ContactForm)