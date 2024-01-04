from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def create_school(request):
    ESO = NameForm()
    d={'forms':ESO}
    if request.method == 'POST':
        SDO = NameForm(request.POST)
        if SDO.is_valid():
            return HttpResponse(str(SDO.cleaned_data))
        else:
            return HttpResponse('Data is invalid')
    return render(request,'create_school.html',d)