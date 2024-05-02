# Run this in the Django shell


from kgnWebApp.models import Machine, KgnBrand, PLCData, PLCIO
from datetime import date

# Retrieve instances for KgnBrand, PLCData, and PLCIO
kgn_brand_instances = KgnBrand.objects.all()[:10]
plc_data_instances = PLCData.objects.all()[:10]
plc_io_instances = PLCIO.objects.all()[:10]

# Data for 10 Machine entries
machine_entries = []
for i in range(10):
    machine_data = {
        "kgnbrand": kgn_brand_instances[i],
        "plcdata": plc_data_instances[i],
        "plcio": plc_io_instances[i],
        "machine_Name": f"Machine {i+1}",
        "status": 1,  # Assuming status is an integer field
        "waste": f"Waste data {i+1}",
        "start_Available": date.today(),
        "end_Available": date.today(),
        "province": f"Province data {i+1}",
        "street": f"Street data {i+1}",
        "postal_Code": f"1234{i+1}",
        "Country": f"Country data {i+1}"
    }
    machine_entries.append(machine_data)

# Create and save 10 Machine instances
for entry in machine_entries:
    machine_entry = Machine(**entry)
    machine_entry.save()


"""
# Sample data for Machine
machine_data = [
    {"brand": KGN_Brand.objects.get(pk=1), "machine_Name": "Machine 1", "Status": "Active", "Waste": "None", "Start_Avail": "8:00 AM", "End_Avail": "5:00 PM", "Street": "123 Main St", "State": "CA", "Country": "USA", "Sim_card": "1234567890"},
    {"brand": KGN_Brand.objects.get(pk=2), "machine_Name": "Machine 2", "Status": "Inactive", "Waste": "Plastic", "Start_Avail": "9:00 AM", "End_Avail": "6:00 PM", "Street": "456 Elm St", "State": "NY", "Country": "USA", "Sim_card": "9876543210"},
    {"brand": KGN_Brand.objects.get(pk=3), "machine_Name": "Machine 3", "Status": "Active", "Waste": "Paper", "Start_Avail": "7:00 AM", "End_Avail": "4:00 PM", "Street": "789 Oak St", "State": "TX", "Country": "USA", "Sim_card": "4567890123"},
    {"brand": KGN_Brand.objects.get(pk=4), "machine_Name": "Machine 4", "Status": "Active", "Waste": "Glass", "Start_Avail": "8:30 AM", "End_Avail": "5:30 PM", "Street": "101 Pine St", "State": "FL", "Country": "USA", "Sim_card": "7890123456"},
    {"brand": KGN_Brand.objects.get(pk=5), "machine_Name": "Machine 5", "Status": "Inactive", "Waste": "Metal", "Start_Avail": "10:00 AM", "End_Avail": "7:00 PM", "Street": "202 Maple St", "State": "WA", "Country": "USA", "Sim_card": "8901234567"},
    {"brand": KGN_Brand.objects.get(pk=6), "machine_Name": "Machine 6", "Status": "Active", "Waste": "Organic", "Start_Avail": "6:00 AM", "End_Avail": "3:00 PM", "Street": "303 Walnut St", "State": "IL", "Country": "USA", "Sim_card": "9012345678"},
    {"brand": KGN_Brand.objects.get(pk=7), "machine_Name": "Machine 7", "Status": "Active", "Waste": "Plastic", "Start_Avail": "8:00 AM", "End_Avail": "5:00 PM", "Street": "404 Cedar St", "State": "GA", "Country": "USA", "Sim_card": "0123456789"},
    {"brand": KGN_Brand.objects.get(pk=8), "machine_Name": "Machine 8", "Status": "Inactive", "Waste": "Paper", "Start_Avail": "9:00 AM", "End_Avail": "6:00 PM", "Street": "505 Birch St", "State": "NC", "Country": "USA", "Sim_card": "2345678901"},
    {"brand": KGN_Brand.objects.get(pk=9), "machine_Name": "Machine 9", "Status": "Active", "Waste": "Glass", "Start_Avail": "7:00 AM", "End_Avail": "4:00 PM", "Street": "606 Elm St", "State": "OH", "Country": "USA", "Sim_card": "3456789012"},
    {"brand": KGN_Brand.objects.get(pk=10), "machine_Name": "Machine 10", "Status": "Active", "Waste": "Metal", "Start_Avail": "8:30 AM", "End_Avail": "5:30 PM", "Street": "707 Oak St", "State": "CA", "Country": "USA", "Sim_card": "4567890123"},
]

# Create and save Machine instances
for data in machine_data:
    machine = Machine(**data)
    machine.save()

"""