from django.urls import re_path as url
from ABCAPP import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^abcclient$', views.abcclientApi),
    url(r'^abcclient/([0-9]+)$', views.abcclientApi),
    url(r'^abcResource', views.abcResourceApi),
    url(r'^abcResource/([0-9]+)$', views.abcResourceApi),
    url(r'^accessLog', views.accessLogApi),
    url(r'^accessLog/([0-9]+)$', views.accessLogApi),
    url(r'^address$', views.addressApi),
    url(r'^address/([0-9]+)$',views.addressApi),
    url(r'^contact$', views.contactApi),
    url(r'^contact/([0-9]+)$', views.contactApi),
    url(r'^inventory', views.resourceTypeApi),
    url(r'^inventory/([0-9]+)$', views.resourceTypeApi),
    url(r'^resourceType', views.resourceTypeApi),
    url(r'^resourceType/([0-9]+)$', views.resourceTypeApi),
    url(r'^storagetype', views.storagetypeApi),
    url(r'^storagetype/([0-9]+)$', views.storagetypeApi)
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
