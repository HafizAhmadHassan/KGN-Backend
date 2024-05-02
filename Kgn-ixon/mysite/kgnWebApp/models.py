from django.db import models


class KGN_Brand(models.Model):
    Brand_ID = models.CharField(max_length=200)
    Brand_Name = models.CharField(max_length=200)
    SN_Manufacture = models.CharField(max_length=200)
    Volume = models.CharField(max_length=200)

    
class Machine(models.Model):
    brand = models.ForeignKey(KGN_Brand, on_delete=models.CASCADE)
    machine_Name = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)
    Waste = models.CharField(max_length=200)
    Start_Avail = models.CharField(max_length=200)
    End_Avail = models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Sim_card= models.CharField(max_length=200)

    def TurnOn_Button(self):
        print("Turn on Machine")
        if self.Status== "damage":
            self.Status="green"
      

    def TurnOff_Button(self):
        print("Turn on Machine")


class Machine_Order(models.Model):
    # i need list of machine ids
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    Customer_ID = models.CharField(max_length=200)
    Customer_Name = models.CharField(max_length=200)
    Order_Name = models.CharField(max_length=200)
    Order_ID= models.CharField(max_length=200)
    Order_Date = models.CharField(max_length=200)  
    Order_Delivery_Date = models.CharField(max_length=200)
    Pieces = models.CharField(max_length=200)
    Assurance_Plan = models.CharField(max_length=200)


class Alarm(models.Model):
    Alarm_type = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Severity = models.CharField(max_length=100)
   # Adress inherited
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    Condition = models.CharField(max_length=255)
    Threshold = models.BooleanField(default=False)
    Threshold_type = models.CharField(max_length=100)
    On_Delay = models.CharField(max_length=100)
    Operator_Instructions = models.CharField(max_length=255)
    Access_Category = models.CharField(max_length=100)



class PLCConfiguration(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)



class PLCConfigIO(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.FloatField()
    unit = models.CharField(max_length=50)

# models.py


class Users(models.Model):
    Name = models.CharField(max_length=200)
    Access_Type = models.CharField(max_length=100)
    email = models.EmailField()
    Last_Access = models.DateTimeField()


class Messages(models.Model):
    Type = models.CharField(max_length=100)
    Machine_ID = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model
    Description = models.TextField()
    Date_and_Time = models.DateTimeField()
    Sender_ID = models.ForeignKey(Users, on_delete=models.CASCADE) 



class Router(models.Model):
    Simcard = models.CharField(max_length=100)
    MacAddress = models.CharField(max_length=100)
    IPAddress = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Firmware = models.CharField(max_length=100)
    Machine_ID = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model


class Machine_Log(models.Model):
    Person_ID = models.CharField(max_length=100)
    Person_Name = models.CharField(max_length=200)
    Change_event_date = models.DateTimeField()
    Description_of_change = models.TextField()
    Machine_ID = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model




"""

"""



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)