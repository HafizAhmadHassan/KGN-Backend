# Run this in the Django shell

from kgnWebApp.models import KGN_Brand

# Sample data for KgnBrand

"""
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
