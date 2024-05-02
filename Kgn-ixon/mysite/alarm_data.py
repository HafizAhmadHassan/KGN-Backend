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
