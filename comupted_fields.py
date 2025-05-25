from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    allergies: Optional[List[str]] = None

    @computed_field(return_type= float)
    @property
    def calc_BMI(self):
        bmi = (self.weight/(self.height**2))
        return bmi
#newly computed field name will be same as function name
def update_patient_data(patient: Patient):
    print(patient)  

patient_info = {'name': 'abhay', 'age': 25, 'weight': 69.8, 'height': 1.73}
patient_1 = Patient(**patient_info)

update_patient_data(patient_1)

    

