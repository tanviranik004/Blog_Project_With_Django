from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    slug = models.CharField(max_length=1000, null=True, blank=True)
    blog_content = models.TextField(verbose_name='what is your mind!!')
    blog_image = models.ImageField(upload_to='blog_images/%Y/%M/%D/', verbose_name='Image', blank=True, null=True, default='media/blog_images/anik.png')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering = ['-publish_date',]


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + int(self.publish_date))
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
