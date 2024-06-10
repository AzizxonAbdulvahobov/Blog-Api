from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.ForeignKey(User, on_delete=models.CASCADE)
    viewers = models.ManyToManyField(User, blank=True, related_name="viewed_blogs")

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Like bosgan odam")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Qaysi blogga bosilganligi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        constraints = [
            UniqueConstraint(fields=['author', 'blog'], name='unique_like')
        ]

    def __str__(self):
        return f"{self.author.username} liked {self.blog.title}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Comment bosgan odam")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Qaysi blogga bosilganligi")
    content = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}..."  # Kommentning birinchi 20 ta belgisi ko'rsatiladi
