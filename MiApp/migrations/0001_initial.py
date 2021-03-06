# Generated by Django 3.1 on 2020-10-05 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellido', models.CharField(max_length=30)),
                ('Nombre', models.CharField(max_length=30)),
                ('DNI', models.CharField(max_length=8)),
                ('FechaNac', models.DateField()),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], default='M', max_length=1)),
                ('Bloqueado', models.BooleanField(default=False)),
            ],
        ),
    ]
