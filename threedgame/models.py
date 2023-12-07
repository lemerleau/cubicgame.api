from django.db import models

# Create your models here.


class RingPosition (models.Model) :
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length = 8)
    color = models.CharField(max_length=100)


class Move (models.Model) :
    id = models.AutoField(primary_key=True)
    listOfRingPosition = models.ManyToManyField(RingPosition)

class CubeData (models.Model) :
    id = models.AutoField(primary_key=True)
    userID = models.CharField(max_length=100) # To be linked to User class from Django
    listOfMoves = models.ManyToManyField(Move)
    numberOfMoves = models.IntegerField()
    status = models.BooleanField();
