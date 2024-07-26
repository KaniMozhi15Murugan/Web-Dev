from django.urls import path
from . import views


urlpatterns = [
    path("", views.register, name='register')
    # other paths within your app
]
