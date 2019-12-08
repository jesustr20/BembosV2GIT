from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Colaborador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Localidad = models.CharField(max_length=100)
    edad = models.IntegerField()
    #rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaborador'
        ordering = ['edad']

    def __str__(self):
        return f'{self.user.username}'

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=8)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rol'
        ordering = ['rol']

    def __str__(self):
        return f'{self.rol}'

#parte de magaly


class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    ingrediente = models.CharField(max_length=100, null = True , blank=True)
    precio = models.DecimalField(max_digits=16, decimal_places=2)
    cantidad = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to="pictures", max_length=255, null=True)

    def __str__(self):
        return f'{str(self.ingrediente)}'

class TipoIngrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null = True, blank=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.nombre)}'

class EstadoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=255, null = True, blank=True)

    def __str__(self):
        return (self.estado)

class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return f'{str(self.ingrediente)}'

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=255, null = True, blank = True)
    fecha_pedido = models.DateTimeField()
    detallepedido = models.ManyToManyField(DetallePedido)
    monto_total = models.DecimalField(max_digits=16, decimal_places=2)
    atendidopor = models.CharField(max_length=255, null=True, blank=True)
    estado = models.ForeignKey(EstadoPedido, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{str(self.id)}'