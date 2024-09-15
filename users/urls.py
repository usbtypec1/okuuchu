from django.urls import path

from users.views import UserCreateApi

urlpatterns = [
    path('users/', UserCreateApi.as_view(), name='user-create'),
]
