from rest_framework import serializers
from api import models

class subSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.subjectList
        fields='id','code','semester','department','credit'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.userlist
        fields='username','password','category','rollno','department'

class AvaiSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.available
        fields='id','semester','batch'

class ITSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ITS2
        fields='rollno','MA102','PH100','BE110','BE102','PH110','EC100','EC110','CS120','CS100','batch'

class CSSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CSS2
        fields='rollno','MA102','PH100','BE110','BE102','PH110','EE100','EE110','CS120','CS100','batch'

class its1Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.ITS1
        fields='rollno','MA101','CY100','BE100','BE10105','BE103','CY110','CS110','EE110','EE100','batch'
class its3Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.ITS3
        fields='rollno','MA201','CS201','IT201','CS205','IT203','HS200','CS231','IT231','batch'

class its4Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.ITS4
        fields='rollno','MA202','CS202','IT202','IT204','CS208','HS210','IT232','IT234','batch'

class css1Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.CSS1
        fields='rollno','MA101','CY100','BE100','BE10105','BE103','CY110','CS110','EC110','EC100','batch'

class css3Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.CSS3
        fields='rollno','MA201','CS201','CS205','CS203','HS200','CS207','CS231','CS233','batch'

class css4Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.CSS4
        fields='rollno','MA202','CS202','CS204','CS206','HS210','CS208','CS232','CS234','batch'


class userlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.userlist
        fields='username','password','email','category','name','college','department','rollno'



