from django import forms
from .models import Sub_Cate11

class SubCateForm11(forms.ModelForm):
    class Meta:
        model = Sub_Cate11
        fields = ('sub_no','username','weight','target')