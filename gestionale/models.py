from django.db import models

# Create your models here.
class Esame(models.Model):
    data_ora = models.DateTimeField(null=True)
    valore = models.FloatField()
    unita_misura = models.CharField(max_length=20)
    paziente = models.ForeignKey('Paziente', on_delete=models.CASCADE)

class Paziente(models.Model):
    codice_fiscale = models.CharField(max_length=16)
    nome = models.CharField(max_length=255)
    cognome = models.CharField(max_length=255)