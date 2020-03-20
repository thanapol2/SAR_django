from django import forms
from .models import Person, Document

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('p_name','p_surname','p_tel','username','password')
        labels = {
            'p_name':'Name',
            'p_surname':'Surname',
            'p_tel':'Phone number',
            'username':'Username',
            'password':'Password'
        }

class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('doc_name','doc_path')
        labels = {
            'doc_name':'File name',
            'doc_path':' '
        }


