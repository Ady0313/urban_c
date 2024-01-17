# tryon/urls.py
from django.urls import path
from .views import home, try_on_api

urlpatterns = [
    path('', home, name='home'),  # Include this line for the root URL
    path('try-on-api/', try_on_api, name='try_on_api'),
    # ... other paths
]
