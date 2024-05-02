from kgnWebApp.models import Message, Machine, Alarm
from datetime import datetime

# Retrieve instances for Machine and Alarm (assuming they already exist)
machine_instances = Machine.objects.all()[:10]
alarm_instances = Alarm.objects.all()[:10]

# Data for 10 Message entries
message_entries = []
for i in range(9):
    message_data = {
        "machine": machine_instances[i],
        "alarm": alarm_instances[i],
        "type": f"Type {i+1}",
        "description": f"Message Description {i+1}",
        "date_Time": datetime.now(),
        "category": i+1
    }
    message_entries.append(message_data)

# Create and save 10 Message instances
for entry in message_entries:
    message_entry = Message.objects.create(**entry)
