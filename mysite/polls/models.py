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

class Document(models.Model):
    doc_id = models.IntegerField(primary_key=True)
    doc_name = models.CharField(max_length=100)
    doc_path = models.FileField(upload_to='files/')

    class Meta:
        db_table = "IT_DOC_FILES"

    def ___str__(self):
        return self.doc_name