from pydantic import BaseModel, model_validator
from typing import Optional, Dict

class Patient(BaseModel):
    name: str
    age: int
    contact_details: Dict[str, str]
    blood_group: str

    @model_validator(mode = 'after')
    def compulsory_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is compulsory for senior citizen')
        return model

def get_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Patient details updated')

patient_info = {'name': 'Abhi', 'age': 65,'contact_details': {'contact': '2345678'}, 'blood_group': 'B+'}

patient_1 = Patient(**patient_info)
get_patient_data(patient_1)