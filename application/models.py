import uuid
from django.db import models

# Create your models here.
class Storage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    storage_initial = models.CharField(max_length=10, unique=True)  # Menyimpan tipe penyimpanan (misal 'RK', 'FR')
    description = models.CharField(max_length=50, blank=True, null=True)  # Deskripsi bisa kosong atau NULL

    def __str__(self):
        return f'{self.storage_type} - {self.description if self.description else "No description"}'
