from django.contrib import admin
from .models import Profile, Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_at']


admin.site.register(Profile)
# admin.site.register(Tweet)
