from django.db import models
from django.utils import timezone
from django.db.models import Count

names_Machines=[
    'Abc',
    'cdf',
    'fgh'
]
class KgnBrand(models.Model):
    name = models.CharField(max_length=40)
    volume_Value = models.DecimalField(max_digits=10, decimal_places=2)
    volume_Unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class PLCData(models.Model):
    
    plant1_Emergenza_NOK = models.IntegerField(default=-1)
    plant1_Errore_di_comunicazione_con_HMI= models.IntegerField(default=-1)
    plant1_Analogica_Peso_in_errore= models.IntegerField(default=-1)
    plant1_Analogica_Pressione_in_errore= models.IntegerField(default=-1)
    plant1_TimeOut_Comunicazione= models.IntegerField(default=-1)
    plant1_Superata_Soglia_Max_Peso= models.IntegerField(default=-1)
    plant1_Mancanza_Rete_Elettrica= models.IntegerField(default=-1)
    plant1_Porte_Aperte= models.IntegerField(default=-1)
    plant1_Errore_di_fase= models.IntegerField(default=-1)
    plant1_Errore_Bilancia= models.IntegerField(default=-1)
    plant1_Errore_Bloccante= models.IntegerField(default=-1)
    plant1_Movimento_non_possibile= models.IntegerField(default=-1)
    plant1_Peso_Instabile= models.IntegerField(default=-1)
    plant1_Comando_Bimanuale_Attivo= models.IntegerField(default=-1)
    plant1_Container_quasi_Pieno= models.IntegerField(default=-1)
    plant1_Container_Pieno= models.IntegerField(default=-1)



   #plant2

    plant2_Segnale_GPS = models.IntegerField(default=-1)
    plant2_Segnale_Internet= models.IntegerField(default=-1)
    plant2_Sistema_di_pesatura_NOk= models.IntegerField(default=-1)
    plant2_Lampada_Foto_in_Errore= models.IntegerField(default=-1)
    plant2_Protezione_Termica_UPS = models.IntegerField(default=-1)
    plant2_Battaria_Tapone_Scarica= models.IntegerField(default=-1)
    plant2_Protezione_Termica_Resistenza= models.IntegerField(default=-1)
    plant2_Inferiore_a_Soglia_Min_Peso= models.IntegerField(default=-1)
    plant2_Kompact_Pronto= models.IntegerField(default=-1)
    plant2_Movimentazione_Manuale_in_Corso= models.IntegerField(default=-1)
    plant2_Fatal_Alarm= models.IntegerField(default=-1)
    plant2_Movimento_non_possibile = models.IntegerField(default=-1)
    plant2_Carico_Ingombrante = models.IntegerField(default=-1)
    plant2_Tentativi_Ripristino_Superati= models.IntegerField(default=-1)
    plant2_Extra1 = models.IntegerField(default=-1)
    plant2_Extra2 = models.IntegerField(default=-1)


    #roll_Up

    roll_Up_Protezione_termica= models.IntegerField(default=-1)
    roll_Up_TimeOut_Apertura= models.IntegerField(default=-1)
    roll_Up_TimeOut_Chiusura= models.IntegerField(default=-1)
    roll_Up_Sensore_Apertura_sempre_attivo= models.IntegerField(default=-1)
    roll_Up_Sensore_Chiusura_sempre_attivo= models.IntegerField(default=-1)
    roll_Up_Bordo_Sensibile_Interrotto= models.IntegerField(default=-1)
    roll_Up_Bordo_Sensibile_Guasto= models.IntegerField(default=-1)
    roll_Up_Extra1= models.IntegerField(default=-1)
    roll_Up_Extra2= models.IntegerField(default=-1)
    roll_Up_Extra3= models.IntegerField(default=-1)
    roll_Up_Fatal_error= models.IntegerField(default=-1)
    roll_Up_Movimento_non_possibile= models.IntegerField(default=-1)
    roll_Up_Superati_Tentativi_in_apertura= models.IntegerField(default=-1)
    roll_Up_Superati_Tentativi_in_chiusura= models.IntegerField(default=-1)
    roll_Up_Possibile_anomalia_al_funzionamento= models.IntegerField(default=-1)
    roll_Up_Eseguire_Manutenzione_Preventiva= models.IntegerField(default=-1)





    #rotation_Drum 
    
    rotation_Drum_Protezione_termica = models.IntegerField(default=-1)
    rotation_Drum_TimeOut_Rotazione_Avanti= models.IntegerField(default=-1)
    rotation_Drum_TimeOut_Rotazione_Indietro= models.IntegerField(default=-1)
    rotation_Drum_Sensore_Avanti_sempre_attivo= models.IntegerField(default=-1)
    rotation_Drum_Sensore_Indietro_sempre_attivo= models.IntegerField(default=-1)
    rotation_Drum_Extra1= models.IntegerField(default=-1)
    rotation_Drum_Movimento_Bloccato= models.IntegerField(default=-1)
    rotation_Drum_Extra2= models.IntegerField(default=-1)
    rotation_Drum_Extra3= models.IntegerField(default=-1)
    rotation_Drum_Extra4= models.IntegerField(default=-1)
    rotation_Drum_Fatal_error= models.IntegerField(default=-1)
    rotation_Drum_Movimento_non_possibile= models.IntegerField(default=-1)
    rotation_Drum_Extra5= models.IntegerField(default=-1)
    rotation_Drum_Superati_Tentativi_di_Ripristino= models.IntegerField(default=-1)
    rotation_Drum_Possibile_anomalia_al_funzionamento= models.IntegerField(default=-1)
    rotation_Drum_Eseguire_Manutenzione_Preventiva = models.IntegerField(default=-1)
        
    #pmp
    pmp_Protezione_termica= models.IntegerField(default=-1)
    pmp_Livello_detergente_Insufficente= models.IntegerField(default=-1)
    pmp_Extra1= models.IntegerField(default=-1)
    pmp_Extra2= models.IntegerField(default=-1)
    pmp_Extra3= models.IntegerField(default=-1)
    pmp_Extra4= models.IntegerField(default=-1)
    pmp_Extra5= models.IntegerField(default=-1)
    pmp_Extra6= models.IntegerField(default=-1)
    pmp_Extra7= models.IntegerField(default=-1)
    pmp_Extra8= models.IntegerField(default=-1)
    pmp_Fatal_error= models.IntegerField(default=-1)
    pmp_Utilizzo_non_possibile= models.IntegerField(default=-1)
    pmp_Extra9= models.IntegerField(default=-1)
    pmp_Extra10= models.IntegerField(default=-1)
    pmp_Possibile_anomalia_al_funzionamento= models.IntegerField(default=-1)
    pmp_Eseguire_Manutenzione_Preventiva = models.IntegerField(default=-1)

    #hydraulic 

    hydraulic_Protezione_termica= models.IntegerField(default=-1)
    hydraulic_Livello_detergente_Insufficente= models.IntegerField(default=-1)
    hydraulic_Extra1= models.IntegerField(default=-1)
    hydraulic_Extra2= models.IntegerField(default=-1)
    hydraulic_Extra3= models.IntegerField(default=-1)
    hydraulic_Extra4= models.IntegerField(default=-1)
    hydraulic_Extra5= models.IntegerField(default=-1)
    hydraulic_Extra6= models.IntegerField(default=-1)
    hydraulic_Extra7= models.IntegerField(default=-1)
    hydraulic_Extra8= models.IntegerField(default=-1)
    hydraulic_Fatal_error= models.IntegerField(default=-1)
    hydraulic_Utilizzo_non_possibile= models.IntegerField(default=-1)
    hydraulic_Extra9= models.IntegerField(default=-1)
    hydraulic_Extra10= models.IntegerField(default=-1)
    hydraulic_Possibile_anomalia_al_funzionamento= models.IntegerField(default=-1)
    hydraulic_Eseguire_Manutenzione_Preventiva = models.IntegerField(default=-1)

