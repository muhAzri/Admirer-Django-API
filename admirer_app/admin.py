from django.contrib import admin
from admirer_app.models import Secret_Messages

# Register your models here.

class message_admin(admin.ModelAdmin):
    list_display = ['id', 'recipient', 'message', 'date']
    search_display = ['id', 'recipient', 'message', 'date']
    list_filter = ['recipient', 'date']

admin.site.register(Secret_Messages, message_admin)
