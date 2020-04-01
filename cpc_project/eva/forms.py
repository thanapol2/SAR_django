from django import forms
from django.forms import TextInput, HiddenInput, Select, NumberInput

from .models import Sub_Cate

TARGET_CHOICES=[
    ('','-- Select Target --'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

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
        self.fields['weight'].widget = NumberInput(attrs={
            'autocomplete':'off',
            'min': 0,
            'class': 'form-control'})
        self.fields['target'].widget = Select(choices=TARGET_CHOICES, attrs={
            'class': 'form-control'})



class SubCateFormUpdate(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no','username','weight','target')

    def __init__(self, *args, **kwargs):
        super(SubCateFormUpdate, self).__init__(*args, **kwargs)

    def setValueSubNo(self, SubNo):
        self.fields['sub_no'].widget = HiddenInput(attrs={
            'class': 'from-control',
            'value': SubNo})

    def setValueUsername(self,Username):
        self.fields['username'].widget = HiddenInput(attrs={
            'class': 'form-control',
            'value': Username})
        self.fields['weight'].widget = NumberInput(attrs={
            'autocomplete': 'off',
            'min': 0,
            'class': 'form-control'})
        self.fields['target'].widget = Select(choices=TARGET_CHOICES,attrs={
            'class': 'form-control'})