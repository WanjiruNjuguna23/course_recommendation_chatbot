from django.contrib import admin

# Register your models here.

from .models import Course, Interest

# Register the Course model for admin interface
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']  # Display these fields in the admin list view
    search_fields = ['name']  # Enable search by course name


