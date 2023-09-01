from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Category (models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre de categoria')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering=['-created']
        
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    content=models.TextField(verbose_name='Contenido')
    published=models.DateTimeField(verbose_name='Fecha de publicacion', default=now)
    image=models.ImageField(verbose_name='Imagen',upload_to='blogs')
    author=models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category, verbose_name='categorias')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    
    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
        ordering=['title']
        
    def __str__(self):
        return self.title
