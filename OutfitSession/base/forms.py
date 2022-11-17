from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import User,DT_model,Connect_Model


class DT_form(forms.ModelForm):
    class Meta:
        model = DT_model
        fields = ['date', 'time','status','email'] 
        widgets = {
            'date': AdminDateWidget(),
            'time': AdminTimeWidget(),
        }
        labels = {'email':"Your Email Address"}


class UserRegisterFormAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','age','country','email','password1','password2','description','is_superuser']

    def __init__(self,*args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2','is_superuser']:
            self.fields[fieldname].help_text = None
            self.fields['is_superuser'].label = 'Designer'
            
        
        
class Connect_form(forms.ModelForm):
    class Meta:
        model = Connect_Model
        fields = "__all__"
        