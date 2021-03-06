# Generated by Django 3.2.13 on 2022-05-21 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_agendar2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendar3',
            fields=[
                ('idHora', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.dia')),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.hora')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.medico')),
                ('mes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.mes')),
            ],
        ),
    ]
