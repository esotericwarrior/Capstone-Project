from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status

from iv.api.permissions import IsAuthorOrReadOnly
from iv.api.serializers import ImageSerializer
from iv.models import Image, Video


from django.shortcuts import render
from iv.forms import VideoForm, ImageForm
from posts.models import Post
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
import requests
import json
import vimeo
import os


class IVViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by("-description")
 #   lookup_field = "slug"
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    #parser_classes = (FormParser, MultiPartParser, FileUploadParser, JSONParser)
    parser_class = (FileUploadParser,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def image_form_upload(request):
	    if request.method == 'POST':
	        form = ImageForm(request.POST, request.FILES)
	        if form.is_valid():
	            
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
	            upload_success = response_data['success']
	            external_link = response_data['data']['link']
	            print(upload_success)

	            # save reference to database as a post
	            new_post = Post(content = external_link, author = request.user)
	            new_post.save()

	            return redirect('image')
	    else:
	        form = ImageForm()
	    return render(request, 'iv/image.html', {
	        'form': form
	    })


class FileUploadView(APIView):
	parser_class = (FileUploadParser,)

	def post(self, request, *args, **kwargs):
	    file_serializer = ImageSerializer(data=request.data)

	    if file_serializer.is_valid():
	        file_serializer.save()
	        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
	    else:
	        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)