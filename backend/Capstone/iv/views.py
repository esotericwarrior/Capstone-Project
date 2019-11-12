from django.shortcuts import render
from iv.models import Video
from iv.forms import VideoForm, ImageForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
import requests
import json
import vimeo
import os



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
            upload_success = response_data['success']
            external_link = response_data['data']['link']
            print(upload_success)
            print(external_link)
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

            # vimeo needs to upload from filepath, so save temporarily
            video = Video(videofile = request.FILES['videofile'])
            video.save()
            
            client = vimeo.VimeoClient(
              token='a3340925680abc80d0327ca333c3f57d',
              key='900d7836b6e85f3ee6dde4ccce84e1e4aa45d986',
              secret='+cwWHT7FDZEJeuS29Et2TjZQZRfoATTt0FHe8ou2EyXD9nBVt6xySAK3SG86Gz86lAt+L1vM6n3/2rp3ojehHILs8rfj0EcGxorHlqmI90PvXYbYzlQa/xwGSZQCJ02y'
            )

            # grab file from where django saved it 
            file_name = settings.MEDIA_ROOT + video.videofile.name
            uri = client.upload(file_name, data={
              'description': request.POST['description']
            })

            response = client.get(uri + '?fields=transcode.status').json()
            if response['transcode']['status'] == 'complete':
              print ('Your video finished transcoding.')
            elif response['transcode']['status'] == 'in_progress':
              print ('Your video is still transcoding.')
            else:
              print ('Your video encountered an error during transcoding.')

            response = client.get(uri + '?fields=link').json()
            print("video link: " + response['link'])

            # clean up
            os.remove(settings.MEDIA_ROOT + video.videofile.name)
            return redirect('video')
    else:
        form = VideoForm()
    return render(request, 'iv/video.html', {
        'form': form
    })


# URL pattern "delete/image/<image_hash>/"
def image_delete(request, image_hash):
#    if request.method == 'POST':
        
        url = "https://api.imgur.com/3/image/" + image_hash
        access_token = "931ddfab9e19c9a7512147c83459ce1d457e09cf"
        headers = {'Authorization': 'Bearer ' + access_token}
        
        response = requests.request("DELETE", url, headers=headers)
        response_data = response.json()
        #print(response_data)
        print(response_data['success']) # True
        
        return redirect('/')
'''    else:
        form = ImageForm()
    return render(request, 'iv/image.html', {
        'form': form
    })
'''


# URL pattern "favorite/image/<image_hash>/"
def image_favorite(request, image_hash):
#    if request.method == 'POST':
        
        url = "https://api.imgur.com/3/image/" + image_hash + "/favorite"
        access_token = "931ddfab9e19c9a7512147c83459ce1d457e09cf"
        headers = {'Authorization': 'Bearer ' + access_token}
        
        response = requests.request("POST", url, headers=headers)
        response_data = response.json()
        #print(response_data)
        print(response_data['data'])    # favorited / unfavorited
        print(response_data['success']) # True
        
        return redirect('/')
'''    else:
        form = ImageForm()
    return render(request, 'iv/image.html', {
        'form': form
    })
'''


# URL pattern "list/favorites/"
def image_get_favorites(request):
#    if request.method == 'POST':
        
        url = "https://api.imgur.com/3/account/higrandpa/favorites/" 
        access_token = "931ddfab9e19c9a7512147c83459ce1d457e09cf"
        headers = {'Authorization': 'Bearer ' + access_token}
        
        response = requests.request("GET", url, headers=headers)
        response_data = response.json()
        print(response_data['success']) # True
        #print(response_data['data'])
        
        favorites_list = []
        for i in response_data['data']:
            favorites_list.append(i['link'])
        print(favorites_list)           # array of URLs
        
        return redirect('/')

'''    else:
        form = ImageForm()
    return render(request, 'iv/image.html', {
        'form': form
    })
'''