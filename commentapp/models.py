from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False,
                                related_name='comments')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                               related_name='comments')

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)

