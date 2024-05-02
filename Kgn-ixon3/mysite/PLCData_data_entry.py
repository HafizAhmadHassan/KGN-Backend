# Run this in the Django shell




from kgnWebApp.models import PLCData  # Import the PLCData model from your app

# Data for 10 entries
data_entries = [
    {"plant_1": "Plant 1 data 1", "plant_2": "Plant 2 data 1", "roll_Up": "Roll Up data 1", "rotation_Drum": "Rotation Drum data 1", "pmp": "PMP data 1", "hydraulic": "Hydraulic data 1", "yv_Fwbw": "YV FWBW data 1", "field": "Field data 1"},
    {"plant_1": "Plant 1 data 2", "plant_2": "Plant 2 data 2", "roll_Up": "Roll Up data 2", "rotation_Drum": "Rotation Drum data 2", "pmp": "PMP data 2", "hydraulic": "Hydraulic data 2", "yv_Fwbw": "YV FWBW data 2", "field": "Field data 2"},
    {"plant_1": "Plant 1 data 3", "plant_2": "Plant 2 data 3", "roll_Up": "Roll Up data 3", "rotation_Drum": "Rotation Drum data 3", "pmp": "PMP data 3", "hydraulic": "Hydraulic data 3", "yv_Fwbw": "YV FWBW data 3", "field": "Field data 3"},
    {"plant_1": "Plant 1 data 4", "plant_2": "Plant 2 data 4", "roll_Up": "Roll Up data 4", "rotation_Drum": "Rotation Drum data 4", "pmp": "PMP data 4", "hydraulic": "Hydraulic data 4", "yv_Fwbw": "YV FWBW data 4", "field": "Field data 4"},
    {"plant_1": "Plant 1 data 5", "plant_2": "Plant 2 data 5", "roll_Up": "Roll Up data 5", "rotation_Drum": "Rotation Drum data 5", "pmp": "PMP data 5", "hydraulic": "Hydraulic data 5", "yv_Fwbw": "YV FWBW data 5", "field": "Field data 5"},
    {"plant_1": "Plant 1 data 6", "plant_2": "Plant 2 data 6", "roll_Up": "Roll Up data 6", "rotation_Drum": "Rotation Drum data 6", "pmp": "PMP data 6", "hydraulic": "Hydraulic data 6", "yv_Fwbw": "YV FWBW data 6", "field": "Field data 6"},
    {"plant_1": "Plant 1 data 7", "plant_2": "Plant 2 data 7", "roll_Up": "Roll Up data 7", "rotation_Drum": "Rotation Drum data 7", "pmp": "PMP data 7", "hydraulic": "Hydraulic data 7", "yv_Fwbw": "YV FWBW data 7", "field": "Field data 7"},
    {"plant_1": "Plant 1 data 8", "plant_2": "Plant 2 data 8", "roll_Up": "Roll Up data 8", "rotation_Drum": "Rotation Drum data 8", "pmp": "PMP data 8", "hydraulic": "Hydraulic data 8", "yv_Fwbw": "YV FWBW data 8", "field": "Field data 8"},
    {"plant_1": "Plant 1 data 9", "plant_2": "Plant 2 data 9", "roll_Up": "Roll Up data 9", "rotation_Drum": "Rotation Drum data 9", "pmp": "PMP data 9", "hydraulic": "Hydraulic data 9", "yv_Fwbw": "YV FWBW data 9", "field": "Field data 9"},
    {"plant_1": "Plant 1 data 10", "plant_2": "Plant 2 data 10", "roll_Up": "Roll Up data 10", "rotation_Drum": "Rotation Drum data 10", "pmp": "PMP data 10", "hydraulic": "Hydraulic data 10", "yv_Fwbw": "YV FWBW data 10", "field": "Field data 10"},
]

# Save each entry to the database
for entry in data_entries:
    plc_data_entry = PLCData(**entry)
    plc_data_entry.save()

