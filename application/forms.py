from django import forms
from .models import Storage

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['storage_initial', 'description']  # Fields yang akan ditampilkan di form
        """widgets = {
            'storage_initial': forms.TextInput(attrs={'placeholder': 'e.g., RK, FL'}),
            'description': forms.TextInput(attrs={'placeholder': 'e.g., RACK, FLOOR'}),
        }"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Iterate through each field and set widget attributes
        for field_name, field in self.fields.items():
        
            if self.errors.get(field_name):
                # Add 'is-invalid' class to fields with errors
                field.widget.attrs.update({'class': 'form-control parsley-error'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
