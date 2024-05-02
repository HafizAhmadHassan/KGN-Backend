from kgnWebApp.models import MessageUser, Message, User

# Retrieve instances for Message and User (assuming they already exist)
message_instances = Message.objects.all()[:10]
user_instances = User.objects.all()[:10]

# Data for 10 MessageUser entries
message_user_entries = []
for i in range(9):
    message_user_data = {
        "message": message_instances[i],
        "user": user_instances[i]
    }
    message_user_entries.append(message_user_data)

# Create and save 10 MessageUser instances
for entry in message_user_entries:
    message_user_entry = MessageUser.objects.create(**entry)
