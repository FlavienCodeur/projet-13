from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

from profiles.views import index, profile

app_name = 'profiles'
urlpatterns = [
    path('profiles/', index, name='index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('sentry-debug/', trigger_error),
    
]
