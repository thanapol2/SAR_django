from django.db import models

# Create your models here.

class Main_Cate(models.Model):
    main_topic_id = models.CharField(max_length=20, primary_key=True)
    main_detail = models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=150, null=True)
    short_result = models.CharField(max_length=2, null=True)
    class Meta:
         db_table = "EVA_CURRENT_MAIN_TOPIC"

class Sub_Cate(models.Model):
    seq_id = models.CharField(max_length=20, primary_key=True)
    sub_no = models.CharField(max_length=20, null = True)
    username = models.CharField(max_length=20, null = True)
    weight = models.CharField(max_length=20, null = True)
    target = models.CharField(max_length=20, null=True)

    class Meta:
         db_table = "EVA_EVA_DETAIL"