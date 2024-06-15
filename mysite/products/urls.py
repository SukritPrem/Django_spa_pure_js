from django.urls import path
from . import views

def catch_all_view(request, remaining_path):
    print(remaining_path)
    return HttpResponse(f"Unmatched path: {remaining_path}")

urlpatterns = [
    path('', views.home_view, name="index"),
]