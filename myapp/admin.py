from django.contrib import admin
from .models import Student

admin.site.site_header = "Student Management System"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome Admin"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('age',)

