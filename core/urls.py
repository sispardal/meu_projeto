from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("SITE ONLINE 🚀")

urlpatterns = [
    path('', home),
]