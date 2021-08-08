from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    married = models.BooleanField()
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
      

class Director(models.Model):
    name = models.CharField(max_length=256)
    fav_actor = models.ForeignKey(Actor, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=256)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    actor = models.ForeignKey(Actor, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    