from django.shortcuts import render
from .models import FormTable

# Create your views here.
def home(request):
    return render(request, 'index.html')

def save(request):

    new_person =  FormTable()
    
    new_person.name = request.POST['name']
    new_person.phone = request.POST['num']
    new_person.mail = request.POST['mail']
    new_person.gender = request.POST['sex']
    new_person.dev = 'Developer' if request.POST.get('dev', False) == 'on' else '-'

    new_person.save()

    return home(request)

def data(request):
    data = FormTable.objects.all()
    return render(request, 'data.html', {'table': data})