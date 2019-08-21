from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home,posts,feed

urlpatterns =[
    url(r'home', home, name = 'club_home'),
    url(r'posts', posts),
    url(r'feed',feed, name ="club_feed"),
    url(r'login',LoginView.as_view(template_name = "aeroclub/login.html"), name='club_login'),
    url(r'logout',LogoutView.as_view(),name = 'club_logout')
]

