# Generated by Django 4.1.2 on 2022-11-08 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('nombre', models.CharField(default='Sin Marca asignada', max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, null=True, unique=True)),
                ('modelo', models.CharField(max_length=30)),
                ('unidades', models.IntegerField(null=True)),
                ('precio', models.FloatField(null=True)),
                ('detalles', models.CharField(max_length=30, null=True)),
                ('marca', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.RESTRICT, to='tienda.marca', verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('unidades', models.IntegerField()),
                ('importe', models.FloatField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Nombre', to='tienda.producto', to_field='nombre')),
            ],
        ),
    ]
