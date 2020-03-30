from django import forms
from django.forms import TextInput, HiddenInput

from .models import Sub_Cate

class SubCateForm(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no','username','weight','target')


class SubCateForm_Test(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no','username','weight','target')

    def __init__(self, *args, **kwargs):
        super(SubCateForm_Test, self).__init__(*args, **kwargs)
        self.fields['sub_no'].widget = HiddenInput(attrs={
            'class': 'textinput textInput from-control',
            'value': '11'})

    def setValueUsername(self, Username):
        self.fields['username'].widget = HiddenInput(attrs={
            'class': 'textinput textInput from-control',
            'value': Username})