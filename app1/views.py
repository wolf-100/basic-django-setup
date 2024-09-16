from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    person = {
        "name": "Yogita", 
        "city": "Pune",
        "marks": [98, 99, 97, 100]
    }
    return render(request, "app1/index.html", person)