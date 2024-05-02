# Run this in the Django shell




from kgnWebApp.models import AlarmSetting  # Import the PLCData model from your app

import pandas as pd
import mysql.connector

def insert_data_from_excel(file_path):
    # Connect to MySQL database
    cnx = mysql.connector.connect(host='database-1.c3gsasq6u7jz.eu-south-1.rds.amazonaws.com',
                     user='admin',password="12345678",
                     database='KGN_DB',
                     port=3306)
    cursor = cnx.cursor()

    # Read data from Excel file
    df = pd.read_excel(file_path)

    # Iterate over each row and insert into the database
    data=[]
    for index, row in df.iterrows():
        add_data = "INSERT INTO kgnWebApp_alarmsetting (name, code, type, text, role, sentmail, sentsms) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data.append((row['Name'], row['Code'], row['Type'], row['Text'], row['Role'], row['Sentemail'], row['Sentsms']))
    print(data)
    print("done")

    cursor.executemany(add_data, data)
    
    # Commit changes and close connection
    cnx.commit()
    cursor.close()
    cnx.close()


# Specify the path to your Excel file
excel_file_path = "AlarmSetting2.xlsx"

# Call the function to insert data from Excel to the database
insert_data_from_excel(excel_file_path)
