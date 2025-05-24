from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    Gender: str
    email: EmailStr
    allergies: Optional[List[str]] =  None
    contact_info: Dict[str, str]



patient_info = {'name': 'Abhay Sharma', 'age': 25, 'Gender': 'Male', 'email': 'abc@gmail.com', 'contact_info': {'contact_no': '55444454343'}} 
patient_info2 = {'name': 'Abhishek Sharma', 'age': 28, 'Gender': 'Male', 'email': 'abc@gmail.com', 'contact_info': {'contact_no': '55444454343'}} 

patient_1 = Patient(**patient_info)
patient_2 = Patient(**patient_info2)

def get_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.Gender)


get_patient_data(patient_1)
get_patient_data(patient_2)

