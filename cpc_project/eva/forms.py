from django import forms
from django.forms import TextInput, HiddenInput

from .models import Sub_Cate

class SubCateFormInsert(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no','username','weight','target')

    def __init__(self, *args, **kwargs):
        super(SubCateFormInsert, self).__init__(*args, **kwargs)

    def setValueSubNo(self, SubNo):
        self.fields['sub_no'].widget = HiddenInput(attrs={
            'class': 'textinput textInput from-control',
            'value': SubNo})

    def setValueUsername(self, Username):
        self.fields['username'].widget = HiddenInput(attrs={
            'class': 'textinput textInput form-control',
            'value': Username})

class SubCateForm_Test(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no','username','weight','target')

    def __init__(self, *args, **kwargs):
        super(SubCateForm_Test, self).__init__(*args, **kwargs)
        self.fields['sub_no'].widget = HiddenInput(attrs={
            'class': 'textinput textInput from-control',
            'value': '11'})

    def setValueUsername(self,Username):
        self.fields['username'].widget = HiddenInput(attrs={
            'class': 'textinput textInput form-control',
            'value': Username})