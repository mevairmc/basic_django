# django_basic
from django.urls import path
from django_basic import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_word'),
    path('sorted/', views.hi, name="hi"),
    path('say_hi/<str:name>/<int:age>/', views.say_hi)
]
