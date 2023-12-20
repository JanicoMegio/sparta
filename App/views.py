import pandas as pd
import time
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import TeleDataForm, ExcelUploadForm, CustomerDataForm
from django.contrib import messages
from .models import TeleData, CustomerData
# Create your views here.



def save_excel(request):
   
    return HttpResponse("Success!!")


def import_excel(request):
    data = CustomerData.objects.filter(agent__user_name="Kyrie32")
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            if excel_file.name.endswith(('.xls', '.xlsx')):
                try:
                    # Read Excel file into a DataFrame
                    data = pd.read_excel(excel_file, engine='openpyxl')
                    # Check for required columns
                    required_columns = ['client_name', 'contact', 'user_id']
                    if not set(required_columns).issubset(data.columns):
                        return HttpResponse("Required columns are missing in the Excel file.")
                    # Iterate over rows and create CustomerData instances
                    for index, row in data.iterrows():
                        # Get or create TeleData instance
                        tele_data_instance, created = TeleData.objects.get_or_create(user_name=row['user_id'])
                        # Create CustomerData instance
                        CustomerData.objects.create(
                            customer_name=row['client_name'],
                            customer_contact=row['contact'],
                            agent=tele_data_instance
                        )

                    return HttpResponse("Data uploaded successfully.")
                except Exception as e:
                    return HttpResponse(f"Error occurred: {str(e)}")
            else:
                return HttpResponse("Please upload a valid Excel file.")
        else:
            return HttpResponse("Form is not valid. Please check your input.")
    else:
        form = ExcelUploadForm()

    return render(request, 'App/dashboard.html', {'form': form, 'data': data})
    



def index(request):
    if request.method == "POST":
        form = TeleDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'STATUS 200 OK')
            return redirect('/')
        else:
             messages.error(request, 'BAD POST')
            
    else:
        form = TeleDataForm()
    return render(request, 'App/index.html', {'form':form})

