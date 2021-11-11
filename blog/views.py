from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
from . team import teamset

def home(request):
    print("hello")
    # sampling with replacement

    context = teamset()
    print(len(context))

    x = len(context)

    while(x <= 0):
        print(x)
        context = teamset()
        x = len(context)
    
    return render(request, 'blog/home.html')


# AJAX
def load_teams(request):
    context = teamset()
    print(len(context))

    x = len(context)

    while(x <= 0):
        print(x)
        context = teamset()
        x = len(context)
    
    return render(request, 'blog/teams.html', context)
	# return JsonResponse(list(schadules.values('title')), safe=False)

