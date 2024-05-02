from django.db import models
from django.utils import timezone
from django.db.models import Count


class KgnBrand(models.Model):
    name = models.CharField(max_length=200)
    volume_Value = models.DecimalField(max_digits=10, decimal_places=2)
    volume_Unit = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PLCData(models.Model):
    
    plant_1 = models.CharField(max_length=600)
    plant_2 = models.CharField(max_length=600)
    roll_Up = models.CharField(max_length=600)
    rotation_Drum = models.CharField(max_length=600)
    pmp = models.CharField(max_length=600)
    hydraulic = models.CharField(max_length=600)
    yv_Fwbw = models.CharField(max_length=600)
    field = models.CharField(max_length=20)

    def __str__(self):
        return f"PLCData {self.id}"

class PLCIO(models.Model):
    
    name = models.CharField(max_length=400)
    unit = models.CharField(max_length=8)
    value =models.IntegerField()

    def __str__(self):
        return f"PLCIO : {self.id}"
      
class Machine(models.Model):
    kgnbrand = models.ForeignKey(KgnBrand, on_delete=models.CASCADE)
    plcdata = models.ForeignKey(PLCData, on_delete=models.CASCADE)
    plcio = models.ForeignKey(PLCIO, on_delete=models.CASCADE)
    machine_Name = models.CharField(max_length=200)
    status = models.IntegerField()
    waste = models.CharField(max_length=200)
    start_Available = models.DateField()
    end_Available = models.DateField()
    province = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postal_Code = models.CharField(max_length=20)
    Country = models.CharField(max_length=200)

    

    
    @classmethod
    def count_machines_by_status(cls):
        return cls.objects.values('status').annotate(Machines=Count('status'))
    
    
    class Meta:
        ordering = ['machine_Name']

    
class User(models.Model):
    name = models.CharField(max_length=200)
    card_Number = models.BigIntegerField()
    email = models.EmailField()
    last_Access = models.DateTimeField(auto_now_add=True, blank=True)
    phone_Number = models.BigIntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MachineOrder(models.Model):
    name = models.CharField(max_length=200)
    order_Date = models.DateField()
    delivery_Date = models.DateField()
    brand_name = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Router(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model

    sim_Card = models.DecimalField(max_digits=18, decimal_places=0)
    mac_Address = models.CharField(max_length=100)
    ip_Address = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    version = models.FloatField(null=True, blank=True, default=None)




class UserMachine(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Machine is another model

    def __str__(self):
        return f"UserMachine : {self.id}"
    
class EventLog(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Machine is another model
    event_Change = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"EventLog {self.id}"

class Alarm(models.Model):
    name = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    threshold = models.CharField(max_length=100)
    threshold_Type = models.BooleanField(default=False)
    on_Delay = models.FloatField()
    operator_Instruction = models.CharField(max_length=255)
    access_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Machine is another model
    alarm = models.ForeignKey(Alarm, on_delete=models.CASCADE)  # Assuming Machine is another model
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_Time = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.IntegerField()

    def __str__(self):
        return f"Message : {self.id} "   



class UsersGroup(models.Model):
    card_Number = models.JSONField(default=list)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name