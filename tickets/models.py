from djongo import models


# Create your models here.

class Tickets(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    bookedBy = models.CharField(max_length=100)
    eventId = models.CharField(max_length=100)

    class Meta:
        db_table = 'Tickets'
