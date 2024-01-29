from django.shortcuts import render
from django.http import HttpResponseForbidden

class PasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('authenticated') and request.path != '/login/' and request.POST.get('password') != '123456':
            # Redirect to the password_protected.html page
            return render(request, 'home/password_protected.html')

        response = self.get_response(request)
        return response
