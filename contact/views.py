from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    # print('Tipo de peticion:{}'.format(request.method))
    #instancias
    contactForm=ContactForm()
    if request.method=='POST':
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            
            email=EmailMessage(
                'La cafettiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribio:\n\n{}'.format(name,email,message),
                'correo-prueba@inbox.mailtrap.io',
                ['vic_gen@hotmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')
        
    return render(request, 'contact/contact.html', {'contactForm' :contactForm})

