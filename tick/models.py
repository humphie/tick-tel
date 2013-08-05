from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import class_prepared


def longer_username(sender, *args, **kwargs):
    # You can't just do `if sender == django.contrib.auth.models.User`
    # because you would have to import the model
    # You have to test using __name__ and __module__
    if sender.__name__ == "User" and sender.__module__ == "django.contrib.auth.models":
        sender._meta.get_field("username").max_length = 13

class_prepared.connect(longer_username)


#model class for sms
class Credit(models.Model):

    name      = models.CharField(max_length=15)
    credit    = models.IntegerField()
    #return the name of the user
    def __unicode__(self):
        return self.name


#model class for phonebook 
class Phone(models.Model):

    username   = models.CharField(max_length=12)     
    name       = models.CharField(max_length=12)
    group      = models.CharField(max_length=12)
    contact    = models.CharField(max_length=15)
    #return the username
    def __unicode__(self):
        return self.username


class Inbox(models.Model):
    
    sender    = models.CharField(max_length=12)
    recipient = models.CharField(max_length=12)
    message   = models.CharField(max_length=300)
    flag      = models.CharField(max_length=12)
    date      = models.DateField()
    #return the username
    def __unicode__(self):
        return self.sender


class memberAcount(models.Model):

    owner      = models.CharField(max_length=12)
    full_name  = models.CharField(max_length=30, null=True)
    username   = models.CharField(max_length=12)
    password   = models.CharField(max_length=12)
    position   = models.CharField(max_length=14)
    contact    = models.CharField(max_length=15)
    country    = models.CharField(max_length=70)
    group      = models.CharField(max_length=10)
    acc_type   = models.CharField(max_length=12)
    short_desc = models.CharField(max_length=130, null=True)
    thumbnail  = models.ImageField(upload_to='/static/users/', null=True)
    def __unicode__(self):
        return self.username


#amodel for the sms reports
class Report(models.Model):

    username  = models.CharField(max_length=15)
    name      = models.CharField(max_length=15)
    message   = models.CharField(max_length=300)
    recip_num = models.CharField(max_length=500)
    date      = models.DateField()


#model for Calender
class Event(models.Model):
    
    owner       = models.CharField(max_length=15)
    event_title = models.CharField(max_length=30)
    date        = models.DateField()
    description = models.CharField(max_length=140)
    priority    = models.CharField(max_length=10)
    event_type  = models.CharField(max_length=10)
    contact     = models.CharField(max_length=500)
    def __unicode__(self):
        return self.owner
    
