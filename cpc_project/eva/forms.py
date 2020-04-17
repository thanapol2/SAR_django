from django import forms
from django.forms import TextInput, HiddenInput, Select, NumberInput

from .models import Sub_Cate, Document

TARGET_CHOICES=[
    ('0','-- Select Target --'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class SubCateFormInsert(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no', 'username', 'weight', 'target')

    def __init__(self, *args, **kwargs):
        super(SubCateFormInsert, self).__init__(*args, **kwargs)

    def setValueSubNo(self, SubNo):
        self.fields['sub_no'].widget = HiddenInput(attrs={
            'class': 'from-control',
            'value': SubNo})

    def setValueUsername(self, Username):
        self.fields['username'].widget = HiddenInput(attrs={
            'class': 'form-control',
            'value': Username})
        self.fields['weight'].widget = NumberInput(attrs={
            'autocomplete': 'off',
            'min': 0,
            'value': 0,
            'class': 'form-control'})
        self.fields['target'].widget = Select(choices=TARGET_CHOICES, attrs={
            'class': 'form-control'})

class SubCateFormUpdate(forms.ModelForm):
    class Meta:
        model = Sub_Cate
        fields = ('sub_no', 'username', 'weight', 'target')

    def __init__(self, *args, **kwargs):
        super(SubCateFormUpdate, self).__init__(*args, **kwargs)
        self.fields['sub_no'].widget = HiddenInput(attrs={
            'class': 'from-control'})
        self.fields['username'].widget = HiddenInput(attrs={
            'class': 'form-control'})
        self.fields['target'].widget = Select(choices=TARGET_CHOICES,attrs={
            'class': 'form-control'})

class UserFormUpload(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file_name', 'upload_user', 'path_file')

    def __init__(self, *args, **kwargs):
        super(UserFormUpload, self).__init__(*args, **kwargs)

    def setUploadUsername(self, Username):
        self.fields['upload_user'].widget = HiddenInput(attrs={
            'class': 'form-control',
            'value': Username})
