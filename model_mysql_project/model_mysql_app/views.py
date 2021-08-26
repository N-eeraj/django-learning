from django.shortcuts import redirect, render
from .models import FormTable

# Create your views here.
def home(request):
    status = request.session.get('status', 404)
    request.session['status'] = 404

    return render(request, 'index.html', {'status': status})

def save(request):

    new_person =  FormTable()
    
    new_person.name = request.POST['name']
    new_person.phone = request.POST['num']
    new_person.mail = request.POST['mail']
    new_person.gender = request.POST['sex']
    new_person.dev = 'Developer' if request.POST.get('dev', False) == 'on' else '-'

    new_person.save()

    request.session['status'] = 200
    return redirect("/")

def data(request):
    data = FormTable.objects.all()
    return render(request, 'data.html', {'table': data})