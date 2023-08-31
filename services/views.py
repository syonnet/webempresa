from django.shortcuts import render
from .models import Service
# Create your views here.
def services(request):
    services=Service.objects.all() #consulta para obtener la lista de servicios
    return render(request, 'services/services.html', {'listServices':services})