from django.db import models
from django.contrib.auth.models import User
from email.message import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.core.mail import send_mail


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    password = models.CharField(max_length=100)


