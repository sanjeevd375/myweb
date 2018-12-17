from django.shortcuts import render
from django.conf import settings
import json
from django.http import HttpResponse
from openpyxl import load_workbook
import openpyxl 
import os



# Create your views here.


def home(request):
	return render(request,'myweb/page.html')


def marlabs(request):
	#print ("inside marlabs method")	
	return render(request,'myweb/marlabs.html')
        
def fbview(request):
	json_filepath = os.path.join('.', 'static', 'json', 'data.json')
	data = open(json_filepath).read() #opens the json file and saves the raw contents
	jsonData = json.loads(data) #converts to a json structure
	print(type(jsonData))
	print(jsonData)
	return HttpResponse(json.dumps(jsonData), content_type='application/json')
 
