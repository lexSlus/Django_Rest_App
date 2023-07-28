from django.contrib import admin
from .models import Restaurant, Menu, MenuVote

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuVote)
