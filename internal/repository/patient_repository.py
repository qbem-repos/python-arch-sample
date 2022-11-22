from ..interface.repository import PatientRepositoryInterface
from ..entity.patient import Patient

class PatientRepository(Metaclass=PatientRepositoryInterface):
    _data = []
    
    def save_changes(self) -> RuntimeError:
        print("Saving data...")
        return None

    def add(self, patient: Patient) -> bool:
        self._data.append(patient)
    
    def remove(self, patient: Patient) -> bool:
        self._data.remove(patient)

    def obtain(self, id: str) -> tuple(Patient, IndexError):
        for patient in self._data:
            if patient.Id == id:
                return patient, None
        return None, IndexError("")
    
    def find(self) -> list:
        return self._data