#yv_Fwbw

    yv_Fwbw_TimeOut_Pressa_Avanti= models.IntegerField(default=-1)
    yv_Fwbw_TimeOut_Pressa_Indietro= models.IntegerField(default=-1)
    yv_Fwbw_Sensore_Avanti_sempre_attivo= models.IntegerField(default=-1)
    yv_Fwbw_Sensore_Indietro_sempre_attivo= models.IntegerField(default=-1)
    yv_Fwbw_Extra1= models.IntegerField(default=-1)
    yv_Fwbw_Extra2= models.IntegerField(default=-1)
    yv_Fwbw_Extra3= models.IntegerField(default=-1)
    yv_Fwbw_Extra4= models.IntegerField(default=-1)
    yv_Fwbw_Extra5= models.IntegerField(default=-1)
    yv_Fwbw_Extra6= models.IntegerField(default=-1)
    yv_Fwbw_Fatal_Alarm= models.IntegerField(default=-1)
    yv_Fwbw_Movimento_non_possibile= models.IntegerField(default=-1)
    yv_Fwbw_Extra7= models.IntegerField(default=-1)
    yv_Fwbw_Superati_Tentativi_di_Ripristino= models.IntegerField(default=-1)
    yv_Fwbw_Possibile_anomalia_al_funzionamento= models.IntegerField(default=-1)
    yv_Fwbw_Eseguire_Manutenzione_Preventiva = models.IntegerField(default=-1)

