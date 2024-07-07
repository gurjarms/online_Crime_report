
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Crime_Report import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('Crime_Report.urls')),
    path('', include('Users.urls')),
    path(r'^404/$', views.page_not_found)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
