from django.contrib import admin
from .models import Staff, Attendance

@admin.register(Staff)
class StassAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'salary')


@admin.register(Attendance)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'status')
    list_filter = ('status', 'date')

