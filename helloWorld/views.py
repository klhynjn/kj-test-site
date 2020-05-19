# from django.shortcuts import render
from mysite.database import my_custom_sql

# Create your views here.
from django.http import HttpResponse
def index(request):
    database=my_custom_sql("select current_database()")
    timestamp=my_custom_sql("select clock_timestamp()")
    response=database+timestamp
    return HttpResponse(response)
