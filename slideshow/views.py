from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import *
from django.http import JsonResponse

def index(request):
    slideshow = Slideshow.objects.all().values()
    return render(request,'Index.html',{'slideshow': slideshow})

def ResearchPapers(request):
    paper=Research.objects.all().values()
    return render(request,'ResearchPapers.html',{'papers': paper})

def Achievements(request):
    achievements=Achievement.objects.all().values()
    return render(request,'Achievements.html',{'achievements': achievements})


def Team(request):
    team1=team.objects.all().values()
    return render(request,'OurTeam.html',{'team1': team1})


def submitFeedback(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        message=request.POST.get('message')
        feedbackinsertid = Feedback.objects.create(email=email,message=message)
        print(feedbackinsertid)
    return render(request, 'index.html')