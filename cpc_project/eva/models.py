from django.db import models

# Create your models here.


class Sub_Cate11(models.Model):
    sub_no = models.CharField(max_length=20, null = True)
    username = models.CharField(max_length=20, null = True)
    weight = models.CharField(max_length=20, null = True)
    target = models.CharField(max_length=20, null=True)

    class Meta:
         db_table = "EVA_EVA_DETAIL"