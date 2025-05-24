from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length = 50)
    age: int = Field(gt = 18, lt = 35)
    Gender: str
    email: EmailStr
    married: bool = Field(default= False)
    weight: float = Field(gt = 0)
    allergies: Optional[List[str]] =  Field(max_length= 5, default= None) #can't add more than 5 values
    contact_info: Dict[str, str]



#patient_info = {'name': 'Abhay Sharma', 'age': 25, 'Gender': 'Male', 'email': 'abc@gmail.com', 'contact_info': {'contact_no': '55444454343'}} 
#patient_info2 = {'name': 'Abhishek Sharma', 'age': 28, 'Gender': 'Male', 'email': 'abc@gmail.com', 'contact_info': {'contact_no': '55444454343'}} 
patient_info3 = {'name': 'Abhishek Sharma', 'age': 28, 'Gender': 'Male', 'email': 'abc@gmail.com', 'contact_info': {'contact_no': '55444454343'}, 'weight': 75.2, 'allergies': ['pollen', 'dust'], 'married': True} 

# patient_1 = Patient(**patient_info)
# patient_2 = Patient(**patient_info2)
patient_3 = Patient(**patient_info3)

def get_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.Gender)


#get_patient_data(patient_1)
get_patient_data(patient_3)

