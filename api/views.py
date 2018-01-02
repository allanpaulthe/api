from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from api import models
from api.serializers import ItemSerializer,marksSerializer
import csv,json,os
from tabula import read_pdf,convert_into
from pprint import pprint
from api import models

class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = ItemSerializer

class marksViewSet(viewsets.ModelViewSet):
    queryset = models.marks.objects.all()
    serializer_class = marksSerializer

def datasave(request):
    data={}
    convert_into("result_TLY.pdf","output.csv", output_format="csv",lattice="True",pages="all",header=None)
    with open("output.csv","r") as f,open('data.json', 'w+') as outfile:
        reader = csv.reader(f)
        for row in reader:
            if len(row[0])==10:
                row[1]=row[1].replace("\n","")
                data.setdefault("data",[]).append({"rollno": row[0],"mark": row[1]})
        json.dump(data,outfile, indent=4, sort_keys=True)
    os.remove('./output.csv')
    json_data=open('./data.json')
    data1 = json.load(json_data)
    i=0
    for a in data1['data']:
        rollno=data1['data'][i]['rollno']
        mark=data1['data'][i]['mark']
        Subs = models.marks.objects.create(marks=mark, rollno=rollno)
        Subs.save()
        i=i+1
    now = 'alan'
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

