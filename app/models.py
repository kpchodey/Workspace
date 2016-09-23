from django.db import models
from django.contrib.auth.models import User


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
    id_test_result = models.CharField(max_length=30)
    date = models.DateTimeField()
    suite_name = models.CharField(max_length=30)
    project_name = models.CharField(max_length=30)
    test_case_id = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    tester = models.CharField(max_length=30)
    box_type = models.CharField(max_length=30)
    box_unit_adress = models.CharField(max_length=30)
    box_ip = models.CharField(max_length=30)
    total_actions = models.CharField(max_length=30)
    toatl_conditions = models.CharField(max_length=30)
    pass_numbers = models.CharField(max_length=30)
    fail_numbers = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    execution_time = models.DateTimeField()
    test_job_name = models.CharField(max_length=30)
    test_job_executionid = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Revo"

class Set_Top_Box(models.Model):           #Set Top Box
    Device_Type = models.CharField(max_length=30)
    IP_Adress = models.CharField(max_length=30)
    Model_Name = models.CharField(max_length=30)
    Serial_Number = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Set Top Box"

