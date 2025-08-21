from django.http import HttpResponse

def home(request):
    return HttpResponse("Charlie Saleh here in Django, Hello!")
