from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Root URL handling
    path('admin/', admin.site.urls),
    path('api/', include('onepte.urls')),  # Include URLs from the `onepte` app
]
