from kgnWebApp.models import EventLog, Machine, User
from datetime import datetime

# Retrieve instances for Machine and User (assuming they already exist)
machine_instances = Machine.objects.all()[:10]
user_instances = User.objects.all()[:10]

# Data for 10 EventLog entries
event_log_entries = []
for i in range(10):
    event_log_data = {
        "machine": machine_instances[i],
        "user": user_instances[i],
        "event_Change": datetime.now(),
        "description": f"Event Description {i+1}"
    }
    event_log_entries.append(event_log_data)

# Create and save 10 EventLog instances
for entry in event_log_entries:
    event_log_entry = EventLog.objects.create(**entry)
