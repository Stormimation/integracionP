# Generated by Django 3.1.7 on 2021-11-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('idMedico', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreMedico', models.CharField(max_length=50)),
                ('apellidoMedico', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=50)),
            ],
        ),
    ]
