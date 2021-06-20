from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_created=True)

    def count(self):
        comments = Comment.objects.filter(post_id=self).count()
        return comments


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

