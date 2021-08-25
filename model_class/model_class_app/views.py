from django.shortcuts import render
from .models import Hero

# Create your views here.
def home(request):
    tony = Hero("Tony Stark", "Iron Man", "I am Iron Man", "stark.jpg")
    steve = Hero("Steve Rogers", "Captain America", "I can do this all day", "rogers.jpg")
    thor = Hero("Thor Odinson", "Thor", "Bring me Thanos", "odinson.jpg")
    bruce = Hero("Bruce Banner", "Hulk", "I'm always angry", "banner.jpg")
    natasha = Hero("Natasha Romanoff", "Black Widow", "", "romanoff.jpg")
    clint = Hero("Clint Barton", "Hawkeye", "I never miss", "barton.jpg")

    heros = [tony, steve, thor, bruce, natasha, clint]
    return render(request, 'index.html', {'heros': heros})