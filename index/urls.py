
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('filter_gallery', filter_gallery, name='filter_gallery'),
    path('contact', contact_form, name='contact'),
]
