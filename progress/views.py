from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

# Create your views here.


def course_progress_tracking(request):
    
    courses=course_data.objects.filter(user_name=request.user)
    
    resp_dict=[]
    for c in courses:
        p=c.no_of_videos_completed/c.no_of_videos
        p*=100
        p=int(p)

        t={
            "course_title": c.title,
            "progress_value": p
        }
    
        resp_dict.append(t)
    
    return render(request, 'course_progress.html', {"resp_dict": resp_dict})


