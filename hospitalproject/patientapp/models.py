from django.db import models
from datetime import date



# Create your models here.
class PatientMaster(models.Model):
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    patientid = models.CharField(max_length=15)
    patientname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender_choices)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile1 = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=12)
    def __str__(self):
        return self.patientname
class DoctorMaster(models.Model):
    doctorname = models.CharField(max_length=50)
    department = models.CharField(max_length=40)
    def __str__(self):
        return self.doctorname
class AppointmentMaster(models.Model):
    patient = models.ForeignKey(PatientMaster, on_delete=models.CASCADE, null=True, default=None)
    patientname = models.CharField(max_length=50)
    mobile1 = models.CharField(max_length=20)
    doctor = models.ForeignKey(DoctorMaster,on_delete=models.CASCADE, null=True, default=None)
    doctorname = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=10)
class TreatmentMaster(models.Model):
    treatmentname = models.CharField(max_length=35)
    description = models.CharField(max_length=70)
    def __str__(self):
        return self.treatmentname
class PresCounter(models.Model):
    presno = models.PositiveIntegerField(default=1)
class VitalMaster(models.Model):
    patient = models.ForeignKey(PatientMaster, on_delete=models.CASCADE, null=True, default=None)
    doctor = models.ForeignKey(DoctorMaster, on_delete=models.CASCADE, null=True, default=None)
    prescriptionno = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    patientid = models.CharField(max_length=15)
    patientname = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    doctorname = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    dbp = models.IntegerField(null=True, blank=True)
    resrate = models.IntegerField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    spo2 = models.IntegerField(null=True, blank=True)
    sbp = models.IntegerField(null=True, blank=True)
    pulserate = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)
    bmi = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)
    status = models.CharField(max_length=255, default='Not Saved')

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.status = "Saved"
        super(VitalMaster, self).save(*args, **kwargs)

    def __str__(self):
        return self. prescriptionno
class ConsultationModel(models.Model):
    vitals = models.ForeignKey(VitalMaster, on_delete=models.CASCADE, null=True, default=None)
    prescriptionno = models.CharField(max_length=20)
    complaints =models.TextField()
    presentmedhis = models.TextField()
    pastmedhis = models.TextField()
    pastsurghis = models.TextField()
    allergies = models.TextField()
    investresult = models.TextField()
    instruction = models.TextField()

    def __str__(self):
        return self.prescriptionno
class ConsultationTreatment(models.Model):
    treatmentname =  models.CharField(max_length=50)
    treatmentdate = models.DateField()
    treatmentduration = models.CharField(max_length=40)
    consultation_model = models.ForeignKey(ConsultationModel, on_delete=models.CASCADE, null=True, default=None, related_name='consultation_treatments')
class ConsultationMedicine(models.Model):
    medicine_taken = (
        ('ac', 'AC'),
        ('pc', 'PC'),
    )
    itemname =  models.CharField(max_length=50)
    route = models.CharField(max_length=30)
    freequency = models.CharField(max_length=30)
    medicine_method = models.CharField(max_length=10, choices=medicine_taken)
    medstartdate = models.DateField()
    medenddate = models.DateField()
    consultation_model = models.ForeignKey(ConsultationModel, on_delete=models.CASCADE, null=True, default=None,related_name='consultation_medicines')


