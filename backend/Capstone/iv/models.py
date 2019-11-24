from django.db import models
from django.conf import settings 

# Create your models here.
class Video(models.Model):
    description= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)


class Image(models.Model):
    description = models.CharField(max_length=255, blank=True)
    imagefile = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="images")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)