from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    category_id = models.ForeignKey('category', on_delete=models.CASCADE)
    author_id = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    contents = models.TextField()
    recommand_count = models.PositiveIntegerField()
    views_count = models.PositiveIntegerField()
    pullup_count = models.PositiveSmallIntegerField()
    pullup_at = models.DateTimeField()
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author_id = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    contents = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return author_id.username + ': ' + self.contents

class PostRecommand(models.Model):
    post_id = models.ForeignKey('post', on_delete=models.CASCADE)
    user_id = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    recommand_type = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CommentRecommand(models.Model):
    comment_id = models.ForeignKey('comment', on_delete=models.CASCADE)
    user_id = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    recommand_type = models.BooleanField()
    created_at = models.BooleanField()


