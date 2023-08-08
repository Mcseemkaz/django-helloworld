from django.http import HttpResponse
from datetime import datetime

now = datetime.now()


def index(request):
    return HttpResponse("Hello, world! UPD SEVEN  Its time " + now.strftime("%H:%M:%S"))
