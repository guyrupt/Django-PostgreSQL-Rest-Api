from django.db import models

# Create your models here.

class table1(models.Model):
    tb1Id = models.AutoField(primary_key=True)
    tb1Name = models.CharField(max_length=500)
