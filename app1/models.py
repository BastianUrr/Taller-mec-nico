from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacto(models.Model):
    id  = models.AutoField(db_column='idContacto', primary_key=True) 
    texto     = models.CharField(max_length=1000, blank=False, null=False)
    email     = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    

class Diagnostico(models.Model):
    id = models.AutoField(db_column='idDiagnostico', primary_key=True) 
    nombre    = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)
    


class Categoria(models.Model):
    id  = models.AutoField(db_column='idCategoria', primary_key=True) 
    nombre     = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)
    

class Material(models.Model):
    id  = models.AutoField(db_column='idMaterial', primary_key=True) 
    nombre     = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)
    



class Trabajo(models.Model):
    id  = models.AutoField(db_column='idTrabajo', primary_key=True)
    fecha = models.DateField(blank=False, null=False)
    publicado           = models.IntegerField() 
    descripcion     = models.CharField(max_length=1000, blank=False, null=False)
    titulo     = models.CharField(max_length=60, blank=False, null=False)
    nombre_foto     = models.CharField(max_length=30, blank=False, null=False)

    id_categoria        = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    id_diagnostico        = models.ForeignKey('Diagnostico',on_delete=models.CASCADE, db_column='idDiagnostico')
    cliente = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    


class Material_trabajo(models.Model):
    id_material        = models.ForeignKey('Material',on_delete=models.CASCADE, db_column='idMaterial')
    id_trabajo        = models.ForeignKey('Trabajo',on_delete=models.CASCADE, db_column='idTrabajo')

    def __str__(self):
        return str(self.id_trabajo) + " - " + str(self.id_material)
    