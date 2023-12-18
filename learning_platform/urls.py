# learning_platform/urls.py
from django.contrib import admin
from django.urls import path, include  # Make sure to include 'include'
from users.views import login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_user, name='login'),
    path('users/', include('users.urls')),
    path('learning_app/', include('learning_app.urls')),
    path('api/', include('learning_app.api_urls')),

]

