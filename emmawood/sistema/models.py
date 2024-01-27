
from django.db import models 

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True)
    stock = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Stock')
    precio = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Precio')
#   imagen = models.ImagenField(upload_to='imagenes/', verbose_name='Imagen', null=True)   / Para cargar en la bd la imagen del producto

    def __str__(self):
        fila = "Descripción: " + self.descripcion 
        return fila
    
    #def delete(self, using=None, keep_parents=False):
    #    self.image.storage.delete(self.imagen.name)
    #    super().delete()