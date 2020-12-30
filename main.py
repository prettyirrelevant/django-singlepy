import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from django.utils.crypto import get_random_string

# DEBUG is true here because i have no intentions of making it live
settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF=__name__,
    SECRET_KEY=get_random_string(60),
)


def index(request):
    return HttpResponse("Hello from Django!")


def facts(request):
    return HttpResponse("Regardless, Flask is bae(might change in future)")


urlpatterns = [path("", index), path("facts/", facts)]

app = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

# Note this approach gets cumbersome as project complexity increases
# Also, this is just to imitate flask single module to spin up a web project
