# Generated by Django 4.1.2 on 2022-10-31 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_producto_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tienda.marca'),
        ),
    ]