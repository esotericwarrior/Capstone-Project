from django.shortcuts import render
from iv.models import Video
from iv.forms import VideoForm, ImageForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
import requests
import json


def image_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            url = "https://api.imgur.com/3/upload"
            access_token = "931ddfab9e19c9a7512147c83459ce1d457e09cf"
            headers = {'Authorization': 'Bearer ' + access_token}
            data = {
                    'image': request.FILES.get('imagefile').read(),
                    'title': request.POST['description'], 
                    'type': 'file'
                    }
            response = requests.request("POST", url, headers=headers, data=data)
            response_data = response.json()
            #print(response_data)
            print(response_data['success'])
            print(response_data['data']['link'])
            return redirect('image')
    else:
        form = ImageForm()
    return render(request, 'iv/image.html', {
        'form': form
    })


def video_form_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video')
    else:
        form = VideoForm()
    return render(request, 'iv/video.html', {
        'form': form
    })