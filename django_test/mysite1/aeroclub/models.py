from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class AeroClubManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(club_status="A")


class AeroClubQuerySet(models.QuerySet):
    def posts_of_club(self,clubname):
        club = AeroClub.objects.get(club_name = clubname)
        return club.post_set.all()
    def urls_of_club(self, clubname):
        club = AeroClub.objects.get(club_name=clubname)
        urls = []
        for post in club.post_set.all():
            post = Post.objects.get(post_id = post.post_id)
            for url in post.url_set.all():
                urls.append(url)
        return urls



class AeroClub(models.Model):
    STATUS_CHOICES = [("A", "Active"), ("INA", "Inactive")]
    user = models.ForeignKey(User, related_name="user_of_club", on_delete=models.CASCADE, default=1)
    club_id = models.CharField(max_length=6, primary_key=True)
    club_name = models.CharField(max_length=255)
    club_secretary = models.CharField(max_length=255)
    club_status = models.CharField(max_length=2, default="INA", choices=STATUS_CHOICES)
    # objects = AeroClubQuerySet.as_manager()
    objects = AeroClubManager.from_queryset(AeroClubQuerySet)()

    def __str__(self):
        return self.club_name


class Post(models.Model):
    post_id = models.CharField(max_length=6, primary_key=True)
    post_content = models.CharField(max_length=2000)
    post_likes = models.IntegerField(default=0)

    club = models.ForeignKey(AeroClub, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_content


class Url(models.Model):
    url = models.URLField(max_length=2000)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return self.url
