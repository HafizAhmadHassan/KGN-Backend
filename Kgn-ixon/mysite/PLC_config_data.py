# Run this in the Django shell

#from kgnWebApp.models import PLCConfiguration, PLCConfigIO

# Sample data for PLCConfiguration

"""

plc_configuration_data = [
    {"name": "PLC1", "state": "Running"},
    {"name": "PLC2", "state": "Stopped"},
    {"name": "PLC3", "state": "Paused"},
    {"name": "PLC4", "state": "Running"},
    {"name": "PLC5", "state": "Stopped"},
    {"name": "PLC6", "state": "Paused"},
    {"name": "PLC7", "state": "Running"},
    {"name": "PLC8", "state": "Stopped"},
    {"name": "PLC9", "state": "Paused"},
    {"name": "PLC10", "state": "Running"},
]

# Sample data for PLCConfigIO
plc_config_io_data = [
    {"name": "Input1", "value": 1.0, "unit": "V"},
    {"name": "Input2", "value": 2.0, "unit": "A"},
    {"name": "Output1", "value": 3.0, "unit": "V"},
    {"name": "Output2", "value": 4.0, "unit": "A"},
    {"name": "Input3", "value": 5.0, "unit": "V"},
    {"name": "Input4", "value": 6.0, "unit": "A"},
    {"name": "Output3", "value": 7.0, "unit": "V"},
    {"name": "Output4", "value": 8.0, "unit": "A"},
    {"name": "Input5", "value": 9.0, "unit": "V"},
    {"name": "Input6", "value": 10.0, "unit": "A"},
]

# Create and save PLCConfiguration instances
for data in plc_configuration_data:
    plc_config = PLCConfiguration(**data)
    plc_config.save()

# Create and save PLCConfigIO instances
for data in plc_config_io_data:
    plc_io = PLCConfigIO(**data)
    plc_io.save()

"""
