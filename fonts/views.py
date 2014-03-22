from django.http import HttpResponse
from zakladnik import settings
import os

def index(request, name):
    response = HttpResponse(content_type = "application/octet-stream")
    path = os.path.join(settings.BASE_DIR ,'fonts' , settings.STATIC_URL[1:], 'fonts', name)
    f = open(path)
    response.content = f.read()
    f.close()

    return response