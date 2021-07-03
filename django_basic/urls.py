# django_basic
from django.urls import path
from django_basic import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_word')
]
