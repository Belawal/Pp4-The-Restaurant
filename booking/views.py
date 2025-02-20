from django.http import HttpResponse

def home(request):
    return render(request, 'booking/home.html')# Renders the homepag