#yv_Slow
     
    yv_Slow_Timeout_Sensore_Fw= models.IntegerField(default=-1)
    yv_Slow_Timeout_Sensore_Bw= models.IntegerField(default=-1)
    yv_Slow_Sensore_FW_Sempre_attivo= models.IntegerField(default=-1)
    yv_Slow_Sensore_BW_Sempre_attivo= models.IntegerField(default=-1)
    yv_Slow_Extra1= models.IntegerField(default=-1)
    yv_Slow_Extra2= models.IntegerField(default=-1)
    yv_Slow_Extra3= models.IntegerField(default=-1)
    yv_Slow_Extra4= models.IntegerField(default=-1)
    yv_Slow_Extra5= models.IntegerField(default=-1)
    yv_Slow_Extra6= models.IntegerField(default=-1)
    yv_Slow_Fatal_Alarm= models.IntegerField(default=-1)
    yv_Slow_Movimento_non_possibile= models.IntegerField(default=-1)
    yv_Slow_Extra7= models.IntegerField(default=-1)
    yv_Slow_Extra8= models.IntegerField(default=-1)
    yv_Slow_Possibile_anomalia_al_funzionamento= models.IntegerField(default=-1)
    yv_Slow_Eseguire_Manutenzione_Preventiva = models.IntegerField(default=-1)

    def __str__(self):
        return f"PLCData {self.id}"

