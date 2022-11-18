from django.urls import re_path as url
from ABCAPP import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^address$', views.addressApi),
    url(r'^address/([0-9]+)$',views.addressApi),
    url(r'^contact$', views.contactApi),
    url(r'^contact/([0-9]+)$', views.contactApi),
    url(r'^abcclient$', views.abcclientApi),
    url(r'^abcclient/([0-9]+)$', views.abcclientApi)
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)