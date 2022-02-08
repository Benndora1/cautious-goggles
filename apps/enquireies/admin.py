from django.contrib import admin


from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
# Register your models here.

    list_display = ('name', 'email',  'message', 'phone_number', 'created_at')

admin.site.register(Enquiry)