class PLCIO(models.Model):



    #unit 

    unit_TimeOut_RollUp_Op = models.CharField(max_length=8,default="null")
    unit_TimeOut_RollUp_Cl = models.CharField(max_length=8,default="null")
    unit_TimeOut_Rot_Fw = models.CharField(max_length=8,default="null")
    unit_TimeOut_Rot_Bw = models.CharField(max_length=8,default="null")
    unit_TimeOut_Press_Fw = models.CharField(max_length=8,default="null")
    unit_TimeOut_Press_Bw = models.CharField(max_length=8,default="null")
    unit_TimeOutEndLoad = models.CharField(max_length=8,default="null")
    unit_Min_Weight = models.CharField(max_length=8,default="null")
    unit_Max_Weight = models.CharField(max_length=8,default="null")
    unit_Max_Weight_Standard_Deviation = models.CharField(max_length=8,default="null")
    unit_TImeCleaner = models.CharField(max_length=8,default="null") 
    unit_Pulse_Cleaner = models.CharField(max_length=8,default="null")
    unit_Time_Winter_Cycle = models.CharField(max_length=8,default="null")
    unit_Full_80_Type_1 = models.CharField(max_length=8,default="null")
    unit_Full_100_Type_1 = models.CharField(max_length=8,default="null")
    unit_TimeFull = models.CharField(max_length=8,default="null")
    unit_TimeSlowPress = models.CharField(max_length=8,default="null")
    unit_TimeBuzzerLoad_1 = models.CharField(max_length=8,default="null")
    unit_TimeBuzzerLoad_2 = models.CharField(max_length=8,default="null")
    unit_TImeRotBw_AfterF_PressFW = models.CharField(max_length=8,default="null")
    unit_Set_Couter_Rotation = models.CharField(max_length=8,default="null")
    unit_TimeOut_Communication = models.CharField(max_length=8,default="null")
    unit_Time_Manut_Prev_RollUp = models.CharField(max_length=8,default="null")
    unit_Time_Manut_Prev_Crate = models.CharField(max_length=8,default="null")
    unit_Time_Manut_Prev_Pmp_Igien = models.CharField(max_length=8,default="null")
    unit_Time_Manut_Prev_Hydr = models.CharField(max_length=8,default="null")
    unit_Time_Manut_Prev_ValveFwBw = models.CharField(max_length=8,default="null")
    unit_Time_Manut_Prev_ValveSlow = models.CharField(max_length=8,default="null")
    unit_TimeSwitchOff = models.CharField(max_length=8,default="null")
    unit_TimeSwitchOff_PC = models.CharField(max_length=8,default="null")
    unit_NumeroPressate = models.CharField(max_length=8,default="null")
    unit_TypeWaste = models.CharField(max_length=8,default="null")
    unit_FunzioneTurista = models.CharField(max_length=8,default="null")
    unit_CicloClean = models.CharField(max_length=8,default="null")
    unit_PressatePesoMinoreSoglia = models.CharField(max_length=8,default="null")
    unit_WhiteListOpen = models.CharField(max_length=8,default="null")
    unit_Try = models.CharField(max_length=8,default="null")
    unit_CamEnabled = models.CharField(max_length=8,default="null")
    unit_TempoConteggioEncoder = models.CharField(max_length=8,default="null")
    unit_TempoFiltroZeroEncoder = models.CharField(max_length=8,default="null")
    unit_Full_80_Type_2 = models.CharField(max_length=8,default="null")
    unit_Full_100_Type_2 = models.CharField(max_length=8,default="null")
    unit_Full_80_Type_3 = models.CharField(max_length=8,default="null")
    unit_Full_100_Type_3 = models.CharField(max_length=8,default="null")
    unit_Buzzer_OFF = models.CharField(max_length=8,default="null")
    unit_Ripristino = models.CharField(max_length=8,default="null")
    unit_Full_80_Type_4 = models.CharField(max_length=8,default="null")
    unit_Full_100_Type_4 = models.CharField(max_length=8,default="null")
    unit_Full_80_Type_5 = models.CharField(max_length=8,default="null")
    unit_Full_100_Type_5 = models.CharField(max_length=8,default="null")

    value_TimeOut_RollUp_Op = models.IntegerField(default=-1)
    value_TimeOut_RollUp_Cl = models.IntegerField(default=-1)
    value_TimeOut_Rot_Fw = models.IntegerField(default=-1)
    value_TimeOut_Rot_Bw = models.IntegerField(default=-1)
    value_TimeOut_Press_Fw = models.IntegerField(default=-1)
    value_TimeOut_Press_Bw = models.IntegerField(default=-1)
    value_TimeOutEndLoad = models.IntegerField(default=-1)
    value_Min_Weight = models.IntegerField(default=-1)
    value_Max_Weight = models.IntegerField(default=-1)
    value_Max_Weight_Standard_Deviation = models.IntegerField(default=-1)
    value_TImeCleaner = models.IntegerField(default=-1)
    value_Pulse_Cleaner = models.IntegerField(default=-1)
    value_Time_Winter_Cycle = models.IntegerField(default=-1)
    value_Full_80_Type_1 = models.IntegerField(default=-1)
    value_Full_100_Type_1 = models.IntegerField(default=-1)
    value_TimeFull = models.IntegerField(default=-1)
    value_TimeSlowPress = models.IntegerField(default=-1)
    value_TimeBuzzerLoad_1 = models.IntegerField(default=-1)
    value_TimeBuzzerLoad_2 = models.IntegerField(default=-1)
    value_TImeRotBw_AfterF_PressFW = models.IntegerField(default=-1)
    value_Set_Couter_Rotation = models.IntegerField(default=-1)
    value_TimeOut_Communication = models.IntegerField(default=-1)
    value_Time_Manut_Prev_RollUp = models.IntegerField(default=-1)
    value_Time_Manut_Prev_Crate = models.IntegerField(default=-1)
    value_Time_Manut_Prev_Pmp_Igien = models.IntegerField(default=-1)
    value_Time_Manut_Prev_Hydr = models.IntegerField(default=-1)
    value_Time_Manut_Prev_ValveFwBw = models.IntegerField(default=-1)
    value_Time_Manut_Prev_ValveSlow = models.IntegerField(default=-1)
    value_TimeSwitchOff = models.IntegerField(default=-1)
    value_TimeSwitchOff_PC = models.IntegerField(default=-1)
    value_NumeroPressate = models.IntegerField(default=-1)
    value_TypeWaste = models.IntegerField(default=-1)
    value_FunzioneTurista = models.IntegerField(default=-1)
    value_CicloClean = models.IntegerField(default=-1)
    value_PressatePesoMinoreSoglia = models.IntegerField(default=-1)
    value_WhiteListOpen = models.IntegerField(default=-1)
    value_Try = models.IntegerField(default=-1)
    value_CamEnabled = models.IntegerField(default=-1)
    value_TempoConteggioEncoder = models.IntegerField(default=-1)
    value_TempoFiltroZeroEncoder = models.IntegerField(default=-1)
    value_Full_80_Type_2 = models.IntegerField(default=-1)
    value_Full_100_Type_2 = models.IntegerField(default=-1)
    value_Full_80_Type_3 = models.IntegerField(default=-1)
    value_Full_100_Type_3 = models.IntegerField(default=-1)
    value_Buzzer_OFF = models.IntegerField(default=-1)
    value_Ripristino = models.IntegerField(default=-1)
    value_Full_80_Type_4 = models.IntegerField(default=-1)
    value_Full_100_Type_4 = models.IntegerField(default=-1)
    value_Full_80_Type_5 = models.IntegerField(default=-1)
    value_Full_100_Type_5 = models.IntegerField(default=-1)



    def __str__(self):
        return f"PLCIO : {self.id}"

