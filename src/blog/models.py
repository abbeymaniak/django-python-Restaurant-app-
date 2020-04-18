from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    Content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/' , blank=True, null=True)
    category = models.ForeignKey('Category' ,null=True, on_delete=models.SET_NULL)
    #tags
    created = models.DateTimeField(default=timezone.now)

    tags = TaggableManager(blank=True)



    #To change normalize the name of the table created from singular to plural
    class Meta:
        verbose_name = ' post'
        verbose_name_plural = 'posts'

    #To change show the name instead of object
    def __str__(self):
        return self.title





class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ' category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category_name





class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.content)