from django.db import models

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

    def __str__(self):
        return self.name + ": " + str(self.imagefile)