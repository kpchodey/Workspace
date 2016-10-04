from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Appium(models.Model):            #Appium
    name = models.CharField(max_length=30)
    details = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Appium"


class Storm(models.Model):           #Storm
    name = models.CharField(max_length=30)
    details = models.TextField(blank = True)
    date = models.DateTimeField()
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Storm"


class Revo(models.Model):           #Revo
    SuiteName = models.CharField(max_length=255)
    Test_Case = models.CharField(max_length=255)
    FileName = models.CharField(max_length=255)
    Total_Action = models.CharField(max_length=255)
    Pass = models.CharField(max_length=255)
    Fail = models.CharField(max_length=255)
    Exe_Time = models.CharField(max_length=255)
    Result = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name_plural = "Revo"


class Set_Top_Box(models.Model):           #Set Top Box
    Device_Type = models.CharField(max_length=30)
    IP_Adress = models.CharField(max_length=30)
    Model_Name = models.CharField(max_length=30)
    Serial_Number = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Set Top Box"


class Test_Suite(models.Model):
    Test_Suite_Name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Test Suite"

    def __unicode__(self):
            return self.Test_Suite_Name

