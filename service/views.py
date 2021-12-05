from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from service.models import CarService
from .forms import NameForm
# Create your views here.
def index(request):
    if request.method == "GET":
        form = NameForm()
        maps = CarService.objects.all()
        return render(request, 'homepage.html', {'form': form, 'maps': maps,})
    elif request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid:
            return HttpResponse('thanks')