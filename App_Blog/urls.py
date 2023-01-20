from django.urls import path
from App_Blog import views

app_name='App_Blog'

urlpatterns = [
   path('write/', views.CreateBlog.as_view(), name='create_blog'),
   path('', views.BlogList.as_view(), name='blog_list'),
   path('details/<str:slug> ', views.blog_details, name='blog_details'),
]



#    path('blog_detail/<str:slug>', views.blog_detail, name="blog_detail"),


