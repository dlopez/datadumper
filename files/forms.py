from django import forms

from files.models import File


class UploadForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['title', 'file']
        labels = {
            'file': "File",
        }
