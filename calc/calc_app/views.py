from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "calc.html")

def add(request):
    num1, num2 = int(request.POST['num1']), int(request.POST['num2'])
    sum = num1 + num2
    return render(request, 'result.html', {'result': sum})