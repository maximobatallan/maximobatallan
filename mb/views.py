from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import formulario


# Create your views here.

def home(request):
    context = 'river'
    return render(request, "home.html", {'context': context})

def send_user_data_email(user_data):
    subject = 'Nuevo usuario maximobatallan.com'
    message = f'Nuevo Usuario de maximobatallan.com:\n\n{user_data}'
    

    from_email = 'notificaciondepaginaweb@gmail.com'
    recipient_list = ['notificaciondepaginaweb@gmail.com','maximobatallan@gmail.com']
    send_mail(subject, message, from_email, recipient_list)





def asistentevirtual(request):    
    
    return render(request, 'asistentevirtual.html')

def desarrollospersonalizados(request):    
    
    return render(request, 'desarrollospersonalizados.html')

def exposicionenlinea(request):    
    
    return render(request, 'exposicionenlinea.html')

def gestiondelainformacion(request):    
    
    return render(request, 'gestiondelainformacion.html')

def acercadeaev(request):    
    
    return render(request, 'acercadeaev.html')
