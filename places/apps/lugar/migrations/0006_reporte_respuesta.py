# Generated by Django 2.2.4 on 2019-12-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0005_remove_lugar_placeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='respuesta',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
