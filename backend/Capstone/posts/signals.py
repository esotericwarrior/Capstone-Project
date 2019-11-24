from django.db.models.signals import pre_save
from django.core.signals import request_started
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from posts.models import Post

###############################
# Function manaually assigns
# the slug field to the new
# instance before it's created.
# Once saved, the new instance
# can have it's own unique slug
###############################
@receiver(pre_save, sender=Post)
def add_slug_to_post(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        print(instance)
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

