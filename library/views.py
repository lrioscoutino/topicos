from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    return HttpResponse("<h1>Hola desde Http</h1>")

def second_view(request):
    name = "Luis Rios"
    age = 47
    number_list = [3,4,5,68,1,4,9,0]
    context = {
        "name": name,
        "age": age,
        "number_list":number_list
    }
    return render(request,"index.html", context=context)
