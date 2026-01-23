from django.http import HttpResponse
from django.urls import path

def index(request):
    return HttpResponse("Hello, Namratha Garu! this is your new jenkins session! sivasoma")

urlpatterns = [
    path("", index),
]
