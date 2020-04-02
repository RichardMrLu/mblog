from django.db import models
from django.utils import timezone







# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)         #文章的标题
    slug = models.CharField(max_length=200)          #文章的网址
    body = models.TextField()                        #文章的内容
    pub_date = models.DateTimeField(default=timezone.now)  #本文发表的时间

    class Meta:
        ordering = ('-pub_date',)        #指定文章显示的顺序

    def __str__(self):
        return self.title