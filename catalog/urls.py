from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.item_detail, name='product_page'),
    url(r'^$', views.item_list, name='all_products'),
]
