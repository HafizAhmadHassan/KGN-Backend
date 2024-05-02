from django.contrib import admin
import subprocess

# Register your models here.
from .models import *
import datetime as dt
from django.db import models 

from django.core.mail import send_mail
import smtplib

"""
class MachineAdmin(admin.ModelAdmin):
    list_display = ['machine_Name','status','waste', 'city']
    list_editable = ['status']
    list_per_page = 10

"""



@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):

    list_display = ['machine_Name','status','waste', 'city','days_since_operation']
    list_editable = ['status']
    list_filter = ['status','waste']
    search_fields = ['machine_Name']
    actions =['set_status_to_change']
    #fields = (('start_Available','end_Available'),'status')

    # Start Allow actions to specific users
    
    #https://stackoverflow.com/questions/38329999/permissions-to-django-admin-actions
    #https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#conditionally-enabling-or-disabling-actions
    
    # End Allow actions to specific users
    list_per_page = 10
    def get_Brand_Name(self, obj):
        return obj.user.email
    
    def set_status_to_change(self,request,queryset):
        count = queryset.update(status=1)
        self.message_user(request,'{} status changed'.format(count))
    set_status_to_change.short_description = 'Select Machines to Active '
    
    # del acrions to drivers
    def get_actions(self, request):
        actions = super(MachineAdmin, self).get_actions(request)
        if request.user.username[0].upper() == "D":
            if "set_status_to_change" in actions:
                del actions["set_status_to_change"]
        return actions
    
    def days_since_operation(self,obj):
        diff = dt.date.today() - obj.start_Available
        return diff.days
    

@admin.register(PLCIO)
class PLCIOAdmin(admin.ModelAdmin):
    change_form_template = "admin/change_form1.html"

    def response_change(self, request, obj):
        if "_change-signal" in request.POST:
            print("Hassan is here in Response change")
            #print(request.POST)

            matching_names_except_this = self.get_queryset(request).exclude(pk= obj.id)

            #matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            print(matching_names_except_this)

            match_one=self.get_queryset(request).get(pk=obj.id)

            another_way_match_one= self.get_queryset(request).filter(pk=obj.id).values()

            print("This is Full matched object Name ",match_one)
            #print("Another way match ",another_way_match_one)
            new_val=[]
            for each_obj in another_way_match_one:
                for name,vals in each_obj.items():
                    #print("vals : ",vals)
                    new_val.append(vals)
            id_obj=str(match_one)[len(str(match_one))-1]
            id_obj=new_val[0]

            print("This is matched one id ",id_obj)

            # now changing updating sql query by passing 
            #matching_names_except_this.delete()
            #obj.is_unique = True
            obj.save()
            print(" Data saved Automatically in Amazon")

            print(" Calling mySql_to_CSV to bring change in CSV File without passing id ")
            #self.message_user(request, "This villain is now unique")
            #return HttpResponseRedirect(".")
            print(str(new_val[1:]))
            id_len=len(str(new_val[0]))
            id_len = id_len*(-1)
            print("This is name if Class object",str(match_one)[:id_len-1])
            subprocess.run(['python3', 'mysql_to_csv_v2.py',str(match_one)[:id_len-1],str(new_val[1:])])
        return super().response_change(request, obj)


@admin.register(PLCData)
class PLCDataAdmin(admin.ModelAdmin):
    change_form_template = "admin/change_form1.html"

    def response_change(self, request, obj):
        if "_change-signal" in request.POST:
            print("Hassan is here in Response change")
            #print(request.POST)

            matching_names_except_this = self.get_queryset(request).exclude(pk= obj.id)

            #matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            print(matching_names_except_this)

            match_one=self.get_queryset(request).get(pk=obj.id)

            another_way_match_one= self.get_queryset(request).filter(pk=obj.id).values()

            print("This is Full matched object Name ",match_one)
            #print("Another way match ",another_way_match_one)
            new_val=[]
            for each_obj in another_way_match_one:
                for name,vals in each_obj.items():
                    #print("vals : ",vals)
                    new_val.append(vals)
            id_obj=str(match_one)[len(str(match_one))-1]
            id_obj=new_val[0]

            print("This is matched one id ",id_obj)

            # now changing updating sql query by passing 
            #matching_names_except_this.delete()
            #obj.is_unique = True
            obj.save()
            print(" Data saved Automatically in Amazon")

            print(" Calling mySql_to_CSV to bring change in CSV File without passing id ")
            #self.message_user(request, "This villain is now unique")
            #return HttpResponseRedirect(".")
            print(str(new_val[1:]))
            id_len=len(str(new_val[0]))
            id_len = id_len*(-1)
            print("This is name if Class object",str(match_one)[:id_len-1])
            subprocess.run(['python3', 'mysql_to_csv_v2.py',str(match_one)[:id_len-1],str(new_val[1:])])
        return super().response_change(request, obj)

admin.site.register(AlarmSetting)

admin.site.register(KgnBrand)
admin.site.register(MachineOrder)
admin.site.register(Router)


"""
class PLCDataModelForm( forms.ModelForm ):
    plant_1 = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = PLCData

class PLCData_Admin( admin.ModelAdmin ):
    form = PLCDataModelForm
"""


"""
from django.forms import TextInput, Textarea



class PLCIOAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':50, 'cols':30})},
        models.IntegerField: {'widget': Textarea(attrs={'rows':50, 'cols':10})},

        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ['name','unit','value']



admin.site.register(PLCIO,PLCIOAdmin)
"""





admin.site.register(User)
admin.site.register(UserMachine)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    change_form_template = "admin/change_form2.html"
    def response_change(self, request, obj):
        print("")
        if "_send-message" in request.POST:
            print("sent") 
            """
            content="Machine Sent a message"

            mail=smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            sender='ahmadhassan061@gmail.com'
            recipient='develop@kgn.it'
            mail.login('ahmadhassan061@gmail.com','jtjrwpaxovfqsgxv')
            header='To:'+ recipient +'\n'+'From:' \
            +sender+'\n'+'subject:testmail\n'
            content=header+content
            mail.sendmail(sender, recipient, content)
            mail.close()
            """
        
        """
        # Check this if there is problem 
        https://www.youtube.com/watch?v=g_j6ILT-X0k

        """
        return super().response_change(request, obj)

admin.site.register(MessageUser)

"""

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

"""



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
