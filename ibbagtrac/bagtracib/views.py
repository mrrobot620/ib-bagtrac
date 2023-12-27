from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from reportlab.lib.pagesizes import landscape
# from .models import Data , Cage , Bags 
from django.utils import timezone
from django.db import IntegrityError
import pytz
import csv
from pytz import timezone as pytz_timezone
import os
from io import BytesIO
from django.shortcuts import get_object_or_404
import qrcode
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Cage, Data 
import uuid
from reportlab.pdfgen import canvas
from django.core.files.storage import default_storage
from django.conf import settings
import os
from io import BytesIO
import qrcode
from PIL import ImageDraw
from PIL import ImageFont
from reportlab.pdfgen import canvas

IST = pytz_timezone('Asia/Kolkata') 
# @login_required
def home(request):
    if request.user.is_authenticated:
        return render(request , 'home.html')
    else:
        return render(request , 'login.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            return render(request , 'login.html' , {'error': "Invalid Username or Password"})
    return render(request , 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def search(request):
    return redirect('home')
