# Generated by Django 4.1.6 on 2023-03-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isb', models.CharField(default='', max_length=20)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('imagen', models.ImageField(default='', upload_to='')),
                ('disponible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PaginaInicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mision', models.CharField(default='', max_length=200)),
                ('vision', models.CharField(default='', max_length=200)),
                ('quienesSomos', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroOrden', models.IntegerField(default=0)),
                ('nombre', models.IntegerField(default='', max_length=20)),
                ('telefono', models.CharField(default='', max_length=9)),
                ('correo', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='solicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.IntegerField(default='', max_length=20)),
                ('telefono', models.CharField(default='', max_length=9)),
                ('correo', models.EmailField(default='', max_length=254)),
                ('detalle', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
