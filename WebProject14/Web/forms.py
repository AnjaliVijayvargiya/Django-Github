from django import forms

from .models import EntryModel

class EntryForm(forms.ModelForm): 
    class Meta: 
        model = EntryModel
        fields = "__all__"