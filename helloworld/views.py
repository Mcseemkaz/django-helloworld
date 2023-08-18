from django.http import HttpResponse
from datetime import datetime


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def index(request):
    return HttpResponse("Hello, world! UPD DEVELOPES  Its time " + get_current_time())
