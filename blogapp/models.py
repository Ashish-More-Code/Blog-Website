from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blogpost(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='userid')
    title=models.CharField(max_length=200)
    content=models.TextField()
    createdate=models.DateTimeField()
    type=models.IntegerField()
    pimage=models.ImageField(upload_to='image/')

class Comments(models.Model):
    bid=models.ForeignKey(Blogpost,on_delete=models.CASCADE,db_column='blogid')
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='userid')
    likecount=models.IntegerField()
    comments=models.CharField(max_length=200)