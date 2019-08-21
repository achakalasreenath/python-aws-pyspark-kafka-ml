from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .models import AeroClub,Url

def feed(request):
    return render(request,"aeroclub/feed.html",{"urls":Url.objects.all()})

@login_required
def home(request):
    return render(request, "aeroclub/home.html", {"club":AeroClub.objects.get(club_name = "Aerounwired"),"urls":AeroClub.objects.urls_of_club('Aerounwired')})

@login_required
def posts(request):
    return render(request, "aeroclub/posts.html", {"club": AeroClub.objects.get(club_name="Aerounwired"),
                                                  "urls": AeroClub.objects.urls_of_club('Aerounwired')})