from pydantic import BaseModel, field_validator, EmailStr

class Patient(BaseModel):
    name: str
    email: EmailStr

    @field_validator('name')
    @classmethod
    def name_case(cls, value):
        return value.title()

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_groups = ['philips.com', 'fortis.healthcare', 'apollo.healthcare']
        domain = value.split('@')[-1]
        if domain not in valid_groups:
            raise ValueError('Employee dont belong to priority organisation')
        
        return value
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)

patient_1 = {'name': 'ajay sarma', 'email': 'abhay@philips.com'}
patient_new = Patient(**patient_1)

update_patient_data(patient_new)
    
    