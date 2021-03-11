from django.db import models
from django.urls import reverse



class Truck_card(models.Model):
    truck_name = models.CharField(max_length=61)
    truck_year = models.IntegerField()
    mileage_in_km = models.IntegerField()
    location = models.CharField(max_length=99)
    price = models.IntegerField()
    photo = models.ImageField()
    HP = models.IntegerField()
    torque = models.IntegerField()
    weight = models.IntegerField()
    max_speed = models.IntegerField()
    fuel_tank = models.IntegerField()
    lifting_capacity = models.IntegerField()
    description = models.TextField()




    def get_absolute_url(self):
        return reverse('Truck_card', kwargs={'pk': self.pk})


class Photo(models.Model):
    truck = models.ForeignKey(Truck_card, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(blank=True, null=True)

