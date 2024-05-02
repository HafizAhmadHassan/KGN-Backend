
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.db.models import Count

# Register your models here.

from .models import *

"""
class MachineAdmin(admin.ModelAdmin):
    list_display = ['machine_Name','status','waste', 'Country']
    list_editable = ['status']
    list_per_page = 10

"""



from django.contrib import admin

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):

    list_display = ['machine_Name','status','waste', 'Country']
    list_editable = ['status']
    list_per_page = 10
    def get_Brand_Name(self, obj):
        return obj.user.email


    



admin.site.register(KgnBrand)
admin.site.register(MachineOrder)
admin.site.register(Router)
admin.site.register(PLCData)
admin.site.register(PLCIO)

admin.site.register(User)
admin.site.register(UserMachine)
admin.site.register(EventLog)


class MessageAdmin(admin.ModelAdmin):

    list_display = [ 'get_Message','get_MachineName','get_Users','get_UsersCategory','get_UsersEmail','alarm','description']
    

    list_per_page = 10

    def get_UsersEmail(self, obj):
        return obj.user.email
    def get_Message(self, obj):
        return obj.id
    def get_Users(self, obj):
        return obj.user.name
    def get_UsersCategory(self, obj):
        return obj.user.category
    def get_MachineName(self, obj):
        return obj.machine.machine_Name
#    get_author.short_description = 'Author'
#    get_author.admin_order_field = 'book__author'
admin.site.register(Message,MessageAdmin)

admin.site.register(Alarm)

"""
from .models import Question,KGN_Brand, Machine,Alarm,PLCConfigIO,PLCConfiguration

admin.site.register(Question)
admin.site.register(KGN_Brand)
admin.site.register(Machine)
admin.site.register(Alarm)
admin.site.register(PLCConfiguration)
admin.site.register(PLCConfigIO)

"""
