from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
def path_and_rename(instance,filename):
    upload_to='pictures/'
    #removing the file extension and then creating new file
    #with username and returning to the media folder
    ext=filename.split('.')[-1]
    if instance.user.username:
        filename='profile_pics/{}.{}'.format(instance.user.username,ext)
        return os.path.join(upload_to,filename)
class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
   
    bio=models.CharField(max_length=150,blank=True)

    profile_picture=models.ImageField(upload_to=path_and_rename ,verbose_name='profile picture',blank=True)

    teacher='teacher'
    student='student'
    user_types=[
    (teacher,'teacher'),
    (student,'student'),
    ]
    user_type=models.CharField(max_length=10,choices=user_types,default=student)
    def __str__(self):
        return self.user.username
