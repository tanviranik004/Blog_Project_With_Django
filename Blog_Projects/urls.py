
from django.contrib import admin
from django.urls import conf, path, include
from . import views 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('', views.Index, name='Index')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)