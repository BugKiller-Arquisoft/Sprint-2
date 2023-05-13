from django.shortcuts import render
from widmy.auth0backend import getRole
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'index.html')