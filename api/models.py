from django.db import models

# Create your models here.
"""
class Leg(models.Model):
    time_of_departure = models.TimeField()
    time_of_arrival = models.TimeField()
    date_of_departure = models.DateField()
    date_of_arrival = models.DateField()
    business_class_ticket_num = models.IntegerField()
    economy_class_ticket_num = models.IntegerField()

    def __str__(self):
        return "Date: "+str(self.date_of_departure)+" - "+str(self.date_of_arrival)+" || "+"Date: "+str(self.time_of_departure)+" - "+str(self.time_of_arrival)
"""
class Flight(models.Model):
    departure = models.CharField(max_length=30)
    arrival = models.CharField(max_length=30)
    #legs = models.ManyToManyField(Leg)
    price = models.FloatField(default=174.2)
    time_of_departure = models.TimeField()
    time_of_arrival = models.TimeField()
    date_of_departure = models.DateField()
    date_of_arrival = models.DateField()
    business_class_ticket_num = models.IntegerField()
    economy_class_ticket_num = models.IntegerField()

    def __str__(self):
        return "Flight: "+str(self.departure)+" - "+str(self.arrival)

