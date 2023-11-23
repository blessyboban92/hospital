import json
from datetime import datetime

from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.db.models import Q
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from hiapp.models import ItemMaster
from django.urls import reverse

from .models import *
page_load_counter = 1
def demo(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            messages.error(request,"Bad Credentials")
            return render(request,'login.html',{'csrf_token': get_token(request)})
    return render(request,'login.html')
def addpatient(request):
    global page_load_counter
    current_year = datetime.now().year
    hospital_name = 'HS'  # Replace with your company name
    series_code = f"{hospital_name}/{current_year}/REG/{page_load_counter}"

    # Increment the page load counter for the next page load
    page_load_counter += 1

    patient_list = list(PatientMaster.objects.all())
    patient_list.reverse()
    context = {
        'patient_list': patient_list,
        'series_code':series_code
    }
    return render(request, 'patientregister.html',context)
def add_patient(request):
    patient_list = list(PatientMaster.objects.all())
    patient_list.reverse()
    if request.method == "POST":
        patientid= request.POST['patientid']
        patientname = request.POST['patientname']
        gender = request.POST['gender']
        age = request.POST['age']
        address = request.POST['address']
        mobile1 = request.POST['mobile1']
        mobile2 = request.POST['mobile2']
        patient = PatientMaster(patientid=patientid, patientname=patientname, gender=gender, age= age, address=address,
                             mobile1=mobile1, mobile2=mobile2)
        patient.save()
        messages.info(request, "Patient Registred Successfully")
        return redirect('patientapp:addpatient')
    context = {
        'patient_list': patient_list,
    }
    return render(request, 'patientregister.html', context)
def delete_patient(request, patientid):
    patient_list = PatientMaster.objects.get(id=patientid)
    patient_list.delete()
    messages.info(request, "Patient Deleted Successfully")
    return redirect('patientapp:add_patient')
def adddoctor(request):
    doctors = list(DoctorMaster.objects.all())
    doctors.reverse()
    context = {
        'doctors': doctors
    }
    return render(request,'doctorregister.html',context)
def add_doctor(request):
    doctors = DoctorMaster.objects.all()
    if request.method == "POST":
        doctorname= request.POST['doctorname']
        department = request.POST['department']
        Doctors = DoctorMaster(doctorname=doctorname,department=department)
        Doctors.save()
        messages.info(request, "Doctor registred successfully")
        return redirect('patientapp:add_doctor')
    context = {

        'doctors': doctors
    }
    return render(request,'doctorregister.html',context)
def delete_doctor(request,doctorid):
        doctors=DoctorMaster.objects.get(id=doctorid)
        doctors.delete()
        messages.info(request,"Doctor Deleted Successfully")
        return redirect('patientapp:add_doctor')
def update_doctor(request,doctorid):
    doctors = DoctorMaster.objects.get(id=doctorid)
    doctors.doctorname= request.POST['doctorname']
    doctors.department = request.POST['department']
    doctors.save()
    messages.info(request,"Doctor Details updated successfully")
    return redirect('patientapp:add_doctor')
def edit_doctor(request,doctorid):
    sel_doctors=DoctorMaster.objects.get(id=doctorid)
    doctors=DoctorMaster.objects.all()
    context = {
        'sel_doctors':sel_doctors,
        'doctors':doctors
    }
    return render(request, 'doctorregister.html', context)
def addappointment(request):
    doctor = DoctorMaster.objects.all()
    patient = PatientMaster.objects.all()
    appointments = list(AppointmentMaster.objects.all())
    appointments.reverse()
    context = {
        'doctor': doctor,
        'patient': patient,
        'appointments':appointments
    }
    return render(request,'appoinment.html',context)
def add_appointment(request):
    appointments = AppointmentMaster.objects.all()
    if request.method == "POST":
        patientname = request.POST['patientname']
        mobile1 = request.POST['mobile1']
        doctorname = request.POST['doctorname']
        day = request.POST['day']
        time = request.POST['time']
        Appointments = AppointmentMaster(patientname=patientname,mobile1=mobile1,doctorname=doctorname,date=day,time=time)
        Appointments.save()
        messages.info(request, "Appoinment Taken successfully")
        return redirect('patientapp:addappointment')
    context = {

        'appointments': appointments
    }
    return render(request,'appoinment.html',context)
def addtreatment(request):
    treatments = list(TreatmentMaster.objects.all())
    treatments.reverse()
    context = {
        'treatments': treatments
    }
    return render(request,'treatment.html',context)
def add_treatment(request):
    treatments = TreatmentMaster.objects.all()
    if request.method == "POST":
        treatmentname= request.POST['treatmentname']
        description = request.POST['description']
        Treatments = TreatmentMaster(treatmentname=treatmentname,description=description)
        Treatments.save()
        messages.info(request, "Treatment saved successfully")
        return redirect('patientapp:add_treatment')
    context = {

        'treatments': treatments
    }
    return render(request,'treatment.html',context)
def delete_treatment(request,treatmentid):
        treatments=TreatmentMaster.objects.get(id=treatmentid)
        treatments.delete()
        messages.info(request,"Treatment Deleted Successfully")
        return redirect('patientapp:add_treatment')
def update_treatment(request,treatmentid):

    treatments = TreatmentMaster.objects.get(id=treatmentid)
    treatments.treatmentname= request.POST['treatmentname']
    treatments.description = request.POST['description']
    treatments.save()
    messages.info(request,"Treatment updated successfully")
    return redirect('patientapp:add_treatment')
def edit_treatment(request,treatmentid):
    sel_treatments=TreatmentMaster.objects.get(id=treatmentid)
    treatments=TreatmentMaster.objects.all()
    context = {
        'sel_treatments':sel_treatments,
        'treatments':treatments
    }
    return render(request, 'treatment.html', context)

def addvitals(request):
    pres_counter, created = PresCounter.objects.get_or_create(id=1)
    pres_counter.presno += 1
    pres_counter.save()
    current_year = datetime.now().year
    hospital_name = 'HS'
    series_code = f"{hospital_name}/{current_year}/PRE/{pres_counter.presno}"
    doctor = DoctorMaster.objects.all()
    patient = PatientMaster.objects.all()
    vitals = list(VitalMaster.objects.all())
    vitals.reverse()
    today = date.today()
    formatted_today = today.strftime('%Y-%m-%d')

    context = {
        'doctor': doctor,
        'patient': patient,
        'vitals':vitals,
        'series_code': series_code,
        'today_date': formatted_today,
    }
    return render(request,'vitals.html',context)
def add_vitals(request):
    vitals = VitalMaster.objects.all()
    if request.method == "POST":
        prescriptionno = request.POST['prescriptionno']
        date = request.POST['date']
        patientid = request.POST['patientid']
        patientname = request.POST['patientname']
        age = request.POST['age']
        doctorname = request.POST['doctorname']
        temperature = request.POST['temperature']
        dbp = request.POST['dbp']
        resrate = request.POST['resrate']
        height = request.POST['height']
        spo2 = request.POST['spo2']
        sbp = request.POST['sbp']
        pulserate = request.POST['pulserate']
        weight = request.POST['weight']
        bmi = request.POST['bmi']
        vitals = VitalMaster(prescriptionno=prescriptionno, date= date,patientid=patientid,patientname=patientname,age=age,
                              doctorname=doctorname,temperature=temperature,dbp=dbp,resrate=resrate,height=height,
                             spo2=spo2,sbp=sbp,pulserate=pulserate,weight=weight,bmi=bmi)
        vitals.save()
        messages.info(request, "Vital information saved successfully")
        return redirect('patientapp:add_vitals')
    context = {

        'vitals': vitals
    }
    return render(request, 'vitals.html', context)


def vital_info(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
    else:
        selected_date = request.GET.get('date', datetime.now().date())

    vitals = VitalMaster.objects.filter(date=selected_date)
    context = {
        'vitals': vitals,
        'selected_date': selected_date,

    }
    return render(request, 'vitalchart.html', context)
def addprescription(request):
    #prescription_number = request.GET.get('prescription_number')
    vitals_id = request.GET.get('vitals_id')
    prescription_info = None
    consultation = None
    treatment_data = None
    medicine_data = None
    try:
        vital = VitalMaster.objects.get(pk=vitals_id)
        prescription_info = vital.prescriptionno
        consultation = ConsultationModel.objects.filter(prescriptionno=prescription_info).first()
        if consultation:
            treatment_data = ConsultationTreatment.objects.filter(consultation_model=consultation)
            medicine_data = ConsultationMedicine.objects.filter(consultation_model=consultation)

    except VitalMaster.DoesNotExist:
        print(f"VitalMaster with vitals_id {vitals_id} does not exist")
    treatments = TreatmentMaster.objects.all()
    items = ItemMaster.objects.all()
    context = {
        'treatments':treatments,
        'items':items,
        'vitals_id': vitals_id,
        'prescription_number': prescription_info,
        'consultation': consultation,
        'treatment_data': treatment_data,
        'medicine_data': medicine_data
        #'prescription_number':prescription_number
    }
    return render(request, 'prescription.html', context)
# views.py
def add_prescription(request):
    consultation = None
    if request.method == 'POST':
        vitals_id = request.POST.get('vitals_id')
        prescriptionno = request.POST['prescriptionno']
        complaints = request.POST['complaints']
        presentmedhis = request.POST['presentmedhis']
        pastmedhis = request.POST['pastmedhis']
        pastsurghis = request.POST['pastsurghis']
        allergies = request.POST['allergies']
        investresult = request.POST['investresult']
        instruction = request.POST['instruction']
        vital, created = VitalMaster.objects.get_or_create(prescriptionno=prescriptionno)
        treatment_data_json = request.POST.get('treatment_data', '[]')
        treatment_data = json.loads(treatment_data_json)
        medicine_data_json = request.POST.get('medicine_data', '[]')
        medicine_data = json.loads(medicine_data_json)
        if not created:
            vital.status = "Updated"  # Update status or other fields if needed
            vital.save()
            existing_consultation = ConsultationModel.objects.filter(prescriptionno=prescriptionno).first()
            if existing_consultation:
                existing_consultation.complaints = complaints
                existing_consultation.presentmedhis = presentmedhis
                existing_consultation.pastmedhis = pastmedhis
                existing_consultation.pastsurghis = pastsurghis
                existing_consultation.allergies = allergies
                existing_consultation.investresult = investresult
                existing_consultation.instruction = instruction
                existing_consultation.save()
                existing_consultation.consultation_treatments.all().delete()
                existing_consultation.consultation_medicines.all().delete()
                for treatment in treatment_data:
                    treatmentname = treatment.get('treatmentname')
                    treatmentdate = treatment.get('treatmentdate')
                    treatmentduration = treatment.get('treatmentduration')
                    existing_treatment = ConsultationTreatment.objects.filter(
                        treatmentname=treatmentname,
                        treatmentdate=treatmentdate,
                        treatmentduration=treatmentduration,
                        consultation_model=existing_consultation
                    ).first()
                    if not existing_treatment:
                        ConsultationTreatment.objects.create(
                            treatmentname=treatmentname,
                            treatmentdate=treatmentdate,
                            treatmentduration=treatmentduration,
                            consultation_model=existing_consultation
                        )
                medicine_data_json = request.POST.get('medicine_data', '[]')
                medicine_data = json.loads(medicine_data_json)
                for medicine in medicine_data:
                    itemname = medicine.get('itemname')
                    route = medicine.get('route')
                    freequency = medicine.get('freequency')
                    medicine_method = medicine.get('medicine_method', None)
                    medstartdate = medicine.get('medstartdate')
                    medenddate = medicine.get('medenddate')
                    existing_medicine = ConsultationMedicine.objects.filter(
                        itemname=itemname,
                        route=route,
                        freequency=freequency,
                        medicine_method=medicine_method,
                        medstartdate=medstartdate,
                        medenddate=medenddate,
                        consultation_model=existing_consultation
                    ).first()
                    if not existing_medicine:
                        ConsultationMedicine.objects.create(
                            itemname=itemname,
                            route=route,
                            freequency=freequency,
                            medicine_method=medicine_method,
                            medstartdate=medstartdate,
                            medenddate=medenddate,
                            consultation_model=existing_consultation
                        )
                messages.info(request, "Prescription data updated successfully")
            else:
                consultation = ConsultationModel.objects.create(
                    prescriptionno=prescriptionno,
                    complaints=complaints,
                    presentmedhis=presentmedhis,
                    pastmedhis=pastmedhis,
                    pastsurghis=pastsurghis,
                    allergies=allergies,
                    investresult=investresult,
                    instruction=instruction,
                    vitals=vital
                )
                treatment_data_json = request.POST.get('treatment_data', '[]')
                treatment_data = json.loads(treatment_data_json)
                for treatment in treatment_data:
                    treatmentname = treatment.get('treatmentname')
                    treatmentdate = treatment.get('treatmentdate')
                    treatmentduration = treatment.get('treatmentduration')
                    ConsultationTreatment.objects.create(
                        treatmentname=treatmentname,
                        treatmentdate=treatmentdate,
                        treatmentduration=treatmentduration,
                        consultation_model=consultation
                    )
                medicine_data_json = request.POST.get('medicine_data', '[]')
                medicine_data = json.loads(medicine_data_json)
                for medicine in medicine_data:
                    itemname = medicine.get('itemname')
                    route = medicine.get('route')
                    freequency = medicine.get('freequency')
                    medicine_method = medicine.get('medicine_method')
                    medstartdate = medicine.get('medstartdate')
                    medenddate = medicine.get('medenddate')
                    ConsultationMedicine.objects.create(
                        itemname=itemname,
                        route=route,
                        freequency=freequency,
                        medicine_method=medicine_method,
                        medstartdate=medstartdate,
                        medenddate=medenddate,
                        consultation_model=consultation
                    )
            messages.info(request, "Prescription data saved successfully")
            try:
                vital.status = "Saved"
                vital.save()
            except Exception as e:
                print(f"Error updating VitalMaster status: {e}")
        return redirect('patientapp:vital_info')
    return render(request, 'prescription.html')
def view_patient_report(request):
    if request.method == 'POST':
        patientid = request.POST.get('patientid')
        selected_date = request.POST.get('date')
        try:
            patient = PatientMaster.objects.get(patientid=patientid)
            vitals = VitalMaster.objects.filter(patientid=patientid, date=selected_date)
            if vitals:
                consultation_data = ConsultationModel.objects.filter(vitals=vitals.first()).first()
                return render(request, 'patientsummaryreport.html', {
                    'patient': patient,
                    'vitals': vitals.first(),
                    'consultation_data': consultation_data,
                })
            else:
                return render(request, 'patientsearchreport.html',
                              {'error_message': 'No data found for the selected patient ID and date.'})
        except (VitalMaster.DoesNotExist, ConsultationModel.DoesNotExist, PatientMaster.DoesNotExist):
            return render(request, 'patientsearchreport.html',
                          {'error_message': 'No data found for the selected patient ID and date.'})
    return render(request, 'patientsearchreport.html')
def delete_treatment(request, treatment_id):
    treatment = get_object_or_404(ConsultationTreatment, id=treatment_id)
    if request.method == 'POST':
        vitals_id = treatment.consultation_model.vitals.id
        treatment.delete()
        return redirect(reverse('patientapp:addprescription') + f'?vitals_id={vitals_id}')
def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(ConsultationMedicine, id=medicine_id)
    if request.method == 'POST':
        vitals_id = medicine.consultation_model.vitals.id
        medicine.delete()
        return redirect(reverse('patientapp:addprescription') + f'?vitals_id={vitals_id}')

