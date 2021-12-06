from django.db import models

# Create your models here.
class ColorModel(models.Model):
    color_name=models.CharField(max_length=45)
    class Meta:
        db_table='color_tbl'