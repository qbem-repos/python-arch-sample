from ..entity.patient import Patient

class PatientRepositoryInterface:
    """A person superclass"""

    def save_changes(self) -> RuntimeError:
        pass
    
    def add(self, patient: Patient):
        pass
    
    def remove(self, patient: Patient):
        pass
    
    def obtain(self, id: str) -> tuple(Patient, IndexError):
        pass
    
    def find(self) -> list:
        pass