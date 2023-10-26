from django.db import models

# Create your models here.
class AddRecord(models.Model):
    img=models.ImageField(upload_to="img")