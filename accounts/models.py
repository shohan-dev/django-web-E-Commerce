from django.db import models
from django.contrib.auth.models import User
from email.message import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.core.mail import send_mail
from base.models import *
from base.emails import *



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)

    def __str__(self):
        return self.user.username



@receiver(post_save , sender = User)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            print("This is email_token:  ",email_token)
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)
            print("This is email:  ",email)
            print("Email Send Done")
            
        
          

    except Exception as e:
        print(e)


