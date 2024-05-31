from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return render(request, "index.html")
 
def postuser(request):
    checked_items = request.POST.getlist("item_checkbox")
    return HttpResponse(f"<h2>Selected: {checked_items}</h2>") 


# Create your views here.
