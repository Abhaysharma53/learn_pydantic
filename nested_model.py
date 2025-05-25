from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict

#another class as an argument for a class
class Address(BaseModel):
    house_no: str
    street_name: str
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    full_address: Address


address_dict = {'house_no': '12/3', 'street_name': 'Dwarka', 'city': 'Delhi', 'state': 'Delhi', 'pin': '110059'}
Address_1 = Address(**address_dict)

patient_info = {'name': 'Abhay', 'age': 25, 'height': 1.72, 'weight': 69.8, 'full_address': Address_1}

patient_1 = Patient(**patient_info)

def get_patient_data(patient: Patient):
    print(patient_1)
    print(patient.weight)
    print(patient_1.full_address)
    print(patient_1.full_address.city)

get_patient_data(patient_1)