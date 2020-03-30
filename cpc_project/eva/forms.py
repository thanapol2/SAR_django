from django import forms
from django.forms import TextInput, HiddenInput

from .models import Sub_Cate

class SubCateForm(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no','username','weight','target')


class SubCateForm_test(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no','username','weight','target')

    def __init__(self, *args, **kwargs):
        super(SubCateForm_test, self).__init__(*args, **kwargs)
        self.fields['description'].widget = HiddenInput(attrs={
            'class': 'myCustomClass'})