from django import forms
from . import models

class NewsForm(forms.ModelForm):
    class Meta:
        model = models.NewsModel
        fields = '__all__'