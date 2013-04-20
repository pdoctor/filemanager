# -*- coding: utf-8 -*-
from django import forms
from datetime import date
from accounts.models import AccountType

class AccountForm(forms.Form):
    account_name = forms.CharField(max_length=200, label='Account Name')
    account_number = forms.CharField(max_length=200, label='Account Number', required=False)
    company = forms.CharField(max_length=200, label='Company')
    date_opened = forms.CharField(label='Account Opened On', required=False)
    date_closed = forms.CharField(label='Account Closed On', required=False)
    description = forms.CharField(max_length=2000, label='Account Description', widget=forms.Textarea)
    website = forms.CharField(label='Website', required=False)
    is_auto_payment = forms.BooleanField(label='Account uses Autopayment', required=False)
    auto_payment_method = forms.CharField(label='Autopayment Method', required=False)
    pin_number = forms.CharField(max_length=200, label='PIN', required=False)
    username = forms.CharField(max_length=200, label='Username on Account', required=False)
    password = forms.CharField(max_length=200, label='Password hint', required=False)
    rewards_number = forms.CharField(max_length=200, label='Rewards Number', required=False)
    name_on_the_account = forms.CharField(max_length=200, label='Name on Account', required=False)
    address_on_the_account = forms.CharField(max_length=200, label='Address on Account', required=False)
    phone_on_the_account = forms.CharField(max_length=30, label='Phone on Account', required=False)
    special_phrase_on_the_account = forms.CharField(max_length=200, label='Special phrase on account', required=False)
    has_recurring_activity = forms.BooleanField(label='Account has recurring activity', required=False)
    is_active = forms.BooleanField(label='Account is active', required=False) 
    types = map(lambda x: (x.id, x.account_type_name), AccountType.objects.all())
    account_type_ref = forms.ChoiceField(choices=types, widget = forms.Select(), label='Account Type')  
    tag = forms.CharField(max_length=200, label='Tag')
    tag_description = forms.CharField(max_length=2000, label='Tag Description', widget=forms.Textarea)


