from django.shortcuts import render
from django.http import HttpResponse


def headTracker(request):
    return render(request, 'headTracker.html')


def trackingjs(request):
    return render(request, 'trackingjs.html')


def clmTrackr(request):
    return render(request, 'clmTrackr.html')



def index(request):
    return render(request, 'index.html')
