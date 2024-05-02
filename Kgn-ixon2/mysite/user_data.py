from kgnWebApp.models import User  # Import your User model
from datetime import datetime

# Sample data for 10 users
user_data = [
    {"name": "John Doe", "card_Number": 1234567890123456, "email": "john@example.com", "phone_Number": 1234567890, "category": "Category A", "last_Access": datetime.now()},
    {"name": "Jane Doe", "card_Number": 9876543210987654, "email": "jane@example.com", "phone_Number": 9876543210, "category": "Category B", "last_Access": datetime.now()},
    {"name": "Alice Smith", "card_Number": 1111222233334444, "email": "alice@example.com", "phone_Number": 11112222333, "category": "Category C", "last_Access": datetime.now()},
    {"name": "Bob Smith", "card_Number": 4444333322221111, "email": "bob@example.com", "phone_Number": 44443333222, "category": "Category A", "last_Access": datetime.now()},
    {"name": "Charlie Brown", "card_Number": 5555666677778888, "email": "charlie@example.com", "phone_Number": 55556666777, "category": "Category B", "last_Access": datetime.now()},
    {"name": "David Johnson", "card_Number": 8888777766665555, "email": "david@example.com", "phone_Number": 88887777666, "category": "Category C", "last_Access": datetime.now()},
    {"name": "Emma Davis", "card_Number": 2222333344445555, "email": "emma@example.com", "phone_Number": 22223333444, "category": "Category A", "last_Access": datetime.now()},
    {"name": "Frank Wilson", "card_Number": 6666555577778888, "email": "frank@example.com", "phone_Number": 66665555777, "category": "Category B", "last_Access": datetime.now()},
    {"name": "Grace Martinez", "card_Number": 9999888877776666, "email": "grace@example.com", "phone_Number": 99998888777, "category": "Category C", "last_Access": datetime.now()},
    {"name": "Henry Taylor", "card_Number": 3333222211110000, "email": "henry@example.com", "phone_Number": 33332222111, "category": "Category A", "last_Access": datetime.now()},
]

# Create User instances from the sample data
for data in user_data:
    User.objects.create(**data)




from kgnWebApp.models import Message, Machine, User, Alarm
from datetime import datetime

# Retrieve instances for Machine, User, and Alarm (assuming they already exist)
machine_instances = Machine.objects.all()[:10]
user_instances = User.objects.all()[:10]
alarm_instances = Alarm.objects.all()[:10]

# Data for 10 Message entries
message_entries = []
for i in range(10):
    message_data = {
        "machine": machine_instances[i],
        "user": user_instances[i],
        "alarm": alarm_instances[i],
        "type": f"Type {i+1}",
        "description": f"Description {i+1}",
        "date_Time": datetime.now(),
        "category": i+1
    }
    message_entries.append(message_data)

# Create and save 10 Message instances
for entry in message_entries:
    message_entry = Message.objects.create(**entry)

