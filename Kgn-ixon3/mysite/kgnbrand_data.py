# Run this in the Django shell

from kgnWebApp.models import KgnBrand
"""
from kgnWebApp.models import KGN_Brand

# Sample data for KgnBrand
kgn_brand_data = [
    {"Brand_ID": "001", "Brand_Name": "Brand A", "SN_Manufacture": "SN001", "Volume": "10ml"},
    {"Brand_ID": "002", "Brand_Name": "Brand B", "SN_Manufacture": "SN002", "Volume": "20ml"},
    {"Brand_ID": "003", "Brand_Name": "Brand C", "SN_Manufacture": "SN003", "Volume": "30ml"},
    {"Brand_ID": "004", "Brand_Name": "Brand D", "SN_Manufacture": "SN004", "Volume": "40ml"},
    {"Brand_ID": "005", "Brand_Name": "Brand E", "SN_Manufacture": "SN005", "Volume": "50ml"},
    {"Brand_ID": "006", "Brand_Name": "Brand F", "SN_Manufacture": "SN006", "Volume": "60ml"},
    {"Brand_ID": "007", "Brand_Name": "Brand G", "SN_Manufacture": "SN007", "Volume": "70ml"},
    {"Brand_ID": "008", "Brand_Name": "Brand H", "SN_Manufacture": "SN008", "Volume": "80ml"},
    {"Brand_ID": "009", "Brand_Name": "Brand I", "SN_Manufacture": "SN009", "Volume": "90ml"},
    {"Brand_ID": "010", "Brand_Name": "Brand J", "SN_Manufacture": "SN010", "Volume": "100ml"},
]

# Create and save KgnBrand instances
for data in kgn_brand_data:
    kgn_brand = KGN_Brand(**data)
    kgn_brand.save()

"""

# Data for 10 entries
data_entries = [
    {"name": "Brand 1", "volume_Value": 10, "volume_Unit": "Liters"},
    {"name": "Brand 2", "volume_Value": 20, "volume_Unit": "Gallons"},
    {"name": "Brand 3", "volume_Value": 15, "volume_Unit": "Liters"},
    {"name": "Brand 4", "volume_Value": 8, "volume_Unit": "Gallons"},
    {"name": "Brand 5", "volume_Value": 12, "volume_Unit": "Liters"},
    {"name": "Brand 6", "volume_Value": 18, "volume_Unit": "Gallons"},
    {"name": "Brand 7", "volume_Value": 14, "volume_Unit": "Liters"},
    {"name": "Brand 8", "volume_Value": 9, "volume_Unit": "Gallons"},
    {"name": "Brand 9", "volume_Value": 16, "volume_Unit": "Liters"},
    {"name": "Brand 10", "volume_Value": 2, "volume_Unit": "Gallons"},
]

# Save each entry to the database
for entry in data_entries:
    kgn_brand_entry = KgnBrand(**entry)
    kgn_brand_entry.save()
