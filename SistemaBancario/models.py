from django.db import models

# Create your models here.

class TipoCuenta(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return self.descripcion

class Genero(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
       return self.descripcion

class EmpresaEmpleo(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    nombre_jefe = models.CharField(max_length=500)
    cargo = models.CharField(max_length=200)
    salario_mes = models.CharField(max_length=200)

    def __str__(self):
       return self.nombre_empresa +" "+ self.nombre_jefe +" "+ self.cargo +" "+ self.salario_mes

class AperturaCuenta(models.Model):
    id_nacional = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=500)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_nacional +" "+ self.nombre_completo +" "+ self.direccion +" "+ self.telefono +" "+  self.empresa


class Cuentas(models.Model):
    id_cuenta = models.CharField(max_length=200)
    cliente = models.CharField(max_length=500)
    saldo = models.CharField(max_length=200)
    id_tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_cuenta

class Transacciones(models.Model):
    id_transacciones = models.CharField(max_length=200)
    depositos = models.CharField(max_length=200)
    retiros = models.CharField(max_length=200)

    def __str__(self):
        return self.depositos + " " + self.retiros

class GestionCuentas(models.Model):
    id_cuenta = models.ForeignKey(Cuentas, on_delete=models.CASCADE)
    id_transacciones = models.ForeignKey(Transacciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_cuenta.cliente + " " + self.id_transacciones

class TipoPrestamo(models.Model):
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descripcion

class Titular(models.Model):
    nombre_completo = models.CharField(max_length=200)
    
    def __str__(self):
      return self.nombre_completo

class Prestamo(models.Model):
    monto = models.CharField(max_length=200)
    cuota = models.CharField(max_length=200)
    id_titular = models.ForeignKey(Titular, on_delete=models.CASCADE)
    id_tipo_empleo = models.ForeignKey(EmpresaEmpleo, on_delete=models.CASCADE)
    id_tipo_prestamo = models.ForeignKey(TipoPrestamo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.monto + " " + self.cuota

    
class Plazos(models.Model):
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
      return self.descripcion

class TipoRemesa(models.Model):
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
      return self.descripcion

class Destinatario(models.Model):
    id_nacional = models.CharField(max_length=50)
    nombre = models.CharField(max_length=500)
    pais = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id_nacional +" "+ self.nombre +" "+ self.pais +" "+ self.direccion

class Remesas(models.Model):
    monto = models.CharField(max_length=200)
    fecha_envio = models.DateField()
    id_tipo_remesa = models.ForeignKey(TipoRemesa, on_delete=models.CASCADE)
    id_destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE)

    def __str__(self):
        return self.monto + " " + self.cuota



    