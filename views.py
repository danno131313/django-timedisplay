from django.shortcuts import render
from django.utils.timezone import now, localtime
from time import strftime, localtime, gmtime
from datetime import datetime

# Create your views here.
def index(request):
    print(localtime(), gmtime())
    date = strftime("%b %d, %Y", localtime())
    time = strftime("%I:%M %p", localtime())
    print(now())
    context = {
        "date": date,
        "time": time,
    }
    return render(request, "timedisplay_app/index.html", context)
