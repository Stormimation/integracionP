from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Medico(models.Model):
    idMedico=models.IntegerField(primary_key=True)
    nombreMedico=models.CharField(max_length=50)
    apellidoMedico=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=50)

     

class UsuarioP3(models.Model):
    rut=models.CharField(max_length=30, primary_key=True)
    email=models.CharField(max_length=300)
    nombre=models.CharField(max_length=300)
    edad=models.CharField(max_length=300)
    password=models.CharField(max_length=10)  

class UsuarioP4(models.Model):
    rut=models.CharField(max_length=30, primary_key=True)
    email=models.CharField(max_length=300)
    nombre=models.CharField(max_length=300)
    apellidos=models.CharField(max_length=300)
    region=models.CharField(max_length=300)
    provincia=models.CharField(max_length=300)
    comuna=models.CharField(max_length=300)
    edad=models.CharField(max_length=300)
    sexo=models.CharField(max_length=300)
    password=models.CharField(max_length=10) 

class UsuarioM(models.Model):
    id=models.CharField(max_length=30, primary_key=True)
    nombre=models.CharField(max_length=300)
    password=models.CharField(max_length=10)

class UsuarioS(models.Model):
    id=models.CharField(max_length=30, primary_key=True)
    nombre=models.CharField(max_length=300)
    password=models.CharField(max_length=10)  

class Region(models.Model):
    region=models.CharField(max_length=30)

class Provincia(models.Model):
    provincia=models.CharField(max_length=30)

class Comuna(models.Model):
    comuna=models.CharField(max_length=30)

class sexo(models.Model):
    sexo=models.CharField(max_length=30)                     

class Dia(models.Model):
    dia=models.CharField(max_length=20)  

class Mes(models.Model):
    mes=models.CharField(max_length=30)    

class Hora(models.Model):
    hora=models.CharField(max_length=50)

class Agendar(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.ForeignKey(Dia, on_delete=models.CASCADE)
    mes=models.ForeignKey(Mes, on_delete=models.CASCADE)
    hora=models.ForeignKey(Hora, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)

class Agendar2(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.ForeignKey(Dia, on_delete=models.CASCADE)
    mes=models.ForeignKey(Mes, on_delete=models.CASCADE)
    hora=models.ForeignKey(Hora, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE) 
    nombre=models.ForeignKey(UsuarioP3, on_delete=models.CASCADE)


class Agendar3(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.ForeignKey(Dia, on_delete=models.CASCADE)
    mes=models.ForeignKey(Mes, on_delete=models.CASCADE)
    hora=models.ForeignKey(Hora, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE) 
    nombre=models.CharField(max_length=300) 

class Agendar4(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.CharField(max_length=300)
    mes=models.CharField(max_length=300)
    hora=models.CharField(max_length=300)
    medico=models.CharField(max_length=300) 
    nombre=models.CharField(max_length=300)  


class Agendar5(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.CharField(max_length=300)
    mes=models.CharField(max_length=300)
    hora=models.CharField(max_length=300)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE) 
    nombre=models.CharField(max_length=300) 


              
class Agendar6(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.CharField(max_length=300)
    mes=models.CharField(max_length=300)
    hora=models.CharField(max_length=300)
    medico=models.CharField(max_length=300) 
    nombre=models.CharField(max_length=300)    


class AgendarA(models.Model):
    idHora=models.CharField(max_length=30, primary_key=True)
    dia=models.CharField(max_length=300)
    mes=models.CharField(max_length=300)
    hora=models.CharField(max_length=300)
    medico=models.CharField(max_length=300) 
    nombre=models.CharField(max_length=300)   
    mensaje=models.CharField(max_length=300)