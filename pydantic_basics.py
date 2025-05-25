from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length = 50, title= 'name of the patient', description= 'name of patient in 50 words', examples= ['Abhay', 'Ajay'])]
    age: Annotated[int ,Field(gt = 18, lt = 35)]
    Gender: Annotated[str,Field(default= 'Unknown')]
    email: Annotated[EmailStr, Field(description= 'email id of the patient')]
    married:Annotated[bool, Field(default = False)]
    weight:Annotated[float,Field(gt = 0, strict= True)]
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

