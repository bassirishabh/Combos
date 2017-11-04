from django.conf.urls import url
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name='offers'
urlpatterns = [
    url(r'^$',views.offer, name='offer'),
    url(r'^add/',views.AddList, name='add'),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)