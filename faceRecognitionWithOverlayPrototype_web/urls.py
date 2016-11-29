from django.conf.urls import url
from faceRecognitionWithOverlayPrototype_web import views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^headTracker', views.headTracker),
    url(r'^trackingjs', views.trackingjs)
    ]
