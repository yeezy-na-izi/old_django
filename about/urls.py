from django.conf.urls import url
from about import views

urlpatterns = [
    url('^$', views.description, name='about_page')
]