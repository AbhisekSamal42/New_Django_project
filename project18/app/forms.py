from django import forms
from app.models import *
class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebPageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
class AccessRecordModelForm(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields='__all__'