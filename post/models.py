from django.db import models
import uuid
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class post(models.Model):
    id = models.UUIDField(primary_key= True,default=uuid.uuid7)
    content = models.TextField(null = True,blank = True)
    image = models.ImageField(null =True,blank=True,upload_to='post/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)