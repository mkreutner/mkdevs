from django.contrib import admin

from .models import ContactMessage

# Custom admin models
class ContactMessageAdmin(admin.ModelAdmin):
    
    list_diplay = ['name','email','message','is_read','is_treated','created_date',]
    search_fields = ['name','email',]

    readonly_fields = ['name','email','message','created_date',]


# Models and admin models registration
admin.site.register(ContactMessage, ContactMessageAdmin)
