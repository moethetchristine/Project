from project import patient

Jimmy = patient("Jimmy Steven", 31, "diabetes", "bone crack + outside injuires; would take months to recover", "Dr. Susan")
Ethan = patient("Ethan Paige", 27, "-", "Tuberculosis tested; positive", "Dr. Alex")
Ginny = patient("Ginny Walters", 17, "-", "dengue emergency; no rush recoveries found yet & been sick for a week", "Dr. Michelle")

print(Jimmy.history)
print(Ethan.history)

total_patients = input("Enter total patients: ")
current_appointment_number = int(total_patients)
for new_patient in total_patients:
    current_appointment_number = current_appointment_number + 1/2

print("Your appointment number is: ",current_appointment_number) 

gender = input("Please select your gender:\n(a) Male\n(b) Female\n\n")
blood_type = input("Please choose your blood type:\n(a) A\n(b) B\n(c) AB\n(d) O\n\n")
current_appointment_number = input("Please enter your appointment number: ")
if int(current_appointment_number) > int(total_patients):
    print("Please wait a few minutes for your turn. Thank you!")

