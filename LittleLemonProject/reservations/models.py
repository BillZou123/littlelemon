from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    num_guest = models.IntegerField()
    booking_date  = models.DateField()

    def __str__(self):
        return self.name +"'s booking at "+ str(self.booking_date)
    


class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title + " " + str(self.price) + " " + str(self.inventory)
