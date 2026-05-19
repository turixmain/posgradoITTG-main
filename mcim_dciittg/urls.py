"""mcim_dciittg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# utils
from django.conf import settings
from django.conf.urls.static import static

# Views from users
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView


urlpatterns = [
    path('', include('apps.investigadores.urls')),
    path('', include('apps.slides.urls')),
    path('', include('apps.posgrados.urls')),
    path('', include('apps.colaboraciones.urls')),
    path('', include('apps.tesis.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='components/registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='components/registration/logout.html'), name='logout'),
    path('accounts/password-change/', PasswordChangeView.as_view() ,name='password_change'),
    path('accounts/password-change/done/', PasswordChangeDoneView.as_view() ,name='password_change_done'),
    path('accounts/password-reset/', PasswordResetView.as_view(template_name='components/registration/password_reset.html', 
        email_template_name='components/registration/password_reset_email.html',
        subject_template_name='components/registration/password_reset_subject.txt'), name='password-reset'),
    path('accounts/password-reset/done/', PasswordResetDoneView.as_view(template_name='components/registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='components/registration/password_reset_confirm.html') ,name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(template_name='components/registration/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


