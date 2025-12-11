# home/admin.py
from django.contrib import admin
from .models import AllowedUser, Card

@admin.register(AllowedUser)
class AllowedUserAdmin(admin.ModelAdmin):
    list_display = ("name", "anniversary")

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("slot", "title")
    list_editable = ("title",)
    ordering = ("slot",)
