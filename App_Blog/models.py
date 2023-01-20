from django.db import models
from django.contrib.auth.models import User
# from django.utils.text import slugify
# from datetime import date
from django.template.defaultfilters import slugify
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    # slug = models.SlugField(max_length=255, unique=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    # post_date = models.DateField(default=date.today)
    blog_content = models.TextField(verbose_name='what is your mind!!')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.publish_date))
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.blog_title)




class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)
    def __str__(self) :
        return self.comment


class Like(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE, related_name="liked_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker_user")


    def __str__(self):
        return self.user + " likes " + self.blog
