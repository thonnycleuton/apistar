import uuid

from django.db import models

STATUS_CHOICES = (
    ('active', 'active'),
    ('inactive', 'inactive')
)


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_identity = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
