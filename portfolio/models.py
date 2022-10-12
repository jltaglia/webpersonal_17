from email.mime import image
from tabnanny import verbose
from django.db import models

# Create your models here.

class Project(models.Model):
    title       = models.CharField(max_length=100, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'descripcion')
    image       = models.ImageField(upload_to='projects', verbose_name = 'imagen')
    created     = models.DateTimeField(auto_now_add= True, verbose_name = 'fecha creado')
    updated     = models.DateTimeField(auto_now= True, verbose_name = 'fecha modificado')
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']
           
    def __str__(self):
        return self.title
    