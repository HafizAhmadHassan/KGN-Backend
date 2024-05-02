

## Python File Running Data Entry

> django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

- python3 manage.py shell

- exec(open("data_entry.py").read())
- exec(open("PLCData_data_entry.py").read())
- exec(open("kgnbrand_data.py").read())
- exec(open("machine_data.py").read())
- exec(open("user_data.py").read())
- exec(open("alarm_data.py").read())
- exec(open("messages_data.py").read())
- exec(open("router_data.py").read())
- exec(open("event_data.py").read())

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