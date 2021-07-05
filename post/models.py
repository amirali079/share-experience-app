from django.db import models
from socialmedia.models import User


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Post = id: {}, creator: {}, title: {}'.format(self.id, self.creator, self.title)


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField("content", max_length=2000)
    title = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        username = self.creator.username
        _content = self.content[:20]
        return f'{self.id}) comment by {username} on post {self.post.id}: {_content}'
