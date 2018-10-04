from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class ObjectPermission(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    can_view = models.BooleanField()
    can_change = models.BooleanField()
    can_delete = models.BooleanField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        permissions = (
            ('view_post', 'Can view post'),
        )