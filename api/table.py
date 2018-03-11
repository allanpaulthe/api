from django.db import models
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from api.serializers import userSerializer,ITSerializer,userlistSerializer
import csv,json,os
from tabula import read_pdf,convert_into
from pprint import pprint
from django.core.management import call_command


def table(request):
    dd="animal1"
    attrs = {
        'name': models.CharField(max_length=32),
        '__module__': 'api.models'
    }
    Animal = type(dd, (models.Model,), attrs)
    call_command('makemigrations')
    call_command('migrate')
    return HttpResponse(status=204)

'''def table(request):
    data={}
    code={}
    attrs = {}
    convert_into("result_TLY.pdf","output.csv", output_format="csv",lattice="True",pages="all",header=None)
    with open("output.csv","r") as f,open('data.json', 'w+') as outfile:
        reader = csv.reader(f)
        for row in reader:
            if len(row[0])==10:
                row[1]=row[1].replace("\n","")
                data.setdefault("data",[]).append({"rollno": row[0],"mark": row[1]})
            if len(row[0])==5:
                data.setdefault("code",[]).append({"code": row[0],"subject": row[1]})
        json.dump(data,outfile, indent=4, sort_keys=True)
    with open("output.csv","r") as f,open('code.json', 'w+') as outfile:
        reader = csv.reader(f)
        for row in reader:
            if len(row[0])==5:
                data.setdefault("code",[]).append({"code": row[0],"subject": row[1]})
        json.dump(data,outfile, indent=4, sort_keys=True)
    #os.remove('./output.csv')
    json_data=open('./data.json')
    data1 = json.load(json_data)
    i=0
    for a in data1['data']:
        rollno=data1['data'][i]['rollno']
        mark=data1['data'][i]['mark']
        Subs = models.marks.objects.create(marks=mark, rollno=rollno)
        Subs.save()
        i=i+1
    json_data=open('./code.json')
    data1 = json.load(json_data)
    i=0
    for a in data1['code']:
        code=data1['code'][i]['code']
        subject=data1['code'][i]['subject']
        Subs = models.subjects.objects.create(code=code,subject=subject)
        Subs.save()
        i=i+1
    with open("output.csv","r") as f,open('x.json', 'w+') as outfile:
        reader = csv.reader(f)
        for row in reader:
            if row[0]=="INFORMATION TECHNOLOGY":
                index=reader.line_num
                li=list(reader)
                i=0
                for x in range(0, 20):
                    if(len(li[x][0])==5):
                        #attrs[li[x][0]]= 'models.CharField(max_length=32)'
                        attrs.update({li[x][0]: 'models.CharField(max_length=32)'})
                        i=i+1
                #attrs['__module__']= "api.models"
                attrs.update({'__module__' : 'api.models'})
                json.dump(attrs,outfile, indent=4, sort_keys=True)
                ITcode = type("ITcode", (models.Model,), attrs)
                call_command('makemigrations')
                call_command('migrate')
    return HttpResponse("success")'''
