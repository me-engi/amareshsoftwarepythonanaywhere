from django.urls import path
from home.views import *

urlpatterns = [
    path('' , homePageFront, name='homePageFront'),
]
