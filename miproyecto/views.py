import datetime
from time import strftime
from django.shortcuts import render
from datetime import date
from django.utils import timezone


def index(request):
    day  = timezone.now()
    hour = timezone.now()
    #formatedHour = hour.strftime("%Y/%m/%d %H:%M:%S")
    formatedDay  = strftime("%d/%m/%Y")
    formatedHour = strftime("%r")
    # today = date.today()
    # fecha = today.strftime("%B %d, %Y")
    # hora = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
    context = {
    'fecha': formatedDay,
    'hora': formatedHour,
    }
    return render(request, 'index.html', context)