from django.contrib import admin
from service.models import servicePageSEO  # Use the correct case (lowercase)

@admin.register(servicePageSEO)  # Use the correct case (lowercase)
class ServicePageSEOAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'meta_description')  # Customize the admin interface
    search_fields = ('meta_title',)  # Add search functionality