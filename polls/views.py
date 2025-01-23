from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to a Musta sauce sprinkle tutorial")