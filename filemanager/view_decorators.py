from decorator import decorator
from django.http import HttpResponse


@decorator
def post_only(f, request):
    """ Ensures a method is post only """
    if request.method != "POST":
        response = HttpResponse("POST requests required.")
        response.status_code = 500
        return response
    return f(request)