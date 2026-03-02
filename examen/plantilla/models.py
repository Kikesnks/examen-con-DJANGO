from django.db import models
import oracledb

# Create your models here.

class Plantilla:
    def __init__(self):
        self.hcod = 0
        self.scod = 0
        self.empno = 0
        self.apellido = ""
        self.funcion = ""
        self.turno = ""
        self.salario = 0
    
class ServicioPlantilla():
    def __init__(self):
        self.conexion = oracledb.connect(user="system", password="oracle", dsn="LOCALHOST/FREEPDB1")
    
    def getPlantilla(self):
        sql = "select * from PLANTILLA"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        listaPlantilla = []
        for dato in cursor:
            plant = Plantilla()
            plant.hcod = dato[0]
            plant.scod = dato[1]
            plant.empno = dato[2]
            plant.apellido = dato[3]
            plant.funcion = dato[4]
            plant.turno = dato[5]
            plant.salario = dato[6]
            listaPlantilla.append(plant)
        
        cursor.close()
        return listaPlantilla
    