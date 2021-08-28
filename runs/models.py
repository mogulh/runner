from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Run(models.Model):
    user = models.ForeignKey(User,related_name="runs" , on_delete=models.CASCADE)
    date= models.DateField(auto_now_add=True)
    start_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_at = models.DateTimeField(blank=True)
    distance = models.PositiveBigIntegerField(blank=True)
    elevation = models.PositiveBigIntegerField(blank=True)
    # duration = models.DurationField()

    def __str__(self) -> str:
        return f"{self.date}"

    @property
    def duration(self):
        tdelta =self.end_at-self.start_at
        return tdelta.total_seconds()

    @property
    def speed(self):
        return self.distance/self.duration

    


class RunStamp(models.Model):
    run = models.ForeignKey(Run, related_name="stamps", on_delete=models.CASCADE)
    start_at = models.PositiveIntegerField()
    end_at = models.PositiveIntegerField()
    

    @property
    def distance(self):
        tdelta =self.end_at - self.start_at
        return tdelta

    @property
    def speed(self):
        return self.distance/60

    
    



