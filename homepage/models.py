from django.db import models
from django.utils import timezone
from .constants import SITES_LIST, REGION_LIST
# Create your models here.
#create table with region, site_name, device_name, port_name, port_status, register_date

class Port(models.Model):
    site_name = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    port_name = models.CharField(max_length=100)
    port_status = models.CharField(max_length=100)
    region = models.CharField(max_length=15, choices=REGION_LIST)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.port_name
