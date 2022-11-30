from django.urls import re_path as url
from api import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^abcResource', views.abcResourceApi),
    url(r'^abcResource/([0-9]+)$', views.abcResourceApi),
    url(r'^inventory', views.inventoryApi),
    # add new entry here for inventory_id and point to function in views.py
    url(r'^inventory/([0-9]+)$', views.inventoryApi),
    url(r'^inventoryDDLX', views.inventoryDDLApi),
    url(r'^inventoryDDLX/([0-9]+)$', views.inventoryDDLApi),
    url(r'^resourceType', views.resourceTypeApi),
    url(r'^resourceType/([0-9]+)$', views.resourceTypeApi)
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)