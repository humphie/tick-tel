from django.contrib import admin
from tick.models import *



#class for Creditz
class CreditAdmin(admin.ModelAdmin):
    list_display = ('name', 'credit')

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('username', 'contact')


class EventAdmin(admin.ModelAdmin):
    list_display = ('owner', 'description')

class memberAcountAdmin(admin.ModelAdmin):
    list_display = ('owner', 'username', 'position')

class ReportAdmin(admin.ModelAdmin):
    list_display =('username', 'message')

class InboxAdmin(admin.ModelAdmin):
    list_display =('sender', 'recipient', 'message')


admin.site.register(Credit, CreditAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(memberAcount, memberAcountAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Inbox, InboxAdmin)

