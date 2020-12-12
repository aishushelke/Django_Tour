from django.db import models
class package(models.Model):

    pname=models.TextField(max_length=20, null=False, blank=False)
    ptype=models.TextField(max_length=20,null=False, blank=False)
    plocation=models.TextField(max_length=30,null=False,blank=False)
    price=models.FloatField(null=True,blank=False)



