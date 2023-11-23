from . import views
from django.contrib import admin
from django.urls import path, include
app_name = 'patientapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('login/',views.login,name='login'),
    path('home/', views.home, name='home'),
    path('AddPatient/',views.addpatient,name='addpatient'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('delete_patient/<int:patientid>/', views.delete_patient, name='delete_patient'),
    path('AddDoctor/', views.adddoctor, name='adddoctor'),
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('delete_doctor/<int:doctorid>/', views.delete_doctor, name='delete_doctor'),
    path('edit_doctor/<int:doctorid>/', views.edit_doctor, name='edit_doctor'),
    path('update_doctor/<int:doctorid>/', views.update_doctor, name='update_doctor'),
    path('AddAppointment/', views.addappointment, name='addappointment'),
    path('add_appointment', views.add_appointment, name='add_appointment'),
    path('AddTreatment/', views.addtreatment, name='addtreatment'),
   path('add_treatment', views.add_treatment, name='add_treatment'),
    path('delete_treatment/<int:treatmentid>/', views.delete_treatment, name='delete_treatment'),
    path('edit_treatment/<int:treatmentid>/', views.edit_treatment, name='edit_treatment'),
    path('update_treatment/<int:treatmentid>/', views.update_treatment, name='update_treatment'),
    path('AddVitals/', views.addvitals, name='addvitals'),
    path('add_vitals', views.add_vitals, name='add_vitals'),
    path('vital-info', views.vital_info, name='vital_info'),
    path('addprescription/',views.addprescription, name='addprescription'),
    path('add_prescription',views.add_prescription,name='add_prescription'),
    path('view_patient_report',views.view_patient_report, name='view_patient_report'),
    path('delete_treatment/<int:treatment_id>', views.delete_treatment, name='delete_treatment'),
    path('delete_medicine/<int:medicine_id>', views.delete_medicine, name='delete_medicine'),


    ]