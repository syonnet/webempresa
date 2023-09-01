from django.db import models

# Create your models here.

class Social(models.Model):
    key=models.SlugField(verbose_name='Nombre clave', max_length=50, unique=True)
    name=models.CharField(verbose_name='Red social', max_length=50)
    url=models.URLField(verbose_name='Enlace', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    
    
    class Meta:
        verbose_name='Red Social'
        verbose_name_plural='Redes Sociales'
        ordering=['name']
        
    def __str__(self):
        return self.name
        
    