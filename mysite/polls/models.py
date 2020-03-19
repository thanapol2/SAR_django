from django.db import models

# Create your models here.
class Person(models.Model):
    p_id = models.CharField(max_length=50,primary_key=True)
    p_name = models.CharField(max_length=50, null = True)
    p_surname = models.CharField(max_length=50, null = True)
    p_tel = models.CharField(max_length=10, null = True)
    username = models.CharField(max_length=100, null = True)
    password = models.CharField(max_length=20, null = True)
    class Meta:
         db_table = "DJANGO_TEST"