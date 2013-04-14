from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm

class Document(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=2000)
    date_created = models.CharField(max_length=10)
    date_uploaded = models.DateTimeField(default=datetime.datetime.utcnow())
    document_file = models.FileField(upload_to='filetest/%Y/%m/%d')
    # uploaded_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class AccountType(models.Model):
    account_type_name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.account_type_name

class Account(models.Model):
    account_name = models.CharField(max_length=200, unique=True)
    account_number = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    account_type_ref = models.ForeignKey(AccountType)
    date_opened = models.DateTimeField()
    date_closed = models.DateTimeField()
    description = models.CharField(max_length=2000)
    website = models.CharField(max_length=200)
    is_auto_payment = models.BooleanField(default=False)
    auto_payment_method = models.CharField(max_length=1000)
    pin_number = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    rewards_number = models.CharField(max_length=200)
    name_on_the_account = models.CharField(max_length=200)
    address_on_the_account = models.CharField(max_length=200)
    phone_on_the_account = models.CharField(max_length=30)            
    special_phrase_on_the_account = models.CharField(max_length=200)
    has_recurring_activity = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True) 

    def __unicode__(self):
        return self.account_name

class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_description = models.CharField(max_length=2000)
    event_participants = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.event_name        

class Tag(models.Model):
    tag_name = models.CharField(max_length=200, unique=True)
    tag_description = models.CharField(max_length=2000)
    account_ref = models.ForeignKey(Account)
    event_ref = models.ForeignKey(Event)

    def __unicode__(self):
        return self.tag_name

class DocumentTag(models.Model):
    document_ref = models.ForeignKey(Document)
    tag_ref = models.ForeignKey(Tag)

    def __unicode__(self):
        return 'doc ref: %d tag ref: %d' % (self.document_ref, self.tag_ref)