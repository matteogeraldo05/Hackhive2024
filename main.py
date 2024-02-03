
import re
import time
import json
#git add --all
#git commit -m "hackhive"
#git push origin main 


"""
Patient class with

name(str)
date of birth(str)
checkout/in time(str)
phone number(str)
address(str)
email(str)
doctor(str)
address(list)
occupation(str)
allergies(list)
conditions(list)
sex(str)
race(str)
image(img)
bodycount(int)
healthcard(str)
insurace(str)
credit card(int)
height(int)
weight(int)
emergency contacty(str)



"""


class Patient:
    def __init__(self, firstName, lastName, birthday, married, checkIn, phone, address, email, doctor, occupation, allergies, conditions,gender, sex, ethnicity, image, insurance, credit_card, height, weight, emergency_contact):
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.married = married
        self.checkIn = checkIn
        self.phone = phone
        self.address = address
        self.email = email
        self.doctor = doctor
        self.occupation = occupation
        self.allergies = allergies
        self.conditions = conditions
        self.gender = gender
        self.sex = sex
        self.gender = gender
        self.ethnicity = ethnicity
        self.image = image
        self.insurance = insurance
        self.credit_card = credit_card
        self.height = height
        self.weight = weight
        self.emergency_contact = emergency_contact
    
        self.patient_dict = {
            "First Name": self.firstName,
            "Last Name": self.lastName,
            "Birthday": self.birthday,
            "Married": self.married,
            "Check In Time": self.checkIn,
            "Phone": self.phone,
            "Address": self.address,
            "Email": self.email,
            "Doctor": self.doctor,
            "Occupation": self.occupation,
            "Allergies": self.allergies,
            "Conditions": self.conditions,
            "Gender": self.gender,
            "Sex": self.sex,
            "Gender": self.gender,
            "Ethnicity":self.ethnicity,
            "Image": self.image,
            "Insurance": self.insurance,
            "Credit Card": self.credit_card,
            "Height": self.height,
            "Weight": self.weight,
            "Emergency Contact": self.emergency_contact
            
            }
    
    #check if users phone number configuration is valid
    def validate_phone():
        #'905-721-8668' OR '9057218668'
        while not re.match("^(?!.*\(\d{3}\)\d{3}-\d{4}$)\(?\d{3}\)?-?\d{3}-?\d{4}$", phone):
            print("Invalid phone number format. Please try again.")
            phone = input("Enter Phone Number: ")
        return phone
    
    #check if user email is valid
    def validate_email(self, email):
        while not re.match("[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format. Please try again.")
            email = input("Enter Email: ")
        return email
        
def current_time():
    localTime = time.localtime()
    current_time = time.strftime("%H:%M:%S", localTime)
    return current_time

def create_patient():
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    birthday = input("Enter Birthday: ")
    married = input("Married? YES or NO: ")
    checkIn = current_time()
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    email = input("Enter Email: ")
    doctor = input("Enter Doctor: ")
    occupation = input("Enter Occupation: ")  
    allergies = input("Enter Allergies: ").split()
    conditions = input("Enter Conditions: ").split()
    gender = input("Enter Gender:")
    sex = input("Enter Sex:")
    ethnicity = input("Enter Ethnicity: ")
    insurance = input("Enter Insurance: ")
    credit_card = int(input("Enter Credit Card: "))
    height = int(input("Enter Height: "))
    weight = int(input("Enter Weight: "))
    emergency_contact = input("Enter Emergency Contact: ")

    return Patient(firstName, lastName, birthday, married, checkIn, phone, address, email, doctor, occupation, allergies, conditions,gender, sex,ethnicity,"Image",insurance,credit_card,height,weight,emergency_contact)


patient1 = create_patient()    

#print(patient1.patient_dict)

with open('data.json', 'a') as a:
    json.dump(patient1.patient_dict, a)

with open('data.json', 'a') as a:
    json.dump('\n', a)


for key, value in patient1.patient_dict.items():
    print(f"{key}: {value}")




print()



class Queue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)

    def remove_patient(self):
        return self.queue.pop(0)

    def show_queue(self):
        for patient in self.queue:
            print(patient.firstName, patient.lastName, patient.conditions)
    
    def next_patient(self):
        return self.queue[0]
    
    def queue_length(self):
        return len(self.queue)

#test
    
queue = Queue()
queue.add_patient(patient1)
queue.show_queue()
print("Length of Queue:",queue.queue_length())
queue.remove_patient()
queue.show_queue()
print("Length of Queue:",queue.queue_length())

#speech to text
import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox



def speech_to_text():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mic On")
        audio = r.listen(source)
        print("Mic Off")
    try:
        print("TEXT: "+r.recognize_google(audio))
        return r.recognize_google(audio)
    except:
        messagebox.showerror("Error", "Sorry, I did not get that")


speech_recognition = tk.Tk() 
speech_recognition.geometry("200x200")
speech_recognition.title("Speech Recognition")



speech_recognition.configure()
speech_recognition.resizable("200","200")

button = tk.Button(speech_recognition, text="Start", command=speech_to_text, width=200, height=200)


button.pack()

speech_recognition.mainloop()
