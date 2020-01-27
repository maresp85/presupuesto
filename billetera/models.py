from django.db import models
import datetime

# Create your models here.
class Balance(models.Model):
    saldo = models.DecimalField(max_digits=8, decimal_places=0)
    ingresos = models.IntegerField()
    gastos = models.IntegerField()

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Movimiento(models.Model):
    GASTO = 1
    INGRESO = 2
    TIPO_GASTO_CHOICE = [
        (INGRESO, 'Ingreso'),
        (GASTO, 'Gasto'),
    ]
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=TIPO_GASTO_CHOICE, default=GASTO)
    monto = models.DecimalField(max_digits=8, decimal_places=0)
    fecha = models.DateField(default=datetime.date.today)
