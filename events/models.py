from djongo import models

class Event(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    createdBy=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    time = models.TimeField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table='Events'


# Create your models here.
