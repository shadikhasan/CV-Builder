from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'login'
    
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout URL
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication routes
    path('', include('cvs.urls')),  # Include URLs from the 'cvs' app
]
