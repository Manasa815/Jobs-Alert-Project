from django.db import models

class HydJobs(models.Model):
    role=models.CharField(max_length=20)
    positions=models.IntegerField()
    address=models.CharField(max_length=20)
    mail=models.EmailField(max_length=20)

class BangloreJobs(models.Model):
    role=models.CharField(max_length=20)
    positions=models.IntegerField()
    address=models.CharField(max_length=20)
    mail=models.EmailField(max_length=20)

class PuneJobs(models.Model):
    role=models.CharField(max_length=20)
    positions=models.IntegerField()
    address=models.CharField(max_length=20)
    mail=models.EmailField(max_length=20)


