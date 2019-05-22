from django.contrib import admin

# Register your models here.
from .models import (
    Course,
    Teacher,
    Student,
    Cycle,
    CycleTime,
    Room,
    Subscription
)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    exclude = ['middle_name']
    list_display=['first_name','last_name','age']
    list_filter=['first_name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ['course','from_date','to_date']


@admin.register(CycleTime)
class CycleTimeAdmin(admin.ModelAdmin):
    list_display = ['cycle','weekday','from_hour','to_hour','teacher','room']



admin.site.register(Room)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['student','cycle','registered_date']