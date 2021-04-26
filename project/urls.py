
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),

    #url(r'^forum/', include('django_forum_app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)