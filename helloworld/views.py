from django.http import HttpResponse
from datetime import datetime

now = datetime.now()


def get_current_time():
    return now.strftime("%H:%M:%S")


def index(request):
    return HttpResponse("Hello, world! UPD SEVEN  Its time " + get_current_time())
