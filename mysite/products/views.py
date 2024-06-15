from django.shortcuts import render

# Create your views here.
def home_view(request):
    print(request)
    return render(request, "products/index.html")