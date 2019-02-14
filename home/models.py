from django.db import models
from django.utils import timezone
# Create your models here.

class Barang(models.Model):
    nama = models.CharField(max_length=255)
    gambar = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)

    def __str__(self):
        return self.nama