from django.db import models

class MyModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.URLField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    personal_link = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class POST(models.Model):
    post_id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created_at']

class LIKE(models.Model):
    class LikeType(models.TextChoices):
        LIKE = 'like', 'Like'
        DISLIKE = 'dislike', 'Dislike'

    like_id = models.AutoField(primary_key=True) 
    post = models.ForeignKey(POST, on_delete=models.CASCADE)
    user = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    like_type = models.CharField(
        max_length=10,
        choices=LikeType.choices,
        default=LikeType.LIKE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user', 'like_type')

class COMMENT(models.Model):
    comment_id = models.AutoField(primary_key=True)  
    post = models.ForeignKey(POST, on_delete=models.CASCADE)
    user = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class FOLLOWS(models.Model):
    follower = models.ForeignKey(MyModel, related_name='following_set', on_delete=models.CASCADE)
    followed = models.ForeignKey(MyModel, related_name='follower_set', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'followed')
