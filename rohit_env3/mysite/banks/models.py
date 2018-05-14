from django.db import models

# Create your models here.


class Banks(models.Model):
   name = models.TextField()

   def __str__(self):
       return self.name

class Branches(models.Model):
    ifsc = models.TextField( primary_key=True)
    bank_id = models.ForeignKey(Banks, related_name="Banks", on_delete=models.CASCADE)
    branch = models.TextField()
    address = models.TextField()
    city = models.TextField()
    district = models.TextField()
    state = models.TextField()

    def __str__(self):
        return self.ifsc
