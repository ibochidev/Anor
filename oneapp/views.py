from django.shortcuts import render, redirect

from .models import Car


def base(request):
    return render(request, 'base.html')


def index(request):
    car = Car.objects.all()
    ctx = {
        'car': car
    }
    return render(request, 'index.html', ctx)


def createCar(request):
    if request.POST:
        car = Car()
        car.name = request.POST.get('nomi')
        car.color = request.POST.get('ranggi')
        car.year = request.POST.get('yili')
        car.image = request.POST.get('image')
        car.save()
        return redirect('index')
    return render(request, 'create.html')