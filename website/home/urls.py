from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('Contact',Contact,name='Contact'),
    path('project',project,name='project'),
    path('gallery',Gallery,name='gallery'),
    path('Resume',Resume,name='Resume'),
]