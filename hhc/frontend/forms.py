from django.forms import ModelForm
from .models import CustomeUser

class CustomeUserForm(ModelForm):
    class Meta:
        model  = CustomeUser
        fields = ['user_name','first_name','last_name','address','pin','email','password','reason']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter {field.label}'
