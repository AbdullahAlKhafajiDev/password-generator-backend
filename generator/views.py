from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thePassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length'))

    if (request.GET.get('specialcharacters')):
        characters.extend('<>:"{}_+()&*%^#$!@~?,./;[]-=\|')

    if (request.GET.get('numbers')):
        characters.extend(list('1234567890'))

    if (request.GET.get('uppercase')):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    for i in range(length):
        randomChoice = random.choice(characters)
        thePassword += randomChoice

    return render(request, 'generator/password.html', {'password':thePassword})

def about(request):
    return render(request, 'generator/about.html')