from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail, name='user_page'),
    url(r'^users/$', views.user_list, name='users_page'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile_page'),
]
