from django.http import HttpResponse
from zakladnik import settings
from os.path import join

def index(request, name):
    response = HttpResponse(content_type = "application/octet-stream")
    path = join(settings.BASE_DIR ,'fonts' , settings.STATIC_URL[1:], 'fonts', name)
    with open(path, 'r') as f: response.content = f.read()

    return response