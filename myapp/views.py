from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def home(request):
    return HttpResponse("<h1>This is first app</h1>")

from django.shortcuts import render

def show_profile(request, name, age):
    books = Book.objects.all()
    context = {'name': name.capitalize(), 'age': age, 'books':books}
    return render(request, 'profile.html', context)
