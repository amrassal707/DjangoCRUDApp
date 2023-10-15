from django.shortcuts import HttpResponse
from django import views
from .models import student
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 

# Create your views here.
class myView(views.View):
    def get(request):
        students= student.objects.all().values()
        return HttpResponse(students)
    @csrf_exempt 
    def post(request):
        student1= student()
        student1.name = request.POST.get('name')
        student1.age= request.POST.get('age')
        print(student1.name)
        print(student1.age)
        student1.save()
        return HttpResponse('saved successfully')
    @csrf_exempt
    def put(request, pk):
        try:
            existing_student = student.objects.get(pk = pk)
            tutorial_data = JSONParser().parse(request) 
            try:
                existing_student.name= tutorial_data['name']
                existing_student.age= tutorial_data['age']
                existing_student.save()
            except:
                return HttpResponse("data is missing, please provide all data")
                
        except student.DoesNotExist:
            return HttpResponse('student not found please try with diffrent id')
        return HttpResponse(existing_student)
       
    @csrf_exempt   
    def delete(request, pk):
        try:
            existing_student= student.objects.get(pk = pk)
            existing_student.delete()
        except student.DoesNotExist:
            return HttpResponse('student not found or recently deleted, please try a different id')
        return HttpResponse('deleted successfully')
    
    