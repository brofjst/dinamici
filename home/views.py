from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@login_required(login_url='/authentication/login/')
def index(request):
    return render(request, 'home/index.html', {})