from django.http import HttpResponse
from django.urls import path

def index(request):
    return HttpResponse("Hello, Namratha Garu!")

urlpatterns = [
    path("", index),
]
