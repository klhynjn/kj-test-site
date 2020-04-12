# from django.shortcuts import render

from mysite.database import db_read_single_value

# Create your views here.
from django.http import HttpResponse
def index(request):
    database=db_read_single_value("select current_database()")
    timestamp=db_read_single_value("select clock_timestamp()")
    response=database+timestamp
    return HttpResponse(response)
