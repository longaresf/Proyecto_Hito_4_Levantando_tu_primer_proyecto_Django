from django.contrib import admin
from web_app.models import Flan, ContactForm

# Register your models here.

admin.site.register(Flan)
admin.site.register(ContactForm)

# class FlanAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price')
#     search_fields = ['name']
    
# @admin.action(description='Mark as new')
# def mark_as_new(modeladmin, request, queryset):
#     """ Mark selected flans as new"""
#     # This is a simple way to show how you can create custom actions.
#     # In more complex scenarios, you might want to use the Django messages framework (https://docs.djangoproject.com/en
#     # For more complex actions, you should use CustomAction or contribute.admin.SimpleListFilter
#     for flan in queryset:
#         flan.is_new = True
#         flan.save()
# mark_as_new.short_description = "Mark selected flans as New"   # short description of the action (up to 50 characters)

