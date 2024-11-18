from django import forms
from .models import FileTransfer

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileTransfer
        fields = ['file']
