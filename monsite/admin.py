from django.contrib import admin

# Register your models here.

from .models import Article, Client, TrainingProgram

admin.site.register(Article)

admin.site.register(TrainingProgram)

admin.site.register(Client)