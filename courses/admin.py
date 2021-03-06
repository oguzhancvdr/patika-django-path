from django.contrib import admin
from . models import Category, Course, Tag


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'teacher')
    list_filter = ('available', 'date')
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name', )}