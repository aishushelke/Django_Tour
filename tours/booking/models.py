from django.utils import timezone
from django.db import models
from user.models import user
from package.models import package

class booking(models.Model):


    package_id = models.ForeignKey(package, null=False, blank=False, on_delete=models.CASCADE)
    user_id=models.ForeignKey(user,null=False, blank=False, on_delete=models.CASCADE)
    fromdate = models.DateField()
    todate = models.DateField()

