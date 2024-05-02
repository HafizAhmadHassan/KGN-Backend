from kgnWebApp.models import UserMachine, Machine, User
from datetime import datetime

# Retrieve instances for Machine and User (assuming they already exist)
machine_instances = Machine.objects.all()[:10]
user_instances = User.objects.all()[:10]

# Data for 10 UserMachine entries
user_machine_entries = []
for i in range(9):
    user_machine_data = {
        "machine": machine_instances[i],
        "user": user_instances[i],
        "event_Change": datetime.now(),
        "description": f"User-Machine Relation {i+1}"
    }
    user_machine_entries.append(user_machine_data)

# Create and save 10 UserMachine instances
for entry in user_machine_entries:
    user_machine_entry = UserMachine.objects.create(**entry)
