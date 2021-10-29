from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(verbose_name="Address",max_length=100,null=True,blank=True)
    city = models.CharField(verbose_name="City",max_length=100,null=True,blank=True)
    county = models.CharField(verbose_name="County",max_length=100,null=True,blank=True)
    state = models.CharField(verbose_name="State",max_length=2,null=True,blank=True)
    zip_code = models.CharField(verbose_name="Zip Code", max_length=8,null=True,blank=True)
    country = models.CharField(verbose_name="County",max_length=100,null=True,blank=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50,null=True,blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50,null=True,blank=True)
    weekly_pickup = models.CharField(max_length=9)
    one_time_pickup = models.DateField(null=True, blank=True)
    suspend_start = models.DateField(null=True, blank=True)
    suspend_end = models.DateField(null=True, blank=True)
    date_of_last_pickup = models.DateField(null=True, blank=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name