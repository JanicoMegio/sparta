from .models import TeleData, CustomerData
from django import forms

class TeleDataForm(forms.ModelForm):
    class Meta:
        model = TeleData
        fields = '__all__'
        
class CustomerDataForm(forms.ModelForm):
    class Meta:
        model = CustomerData
        fields = '__all__'
        
        
class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()