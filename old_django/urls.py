from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^about/', include('about.urls')),
    url('^catalog/', include('catalog.urls')),
    url('^auth/', include('users.urls')),
    url('^', include('homepage.urls')),
]
