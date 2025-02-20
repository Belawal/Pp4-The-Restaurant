from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello! This is the Booking app.</h1><p>Book a your table</p>")