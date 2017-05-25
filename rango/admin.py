from django.contrib import admin

from rango.models import Category, Page, UserProfile


class PageModel(admin.ModelAdmin):
    # fields = ['title', 'category', 'url'] the fields which we can edit in administration
    list_display = ['title', 'category', 'url']


class CategoryModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class UserProfileModel(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Category, CategoryModel)
admin.site.register(Page, PageModel)
admin.site.register(UserProfile, UserProfileModel)
