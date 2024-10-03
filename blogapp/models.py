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
    likecount = models.IntegerField(default=0)


class Like(models.Model):
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('blogpost', 'user')

class comments(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='userid')
    bid=models.ForeignKey(Blogpost,on_delete=models.CASCADE,db_column='blogid')
    comment=models.TextField()

