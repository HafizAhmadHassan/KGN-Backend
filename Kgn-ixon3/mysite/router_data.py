from kgnWebApp.models import Router, Machine
from decimal import Decimal

# Retrieve instances for Machine (assuming they already exist)
machine_instances = Machine.objects.all()[:10]

# Data for 10 Router entries
router_entries = []
for i in range(9):
    router_data = {
        "machine": machine_instances[i],
        "sim_Card": Decimal(i + 1),  # Example sim card data
        "mac_Address": f"MAC_Address_{i+1}",
        "ip_Address": f"192.168.1.{i+1}",
        "type": f"Type_{i+1}",
        "version": i + 1 if i % 2 == 0 else None  # Example version data, every other entry is None
    }
    router_entries.append(router_data)

# Create and save 10 Router instances
for entry in router_entries:
    router_entry = Router.objects.create(**entry)
