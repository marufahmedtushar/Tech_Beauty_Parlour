from django.db import models

# Create your models here.


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70, default="")
    shedule = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.first_name


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    cover = models.ImageField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.name


class AddProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name


class AddService(models.Model):
    id = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    txt = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.first_name