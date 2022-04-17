from django.urls import path
from .views import dashboard, profile_list, _profile

app_name = 'tweets'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/list/', profile_list, name='profile_list'),
    path('profile/<slug:slug>', _profile, name='profile'),
]
