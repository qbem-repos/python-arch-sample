from ..entity.patient import Patient

class PatientRepositoryInterface:
    def save_changes(self):
        """Save all patients"""
        pass
    
    def add(self, patient: Patient):
        """Save all patients"""
        pass
    
    def remove(self, patient: Patient):
        """Save all patients"""
        pass
    
    def obtain(self, patient: Patient):
        """Save all patients"""
        pass
    
    def find(self, patient: Patient):
        """Find patients by filter"""
        pass