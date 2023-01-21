from django.db import models  
from django.db.models import fields
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, View, TemplateView
from App_Blog import models
from App_Blog.forms import CommentForm
from App_Blog.models import Blog, Comment, Like
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from App_Blog.forms import CommentForm 
from .models import Blog
# from django.shortcuts import get_object_or_404
# Create your views here.

# def blog_list(request):
#     return render(request,'App_Blog/blog_list.html',context={})


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)


    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('Index'))








class BlogList(ListView):
    context_object_name='blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    # queryset =Blog.objects.order_by('-publish_date')


@login_required
def blog_details(request, slug):
    blog =Blog.objects.get(id=slug)
    all_blogs = Blog.objects.all().order_by('-publish_date')[:10]
    comment_form = CommentForm()

    if request.method == 'POST':
         comment_form = CommentForm(request.POST)
         if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':slug}))

    return render(request, 'App_Blog/blog_details.html',context={'blog':blog, 'comment_form':comment_form})






