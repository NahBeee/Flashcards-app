# from django.db import models

# Create your models here.
from email.policy import default
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models

num_boxes =5
boxes = range(1,num_boxes +1)

class Card(models.Model):
    question = models.CharField(max_length= 100) #the maximum length of the field.
    answer= models.CharField(max_length=100)
    box= models.IntegerField(
        choices= zip(boxes, boxes),
        default= boxes[0],
    )
    date_created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def move(self,solved):
        new_box= self.box + 1 if solved else boxes[0]

        if new_box in boxes:
            self.box= new_box
            self.save()

        return self