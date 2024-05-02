# Run this in the Django shell

"""

from kgnWebApp.models import Machine_Order, Machine

# Sample data for MachineOrder
machine_order_data = [
    {"machine": Machine.objects.get(pk=1), "Customer_ID": "C001", "Customer_Name": "Customer A", "Order_Name": "Order 1", "Order_ID": "O001", "Order_Date": "2024-02-19", "Order_Delivery_Date": "2024-03-01", "Pieces": "100", "Assurance_Plan": "Basic"},
    {"machine": Machine.objects.get(pk=2), "Customer_ID": "C002", "Customer_Name": "Customer B", "Order_Name": "Order 2", "Order_ID": "O002", "Order_Date": "2024-02-20", "Order_Delivery_Date": "2024-03-05", "Pieces": "200", "Assurance_Plan": "Extended"},
    {"machine": Machine.objects.get(pk=3), "Customer_ID": "C003", "Customer_Name": "Customer C", "Order_Name": "Order 3", "Order_ID": "O003", "Order_Date": "2024-02-21", "Order_Delivery_Date": "2024-03-10", "Pieces": "150", "Assurance_Plan": "Standard"},
    {"machine": Machine.objects.get(pk=4), "Customer_ID": "C004", "Customer_Name": "Customer D", "Order_Name": "Order 4", "Order_ID": "O004", "Order_Date": "2024-02-22", "Order_Delivery_Date": "2024-03-15", "Pieces": "120", "Assurance_Plan": "Basic"},
    {"machine": Machine.objects.get(pk=5), "Customer_ID": "C005", "Customer_Name": "Customer E", "Order_Name": "Order 5", "Order_ID": "O005", "Order_Date": "2024-02-23", "Order_Delivery_Date": "2024-03-20", "Pieces": "180", "Assurance_Plan": "Extended"},
    {"machine": Machine.objects.get(pk=6), "Customer_ID": "C006", "Customer_Name": "Customer F", "Order_Name": "Order 6", "Order_ID": "O006", "Order_Date": "2024-02-24", "Order_Delivery_Date": "2024-03-25", "Pieces": "130", "Assurance_Plan": "Standard"},
    {"machine": Machine.objects.get(pk=7), "Customer_ID": "C007", "Customer_Name": "Customer G", "Order_Name": "Order 7", "Order_ID": "O007", "Order_Date": "2024-02-25", "Order_Delivery_Date": "2024-03-30", "Pieces": "170", "Assurance_Plan": "Basic"},
    {"machine": Machine.objects.get(pk=8), "Customer_ID": "C008", "Customer_Name": "Customer H", "Order_Name": "Order 8", "Order_ID": "O008", "Order_Date": "2024-02-26", "Order_Delivery_Date": "2024-04-04", "Pieces": "140", "Assurance_Plan": "Extended"},
    {"machine": Machine.objects.get(pk=9), "Customer_ID": "C009", "Customer_Name": "Customer I", "Order_Name": "Order 9", "Order_ID": "O009", "Order_Date": "2024-02-27", "Order_Delivery_Date": "2024-04-09", "Pieces": "160", "Assurance_Plan": "Standard"},
    {"machine": Machine.objects.get(pk=10), "Customer_ID": "C010", "Customer_Name": "Customer J", "Order_Name": "Order 10", "Order_ID": "O010", "Order_Date": "2024-02-28", "Order_Delivery_Date": "2024-04-14", "Pieces": "190", "Assurance_Plan": "Basic"},
]

# Create and save MachineOrder instances
for data in machine_order_data:
    machine_order = Machine_Order(**data)
    machine_order.save()


"""