from django.urls import path
from .views import home_view, about_view, contact_view, profile

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('profile/', profile, name='profile'),
]
