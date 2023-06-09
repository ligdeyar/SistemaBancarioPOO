# Generated by Django 4.1.7 on 2023-04-01 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cuenta', models.CharField(max_length=200)),
                ('cliente', models.CharField(max_length=500)),
                ('saldo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nacional', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=500)),
                ('pais', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaEmpleo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('nombre_jefe', models.CharField(max_length=500)),
                ('cargo', models.CharField(max_length=200)),
                ('salario_mes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plazos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPrestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRemesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_transacciones', models.CharField(max_length=200)),
                ('depositos', models.CharField(max_length=200)),
                ('retiros', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Remesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.CharField(max_length=200)),
                ('fecha_envio', models.DateField()),
                ('id_destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.destinatario')),
                ('id_tipo_remesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.tiporemesa')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.CharField(max_length=200)),
                ('cuota', models.CharField(max_length=200)),
                ('id_tipo_empleo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.empresaempleo')),
                ('id_tipo_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.tipoprestamo')),
                ('id_titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.titular')),
            ],
        ),
        migrations.CreateModel(
            name='GestionCuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.cuentas')),
                ('id_transacciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.transacciones')),
            ],
        ),
        migrations.AddField(
            model_name='cuentas',
            name='id_tipo_cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.tipocuenta'),
        ),
        migrations.CreateModel(
            name='AperturaCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nacional', models.CharField(max_length=50)),
                ('nombre_completo', models.CharField(max_length=500)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('empresa', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('id_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaBancario.genero')),
            ],
        ),
    ]
