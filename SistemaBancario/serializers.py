from rest_framework import serializers 
from SistemaBancario.models import *
 
 
class TipoCuentaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TipoCuenta
        fields = ('id', 'descripcion', 'fecha_creacion')
 
class GeneroSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Genero
        fields = ('id', 'descripcion')
                   
class EmpresaEmpleoSerializer(serializers.ModelSerializer):
    #es para saber si es apto para la apertura de la cuenta
    class Meta:
        model = EmpresaEmpleo
        fields = ('id','nombre_empresa','nombre_jefe','cargo','salario_mes')
                   
class AperturaCuentaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AperturaCuenta
        fields = ('id', 'id_nacional', 'nombre_completo', 'direccion', 'telefono', 'empresa', 'fecha_nacimiento', 'email', 'id_genero')

class CuentasSerializer(serializers.ModelSerializer):
    def validate_id(self, value):
        # Verifica si esta activa o inactiva  y si pertenece a esa persona una cuenta en la base de datos 
        #
        if Cuentas.objects.filter(id=value).exists():
            raise serializers.ValidationError('Ya existe esta cuenta con esta persona')
        return value

    class Meta:
        model = Cuentas
        fields = ('id', 'id_cuenta', 'cliente','saldo','id_tipo_cuenta')
                   
class TransaccionesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Transacciones
        fields = ('id','id_transacciones','depositos', 'retiros')

class GestionCuentasSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GestionCuentas
        fields = ('id', 'id_cuenta', 'id_transacciones')
        
class TitularSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Titular
        fields = ('id', 'descripcion')

class PrestamoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Prestamo
        fields = ('id','monto','cuota','id_titular','id_tipo_empleo','id_tipo_prestamo')

class PlazosSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Plazos
        fields = ('id', 'descripcion')

class TipoRemesaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TipoRemesa
        fields = ('id', 'descripcion')

class DestinatarioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Destinatario
        fields = ('id','id_nacional','nombre','pais','direccion')

class RemesasSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Remesas
        fields = ('id','monto','fecha_envio','id_tipo_remesa','id_destinatario')




