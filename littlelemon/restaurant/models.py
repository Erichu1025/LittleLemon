from django.db import models

#class Menu(models.Model):
    #title = models.CharField(max_length=255)
    #price = models.DecimalField(max_digits=6, decimal_places=2)
    #inventory = models.SmallIntegerField(default=0)

    #def __str__(self):
        #return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    # Django will create id field automatically
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()

    def __str__(self): 
        return self.Name

    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    