from django.db import models

# Create your models here.
class Person(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50, null = True)
    p_surname = models.CharField(max_length=50, null = True)
    p_tel = models.CharField(max_length=10, null = True)
    class Meta:
         db_table = "DJANGO_TEST"