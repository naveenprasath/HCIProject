
from django import forms
from django.contrib import admin

from bwf.models import User, Friend,  Bill

admin.site.register(User)


admin.site.register(Friend)


admin.site.register(Bill)
