from django.urls import path

# model from documentation : https://docs.djangoproject.com/fr/4.1/topics/http/urls/#url-namespaces
# from . import views

# app_name = 'polls'
# urlpatterns = [
#    path('', views.IndexView.as_view(), name='index'),
#    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#    ...
# ]

from lettings.views import index as lettings_index
from lettings.views import letting


urlpatterns = [
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
]