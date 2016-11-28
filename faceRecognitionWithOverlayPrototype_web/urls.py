from django.conf.urls import url
from faceRecognitionWithOverlayPrototype_web import views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^ping$', views.ping),
    url(r'^$', views.hello_world)
    ]
