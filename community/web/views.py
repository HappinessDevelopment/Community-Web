from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'auth/register.html')


def list_groups(request):
    groups = Group.objects.all().order_by('-name')
    return render(request, 'groups/list.html', {'groups': groups})