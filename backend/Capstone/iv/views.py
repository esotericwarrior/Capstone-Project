from django.shortcuts import render
from iv.models import Video
from iv.forms import VideoForm, ImageForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

def image_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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