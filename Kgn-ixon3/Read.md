

## Python File Running Data Entry

> django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

- python3 manage.py shell
-
- exec(open("PLC_config_data.py").read())
- exec(open("PLCData_data_entry.py").read())
- exec(open("kgnbrand_data.py").read())
- exec(open("machine_data.py").read())
- exec(open("user_data.py").read())
- exec(open("alarm_data.py").read())
- exec(open("messages_data.py").read())
- exec(open("router_data.py").read())
- exec(open("execure_all_data.py").read())

## Current Work Description

> I am on tutorial 2 on python shell and using OpenAI I did data entry on existing tables

> check kgnbrand_data for latest work




## Remember we need to pass not objects But Query Sets in contexts to get infomation


>  In detail file Views detail function Check Alarm:   print("Attention : Look at the difference behind print does not contain Query Set and Object Inside")

> https://stackoverflow.com/questions/29587382/how-to-add-an-model-instance-to-a-django-queryset
> queryset = MyModel.objects.none()
> instance = MyModel.objects.first()
> queryset |= MyModel.objects.filter(pk=instance.pk)



BEGIN;
--
-- Create model KGN_Brand
--
CREATE TABLE "kgnWebApp_kgn_brand" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Brand_ID" varchar(200) NOT NULL, "Brand_Name" varchar(200) NOT NULL, "SN_Manufacture" varchar(200) NOT NULL, "Online" varchar(200) NOT NULL, "Volume" varchar(200) NOT NULL);
--
-- Create model PLCConfigIO
--
CREATE TABLE "kgnWebApp_plcconfigio" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "value" real NOT NULL, "unit" varchar(50) NOT NULL);
--
-- Create model PLCConfiguration
--
CREATE TABLE "kgnWebApp_plcconfiguration" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "state" varchar(50) NOT NULL);
--
-- Create model Question
--
CREATE TABLE "kgnWebApp_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Machine
--
CREATE TABLE "kgnWebApp_machine" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "machine_Name" varchar(200) NOT NULL, "Status" varchar(200) NOT NULL, "Waste" varchar(200) NOT NULL, "Start_Avail" varchar(200) NOT NULL, "End_Avail" varchar(200) NOT NULL, "Street" varchar(200) NOT NULL, "State" varchar(200) NOT NULL, "Country" varchar(200) NOT NULL, "Sim_card" varchar(200) NOT NULL, "brand_id" bigint NOT NULL REFERENCES "kgnWebApp_kgn_brand" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Alarm
--
CREATE TABLE "kgnWebApp_alarm" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Alarm_type" varchar(100) NOT NULL, "Name" varchar(100) NOT NULL, "Severity" varchar(100) NOT NULL, "Condition" varchar(255) NOT NULL, "Threshold" bool NOT NULL, "Threshold_type" varchar(100) NOT NULL, "On_Delay" varchar(100) NOT NULL, "Operator_Instructions" varchar(255) NOT NULL, "Access_Category" varchar(100) NOT NULL, "machine_id" bigint NOT NULL REFERENCES "kgnWebApp_machine" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Machine_Order
--
CREATE TABLE "kgnWebApp_machine_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Cutomer_ID" varchar(200) NOT NULL, "Cutomer_Name" varchar(200) NOT NULL, "Order_Name" varchar(200) NOT NULL, "Order_ID" varchar(200) NOT NULL, "Order_Date" varchar(200) NOT NULL, "Order_Delivery_Date" varchar(200) NOT NULL, "Pieces" varchar(200) NOT NULL, "Assurance_Plan" varchar(200) NOT NULL, "machine_id" bigint NOT NULL REFERENCES "kgnWebApp_machine" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Choice
--
CREATE TABLE "kgnWebApp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "kgnWebApp_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "kgnWebApp_machine_brand_id_93dce3cf" ON "kgnWebApp_machine" ("brand_id");
CREATE INDEX "kgnWebApp_alarm_machine_id_aa8f973f" ON "kgnWebApp_alarm" ("machine_id");
CREATE INDEX "kgnWebApp_machine_order_machine_id_500ccaae" ON "kgnWebApp_machine_order" ("machine_id");
CREATE INDEX "kgnWebApp_choice_question_id_d6662941" ON "kgnWebApp_choice" ("question_id");
COMMIT;



# Error Pip3 install mysqlclient MYSQL Data insertion

Pip3 install mysqlclient


https://stackoverflow.com/questions/76585758/mysqlclient-cannot-install-via-pip-cannot-find-pkg-config-name-in-ubuntu


Brew Install 

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential


https://stackoverflow.com/questions/59229903/inserting-csv-into-mysql-database-with-python-library-mysql-connector


Pip3 install mysqlclient


https://stackoverflow.com/questions/76585758/mysqlclient-cannot-install-via-pip-cannot-find-pkg-config-name-in-ubuntu


Brew Install 

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential



To Solve check Experiment There is dataType Tuple Issue
https://www.w3schools.com/python/python_mysql_insert.asp


# Issues 

## Excel File Error Resolve
https://stackoverflow.com/questions/35743905/pd-read-excel-throws-permissionerror-if-file-is-open-in-excel


try:
    file = pd.ExcelFile("myfile.xlsm")
except PermissionError :
    pass
    file = pd.ExcelFile("myfile.xlsm")


# python Sql
cursor.fetchall()


# XLSM multiple sheets read

from openpyxl import load_workbook
wb2 = load_workbook('Kgn-ixon3/mysite/book3.xlsm')
sheets = wb2.sheetnames
ws = wb2[sheets[1]]


# Getting admin User information Admin Panel Django Down to Top Logs

https://docs.djangoproject.com/en/5.0/topics/auth/default/

https://stackoverflow.com/questions/2938879/displaying-list-of-registered-user-in-django-admin?rq=3


https://stackoverflow.com/questions/6005628/viewing-auth-user-model-in-django?rq=3


https://stackoverflow.com/questions/62009002/get-models-modeladmin-list-display-fields


-  admin_users = User.objects.filter()
- print(user.email)
- for user in admin_users:
- print(user)
- for user in admin_users:
- print(user.username)
- for user in admin_users:
- print(user.username)
- for user in admin_users:
- admin_users = User.objects.filter(is_staff=True)
 q.email
 q.admin
 q
  q= User.objects.all()
   from django.contrib.auth.models import User
   admin_users = User.objects.filter(is_staff=True)

   for user in admin_users:    print(user.username)

   admin_users = User.objects.all()
   admin_users
   admin_users = User.obr.get_queryset()
   admin_users = User.obr.get_queryset().all()
   admin_users = User.obr.get_queryset.all()
   exadmin_users = User.objects.filter()

# Add Field in Admin Panel
## Django admin Model field

https://stackoverflow.com/questions/31366720/django-admin-model-field-set-to-current-user?rq=3