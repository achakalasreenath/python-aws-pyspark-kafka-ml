from django.shortcuts import render,redirect

def welcome(request):
    if request.user.is_authenticated :
        return redirect("club_home")
    else:
        return render(request, "welcome.html")