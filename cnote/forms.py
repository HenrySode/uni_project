from django.forms import ModelForm
from .models import ConceptNote
from . import forms

class CNoteForm(ModelForm):
    class Meta:
        model = ConceptNote
        fields = '__all__'

        labels = {
            'description': 'Functional Requirements',
        }
        
    def __init__(self, *args, **kwargs):
        super(CNoteForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})