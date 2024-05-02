# Run this in the Django shell
"""
from kgnWebApp.models import Alarm, Machine

# Sample data for Alarm
alarm_data = [
    {"Alarm_type": "Temperature", "Name": "High Temperature", "Severity": "High", "machine": Machine.objects.get(pk=1), "Condition": "Temperature > 100°C", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "30 seconds", "Operator_Instructions": "Check cooling system", "Access_Category": "Maintenance"},
    {"Alarm_type": "Pressure", "Name": "Low Pressure", "Severity": "Medium", "machine": Machine.objects.get(pk=2), "Condition": "Pressure < 20 psi", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "1 minute", "Operator_Instructions": "Check pressure valve", "Access_Category": "Maintenance"},
    {"Alarm_type": "Voltage", "Name": "High Voltage", "Severity": "High", "machine": Machine.objects.get(pk=3), "Condition": "Voltage > 220V", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "20 seconds", "Operator_Instructions": "Check electrical circuit", "Access_Category": "Maintenance"},
    {"Alarm_type": "Flow Rate", "Name": "Low Flow Rate", "Severity": "Low", "machine": Machine.objects.get(pk=4), "Condition": "Flow Rate < 10 l/min", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "45 seconds", "Operator_Instructions": "Check flow sensor", "Access_Category": "Maintenance"},
    {"Alarm_type": "Humidity", "Name": "High Humidity", "Severity": "Medium", "machine": Machine.objects.get(pk=5), "Condition": "Humidity > 80%", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "1 minute", "Operator_Instructions": "Check dehumidifier", "Access_Category": "Maintenance"},
    {"Alarm_type": "Vibration", "Name": "High Vibration", "Severity": "Medium", "machine": Machine.objects.get(pk=6), "Condition": "Vibration > 0.1 g", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "1 minute", "Operator_Instructions": "Check vibration damper", "Access_Category": "Maintenance"},
    {"Alarm_type": "Speed", "Name": "Low Speed", "Severity": "Low", "machine": Machine.objects.get(pk=7), "Condition": "Speed < 1000 rpm", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "30 seconds", "Operator_Instructions": "Check motor", "Access_Category": "Maintenance"},
    {"Alarm_type": "Level", "Name": "Low Level", "Severity": "Low", "machine": Machine.objects.get(pk=8), "Condition": "Level < 20%", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "1 minute", "Operator_Instructions": "Check tank level", "Access_Category": "Maintenance"},
    {"Alarm_type": "Frequency", "Name": "High Frequency", "Severity": "Medium", "machine": Machine.objects.get(pk=9), "Condition": "Frequency > 60 Hz", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "45 seconds", "Operator_Instructions": "Check electrical system", "Access_Category": "Maintenance"},
    {"Alarm_type": "Power", "Name": "Low Power", "Severity": "High", "machine": Machine.objects.get(pk=10), "Condition": "Power < 80%", "Threshold": True, "Threshold_type": "Absolute", "On_Delay": "30 seconds", "Operator_Instructions": "Check power supply", "Access_Category": "Maintenance"},
]

# Create and save Alarm instances
for data in alarm_data:
    alarm = Alarm(**data)
    alarm.save()


"""

from kgnWebApp.models import Alarm  # Import your Alarm model

# Sample data for 10 alarms
alarm_data = [
    {"name": "Alarm 1", "severity": "High", "address": "Address 1", "threshold": "Threshold 1", "threshold_Type": True, "on_Delay": 5.0, "operator_Instruction": "Check instruction 1", "access_category": "Category A"},
    {"name": "Alarm 2", "severity": "Medium", "address": "Address 2", "threshold": "Threshold 2", "threshold_Type": False, "on_Delay": 10.0, "operator_Instruction": "Check instruction 2", "access_category": "Category B"},
    {"name": "Alarm 3", "severity": "Low", "address": "Address 3", "threshold": "Threshold 3", "threshold_Type": True, "on_Delay": 15.0, "operator_Instruction": "Check instruction 3", "access_category": "Category C"},
    {"name": "Alarm 4", "severity": "High", "address": "Address 4", "threshold": "Threshold 4", "threshold_Type": False, "on_Delay": 20.0, "operator_Instruction": "Check instruction 4", "access_category": "Category A"},
    {"name": "Alarm 5", "severity": "Medium", "address": "Address 5", "threshold": "Threshold 5", "threshold_Type": True, "on_Delay": 25.0, "operator_Instruction": "Check instruction 5", "access_category": "Category B"},
    {"name": "Alarm 6", "severity": "Low", "address": "Address 6", "threshold": "Threshold 6", "threshold_Type": False, "on_Delay": 30.0, "operator_Instruction": "Check instruction 6", "access_category": "Category C"},
    {"name": "Alarm 7", "severity": "High", "address": "Address 7", "threshold": "Threshold 7", "threshold_Type": True, "on_Delay": 35.0, "operator_Instruction": "Check instruction 7", "access_category": "Category A"},
    {"name": "Alarm 8", "severity": "Medium", "address": "Address 8", "threshold": "Threshold 8", "threshold_Type": False, "on_Delay": 40.0, "operator_Instruction": "Check instruction 8", "access_category": "Category B"},
    {"name": "Alarm 9", "severity": "Low", "address": "Address 9", "threshold": "Threshold 9", "threshold_Type": True, "on_Delay": 45.0, "operator_Instruction": "Check instruction 9", "access_category": "Category C"},
    {"name": "Alarm 10", "severity": "High", "address": "Address 10", "threshold": "Threshold 10", "threshold_Type": False, "on_Delay": 50.0, "operator_Instruction": "Check instruction 10", "access_category": "Category A"},
]

# Create Alarm instances from the sample data
for data in alarm_data:
    Alarm.objects.create(**data)
