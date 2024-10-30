"""
URL configuration for travelmanagement project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
    path('submit_passport/', views.submit_passport, name='submit_passport'),
    path('submit_second_passport/', views.submit_second_passport, name='submit_second_passport'),
    path('submit_visa/', views.submit_visa, name='submit_visa'),  # Ensure this URL pattern exists
    path('submit_extended_visa/', views.submit_extended_visa, name='submit_extended_visa'),
    # other URL patterns
]