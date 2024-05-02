from django.http import HttpResponse
from django.template import loader

from .models import Machine, KGN_Brand,Alarm, PLCConfiguration,Machine_Order

#def show_all_machine():
    
#   machine = Machine.objects.values_list("machine_Name",flat=True)
#   output="\n".join([m_text for m_text in machine])
#   print(output)
    

#    machine = Machine.objects.values_list("machine_Name")
#    output=" - ".join([str(m_text[0]) for m_text in machine])
#    print(output)
    

   
"""
def index(request):
    machine = Machine.objects.values_list("machine_Name",flat=True)

    template = loader.get_template("kgnWebApp/index.html")
    context ={
        "machine" : machine,
    }
    return HttpResponse(template.render(context,request))
"""

def index(request):
    machine = Machine.objects.all()

    template = loader.get_template("kgnWebApp/index.html")
    context ={
        "machines" : machine,
    }
    return HttpResponse(template.render(context,request))

def details(request,machine_id):
    response = "You're looking at the machine %s."
    return HttpResponse(response % machine_id)


def detail(request,machine_id):
  
    machine=Machine.objects.get(pk=machine_id)
    #every alarm has machine id 
    # there is Foreign key machine in Alarm
    print(machine.alarm_set.all(),machine.alarm_set.count())
    alarm = Alarm.objects.get(machine=machine_id)
    print("Attention : Look at the difference behind print does not contain Query Set and Object Insidre")
    print(alarm)
    print(machine.machine_order_set.count())
    machine_orders_counts=machine.machine_order_set.count()

    machine_orders=machine.machine_order_set.all()

    alarm = Alarm.objects.get(machine=machine_id)
    print(alarm)
    alarm_queryset = Alarm.objects.none()
    alarm_queryset |= Alarm.objects.filter(pk=alarm.pk)
    print(alarm_queryset)
    print(machine_orders[0].Pieces)

    context ={
        "machines" : machine,
        "machine_orders": machine_orders,
        "machine_orders_count" : machine_orders_counts,
    }
    template = loader.get_template("kgnWebApp/detail.html")
    
    return HttpResponse(template.render(context,request))
