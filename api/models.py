from django.db import models

class Item(models.Model):
    topic=models.CharField(max_length=100)
    description=models.CharField(max_length=500)


class marks(models.Model):
    rollno=models.CharField(max_length=15)
    marks=models.CharField(max_length=200)

class myUser(models.Model):
    username=models.CharField(max_length=32,unique=True,primary_key=True)
    password=models.CharField(max_length=20)

class subjectcodes(models.Model):
    code=models.CharField(max_length=32)
    subject=models.CharField(max_length=50)

class subjectList(models.Model):
    code=models.CharField(max_length=32)
    semester=models.CharField(max_length=32)
    department=models.CharField(max_length=32)
    credit=models.IntegerField()



class ITS2(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA102=models.CharField(max_length=32, blank=True,null=True)
    PH100=models.CharField(max_length=32, blank=True,null=True)
    BE110=models.CharField(max_length=32, blank=True,null=True)
    BE102=models.CharField(max_length=32, blank=True,null=True)
    PH110=models.CharField(max_length=32, blank=True,null=True)
    EC100=models.CharField(max_length=32, blank=True,null=True)
    EC110=models.CharField(max_length=32, blank=True,null=True)
    CS120=models.CharField(max_length=32, blank=True,null=True)
    CS100=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class CSS2(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA102=models.CharField(max_length=32, blank=True,null=True)
    PH100=models.CharField(max_length=32, blank=True,null=True)
    BE110=models.CharField(max_length=32, blank=True,null=True)
    BE102=models.CharField(max_length=32, blank=True,null=True)
    PH110=models.CharField(max_length=32, blank=True,null=True)
    EE100=models.CharField(max_length=32, blank=True,null=True)
    EE110=models.CharField(max_length=32, blank=True,null=True)
    CS120=models.CharField(max_length=32, blank=True,null=True)
    CS100=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class CSS1(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA101=models.CharField(max_length=32, blank=True,null=True)
    CY100=models.CharField(max_length=32, blank=True,null=True)
    BE100=models.CharField(max_length=32, blank=True,null=True)
    BE10105=models.CharField(max_length=32, blank=True,null=True)
    EC100=models.CharField(max_length=32, blank=True,null=True)
    BE103=models.CharField(max_length=32, blank=True,null=True)
    CY110=models.CharField(max_length=32, blank=True,null=True)
    CS110=models.CharField(max_length=32, blank=True,null=True)
    EC110=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class ITS1(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA101=models.CharField(max_length=32, blank=True,null=True)
    CY100=models.CharField(max_length=32, blank=True,null=True)
    BE100=models.CharField(max_length=32, blank=True,null=True)
    BE10105=models.CharField(max_length=32, blank=True,null=True)
    BE103=models.CharField(max_length=32, blank=True,null=True)
    CY110=models.CharField(max_length=32, blank=True,null=True)
    CS110=models.CharField(max_length=32, blank=True,null=True)
    EE110=models.CharField(max_length=32, blank=True,null=True)
    EE100=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class ITS3(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA201=models.CharField(max_length=32, blank=True,null=True)
    CS201=models.CharField(max_length=32, blank=True,null=True)
    IT201=models.CharField(max_length=32, blank=True,null=True)
    CS205=models.CharField(max_length=32, blank=True,null=True)
    IT203=models.CharField(max_length=32, blank=True,null=True)
    HS200=models.CharField(max_length=32, blank=True,null=True)
    CS231=models.CharField(max_length=32, blank=True,null=True)
    IT231=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class CSS3(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA201=models.CharField(max_length=32, blank=True,null=True)
    CS201=models.CharField(max_length=32, blank=True,null=True)
    CS205=models.CharField(max_length=32, blank=True,null=True)
    CS203=models.CharField(max_length=32, blank=True,null=True)
    HS200=models.CharField(max_length=32, blank=True,null=True)
    CS207=models.CharField(max_length=32, blank=True,null=True)
    CS231=models.CharField(max_length=32, blank=True,null=True)
    CS233=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class ITS4(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA202=models.CharField(max_length=32, blank=True,null=True)
    CS202=models.CharField(max_length=32, blank=True,null=True)
    IT202=models.CharField(max_length=32, blank=True,null=True)
    IT204=models.CharField(max_length=32, blank=True,null=True)
    CS208=models.CharField(max_length=32, blank=True,null=True)
    HS210=models.CharField(max_length=32, blank=True,null=True)
    IT232=models.CharField(max_length=32, blank=True,null=True)
    IT234=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class CSS4(models.Model):
    rollno=models.CharField(max_length=100,unique=True,primary_key=True)
    MA202=models.CharField(max_length=32, blank=True,null=True)
    CS202=models.CharField(max_length=32, blank=True,null=True)
    CS204=models.CharField(max_length=32, blank=True,null=True)
    CS206=models.CharField(max_length=32, blank=True,null=True)
    CS208=models.CharField(max_length=32, blank=True,null=True)
    HS210=models.CharField(max_length=32, blank=True,null=True)
    CS232=models.CharField(max_length=32, blank=True,null=True)
    CS234=models.CharField(max_length=32, blank=True,null=True)
    batch=models.CharField(max_length=32, blank=True,null=True)

class userlist(models.Model):
    username=models.CharField(max_length=32,unique=True,primary_key=True)
    password=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    category=models.CharField(max_length=32)
    name=models.CharField(max_length=32)
    college=models.CharField(max_length=32, blank=True,null=True)
    department=models.CharField(max_length=32, blank=True,null=True)
    rollno=models.CharField(max_length=32, blank=True,null=True)

class available(models.Model):
    semester=models.CharField(max_length=32)
    batch=models.CharField(max_length=32)
    class Meta:
        unique_together=["semester","batch"]


