from django.urls import path, include
from . import views
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='home.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='User/login.html'), name='login'),
    path('profile/', login_required(views.profile.as_view()), name='profile'),
    path('UploadImage/', views.UploadImage, name='uploadimage'),
    path('UpdateProfile/', views.UpdateProfile, name='updateprofile'),
    path('send_otp/', views.send_otp, name='send_otp'),
    path('mailsending/', views.mailsending, name='mailsending'),
    path('Varify/', views.Varify, name='varify'),
    path('social-auth/', include('social_django.urls', namespace='social')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