class PLCStatus(models.Model):
    SERRANDA_CHIUSA = models.BooleanField(default=False)
    SERRANDA_APERTA = models.BooleanField(default=False)
    PRESSA_AVANTI = models.BooleanField(default=False)
    PRESSA_INDIETRO = models.BooleanField(default=False)
    CESTA_IN_CARICO = models.BooleanField(default=False)
    CESTA_IN_SCARICO = models.BooleanField(default=False)
    SERRANDA_SICUREZZA_CHIUSA = models.BooleanField(default=False)
    CESTA_SICUREZZA_IN_CARICO = models.BooleanField(default=False)
    CARICO_INGOMBRANTE = models.BooleanField(default=False)
    BORDO_SENSIBILE_INTERVENUTO = models.BooleanField(default=False)
    PORTE_LATERALI_APERTE = models.BooleanField(default=False)
    READY = models.BooleanField(default=False)
    ATTUALE_PRESSIONE = models.BooleanField(default=False)
    ATTUALE_PESO = models.BooleanField(default=False)
    SEQUENZA = models.BooleanField(default=False)
    VERSIONE_PLC = models.BooleanField(default=False)
    PULSANTE_EMERGENZA_INSERITO = models.BooleanField(default=False)
    PULSANTE_RESET_MACCHINA = models.BooleanField(default=False)
    PULSANTE_APRI_SERRANDA = models.BooleanField(default=False)
    PULSANTE_CHIUDI_SERRANDA = models.BooleanField(default=False)
    PULSANTE_AVANTI_PRESSA = models.BooleanField(default=False)
    PULSANTE_INDIETRO_PRESSA = models.BooleanField(default=False)
    PULSANTE_CESTA_IN_CARICO = models.BooleanField(default=False)
    PULSANTE_CESTA_IN_SCARICO = models.BooleanField(default=False)
    PULSANTE_POMPA_IGENIZZANTE = models.BooleanField(default=False)

    def __str__(self):
        return "PLC Status"


