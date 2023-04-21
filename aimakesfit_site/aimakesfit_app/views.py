from django.shortcuts import render
from .models import Users

# Create your views here.
def inputformview(request):
    if request.method == 'POST':
        print(request.POST)
        user = Users()
        user.email = request.POST['email']
        user.age = request.POST['age']
        user.activity_level = request.POST['activity_level']
        user.allergies = request.POST['allergies']
        user.budget = request.POST['budget']
        user.dietary_preference = request.POST['dietary_preference']
        user.weight = request.POST['weight']
        user.height = request.POST['height']
        user.cooking_time = request.POST['cooking_time']
        user.fitness_goal = request.POST['fitness_goal']
        user.gender = request.POST['gender']
        user.location = request.POST['location']
        user.medical_conditions = request.POST['medical_conditions']
        user.save()
    return render(request,'index.html')
