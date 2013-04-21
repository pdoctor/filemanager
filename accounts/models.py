from django.db import models


class AccountType(models.Model):
    account_type_name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.account_type_name


class Account(models.Model):
    account_name = models.CharField(max_length=200, unique=True)
    account_number = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    account_type_ref = models.ForeignKey(AccountType)
    year_opened = models.PositiveSmallIntegerField()
    month_opened = models.PositiveSmallIntegerField()
    day_opened = models.PositiveSmallIntegerField()
    year_closed = models.PositiveSmallIntegerField()
    month_closed = models.PositiveSmallIntegerField()
    day_closed = models.PositiveSmallIntegerField()
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
    tag_ref = models.ForeignKey('fm.Tag')

    def __unicode__(self):
        return self.account_name


