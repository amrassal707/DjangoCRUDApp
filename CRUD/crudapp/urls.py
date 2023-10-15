from django.urls import path
from . import views
from .models import student

urlpatterns = [
    path('readallstudents/' , views.myView.get),
    path('addstudent/' , views.myView.post),
    path('updatestudent/<int:pk>', views.myView.put),
    path('delete/<int:pk>', views.myView.delete),
]