class AlarmSetting(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    text = models.TextField()
    role = models.CharField(max_length=200)
    sentmail = models.BooleanField(default=True)
    sentsms = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Machine(models.Model):
    kgnbrand = models.ForeignKey(KgnBrand, on_delete=models.CASCADE)
    plcdata = models.ForeignKey(PLCData, on_delete=models.CASCADE)
    plcio = models.ForeignKey(PLCIO, on_delete=models.CASCADE)
    plcstatus = models.ForeignKey(PLCStatus, on_delete=models.CASCADE,default='1')
    machine_Name = models.CharField(max_length=40)
    status = models.IntegerField()
    waste = models.CharField(max_length=20)
    linux_Version = models.CharField(max_length=10,default="v0")
    start_Available = models.DateField()
    end_Available = models.DateField()
    street = models.CharField(max_length=40)
    postal_Code = models.CharField(max_length=10)
    province = models.CharField(max_length=40)
    city = models.CharField(max_length=20,default="Vicenza")
    country = models.CharField(max_length=20,default="Italy")

    
    @classmethod
    def count_machines_by_status(cls):
        return cls.objects.values('status').annotate(Machines=Count('status'))
    
    
    class Meta:
        ordering = ['machine_Name']

    


    
class Router(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model
    sim_Card = models.DecimalField(max_digits=18, decimal_places=0)
    mac_Address = models.CharField(max_length=25)
    ip_Address = models.CharField(max_length=25)
    type = models.CharField(max_length=40)
    version = models.FloatField(null=True, blank=True, default=None)

class User(models.Model):
    name = models.CharField(max_length=30)
    card_Number = models.BigIntegerField(default=0)
    email = models.EmailField()
    last_Access = models.DateTimeField(auto_now_add=True, blank=True)
    phone_Number = models.BigIntegerField(default=0)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserMachine(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Machine is another model
    event_Change = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"UserMachine : {self.id}"
    

class Alarm(models.Model):
    name = models.CharField(max_length=40)
    position = models.CharField(default="General",max_length=10)
    sent = models.CharField(max_length=1,default='y')
    operator_Instruction = models.CharField(max_length=255) # Received from PLC

    def __str__(self):
        return self.name
    

class Message(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Assuming Machine is another model
    alarm = models.ForeignKey(Alarm, on_delete=models.CASCADE)  # Assuming Machine is another model
    type = models.CharField(max_length=40) # Waste Carta Comes from Machine
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=20) # Comes from user
    date_Time = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return f"Message : {self.id} "   





class MachineOrder(models.Model):
    name = models.CharField(max_length=40)
    order_Date = models.DateField()
    delivery_Date = models.DateField()
    brand_name = models.CharField(max_length=40)
    insurance = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class MessageUser(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)  # Assuming Machine is another model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Machine is another model

