# -*- coding: utf-8 -*-
from django import forms
from accounts.models import AccountType, Account
import dateutil.parser
from django.forms.models import model_to_dict


class AccountForm(forms.Form):
    account_name = forms.CharField(max_length=200, label='Account Name', widget=forms.TextInput(attrs={'class': 'required', 'minLength': 2 }))
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
    account_type_ref = forms.ChoiceField(choices=types, widget=forms.Select(), label='Account Type')
    tag = forms.CharField(max_length=200, label='Tag')
    tag_description = forms.CharField(max_length=2000, label='Tag Description', widget=forms.Textarea)

    @staticmethod
    def get_AccountForm(account):
        model_dict = model_to_dict(account, fields=[field.name for field in account._meta.fields],
                                   exclude=['account_type_ref', 'tag_ref'])
        model_dict['tag'] = account.tag_ref.tag_name
        model_dict['tag_description'] = account.tag_ref.tag_description

        model_dict['account_type_ref'] = account.account_type_ref.id

        form = AccountForm(model_dict)

        return form


    def to_account_model(self, account_type, new_tag):
        date_opened = dateutil.parser.parse(self.date_opened)
        date_closed = dateutil.parser.parse(self.date_closed)
        new_account = Account(account_name=self.account_name,
                              account_number=self.account_number,
                              company=self.company,
                              description=self.description,
                              website=self.website,
                              is_auto_payment=self.is_auto_payment or False,
                              auto_payment_method=self.auto_payment_method,
                              year_opened=date_opened.year,
                              month_opened=date_opened.month,
                              day_opened=date_opened.day,
                              year_closed=date_closed.year,
                              month_closed=date_closed.month,
                              day_closed=date_closed.day,
                              pin_number=self.pin_number,
                              username=self.username,
                              password=self.password,
                              rewards_number=self.rewards_number,
                              name_on_the_account=self.name_on_the_account,
                              address_on_the_account=self.address_on_the_account,
                              phone_on_the_account=self.phone_on_the_account,
                              special_phrase_on_the_account=self.special_phrase_on_the_account,
                              has_recurring_activity=self.has_recurring_activity or False,
                              is_active=self.is_active or False,
                              account_type_ref=account_type,
                              tag_ref=new_tag)
        return new_account


