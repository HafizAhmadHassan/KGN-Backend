from django.contrib import admin

# Register your models here.

from .models import Question,KGN_Brand, Machine,Alarm,PLCConfigIO,PLCConfiguration

admin.site.register(Question)
admin.site.register(KGN_Brand)
admin.site.register(Machine)
admin.site.register(Alarm)
admin.site.register(PLCConfiguration)
admin.site.register(PLCConfigIO)