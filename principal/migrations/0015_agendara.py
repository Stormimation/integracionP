# Generated by Django 3.2.13 on 2022-06-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_comuna_provincia_region_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendarA',
            fields=[
                ('idHora', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=300)),
                ('mes', models.CharField(max_length=300)),
                ('hora', models.CharField(max_length=300)),
                ('medico', models.CharField(max_length=300)),
                ('nombre', models.CharField(max_length=300)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
    ]
