from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 150)
    summery = models.CharField(max_length = 400, blank = True)
    text = RichTextField()
    photo = models.ImageField(upload_to = 'images/', blank = True)
    date = models.DateTimeField(auto_now_add= True)
    auther = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('article_detail', args = [str(self.id)])