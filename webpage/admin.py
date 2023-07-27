from django.contrib import admin

# Register your models here.

from .models import Student

@admin.register(Student)
class Admin(admin.ModelAdmin):
    list_display = ("std_id","name","prefix","lastname","phone")
    search_fields = ("std_id","name","prefix","lastname","phone")