from django.contrib import admin
from django.urls import path
from django.conf import settings
from slideshow import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('ResearchPapers',views.ResearchPapers,name='ResearchPapers'),
    path('Achievements',views.Achievements,name='Achievements'),
    path('Team',views.Team,name='Team'),
    path('submitFeedback/', views.submitFeedback, name='submitFeedback'),
]