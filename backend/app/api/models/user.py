from django.db import models

class User(models.Model):
    password = models.CharField(max_length=128, blank=False)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=250, blank=False)