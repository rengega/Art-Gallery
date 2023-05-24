from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')   #the vew passes the rendered request to the template
def contact(request):
    return render(request, 'core/contact.html')