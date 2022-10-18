
from django.db import models

# Create your models here.
class Materi(models.Model):
    no = models.CharField(max_length=200)
    bab = models.CharField(max_length=200)
    daftar_materi = models.CharField(max_length=200)
    sub_materi = models.CharField(max_length=200)

