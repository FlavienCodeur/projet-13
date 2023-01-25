from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-profiles/', include('profiles.urls', namespace='all-profiles')),
    path('all-lettings/', include('lettings.urls', namespace='all-lettings')),
    path('admin/', admin.site.urls),
]
