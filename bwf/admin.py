
from django import forms
from django.contrib import admin

from bwf.models import User, Friend, Friendship, Debt

admin.site.register(User)


admin.site.register(Friend)


class FriendshipAdmin(admin.ModelAdmin):
    fields=('user', 'friend')

admin.site.register(Friendship, FriendshipAdmin)

admin.site.register(Debt)
# Register your models here.
