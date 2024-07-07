from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('criminal_list', views.criminal_list.as_view(), name='top_criminals'),
    path('criminal', views.criminal.as_view(), name='criminals_list'),
    path('contact', views.contact, name='contact'),
    path('profile/firview/-user', views.Firview.as_view(), name='firview'),
    path('Write-FIR', login_required(views.FIR.as_view()), name='FIR'),
    path('login/password-reset', views.password_reset, name='password_reset'),
    path('profile/<int:pk>/delete', views.DeleteProfile, name='deleteprofile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
