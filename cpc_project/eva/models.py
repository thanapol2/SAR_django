from django.db import models

# Create your models here.
#  Master model
class Sub_Cate_Master(models.Model):
    sub_id = models.CharField(max_length=20, primary_key=True)
    seq = models.CharField(max_length=20)
    main_id = models.CharField(max_length=20)

    class Meta:
         db_table = "EVA_SUB_TOPIC"

#  /////////////////////////////////////////////

class Main_Cate(models.Model):
    main_topic_id = models.CharField(max_length=20, primary_key=True)
    main_detail = models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=150, null=True)
    short_result = models.CharField(max_length=2, null=True)

    class Meta:
         db_table = "EVA_CURRENT_MAIN_TOPIC"

class Sub_Cate(models.Model):
    seq_id = models.CharField(max_length=20, primary_key=True)
    # sub_no = models.CharField(max_length=20, null = True)
    sub_no = models.ForeignKey(Sub_Cate_Master,on_delete=models.CASCADE,to_field='sub_id',db_column='sub_no')
    username = models.CharField(max_length=20, null = True)
    weight = models.CharField(max_length=20, null = True)
    target = models.CharField(max_length=20, null=True)

    class Meta:
         db_table = "EVA_EVA_DETAIL"

class Document(models.Model):
    file_id = models.CharField(max_length=200, primary_key=True)
    file_name = models.CharField(max_length=200, null=True)
    upload_user = models.CharField(max_length=200, null=True)
    path_file = models.FileField(upload_to='files/')

    class Meta:
        db_table = "EVA_TRAN_FILE"

    def ___str__(self):
        return self.file_name

