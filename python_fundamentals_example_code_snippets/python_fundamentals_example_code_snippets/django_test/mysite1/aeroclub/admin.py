from django.contrib import admin

# Register your models here.
from .models import AeroClub,Post,Url

admin.site.register(AeroClub)
admin.site.register(Post)
admin.site.register(Url)