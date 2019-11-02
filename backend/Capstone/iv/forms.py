from django import forms
from django.forms import ModelForm

from .models import Image, Video

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["description", "videofile"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'imagefile', )