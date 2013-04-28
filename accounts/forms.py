# -*- coding: utf-8 -*-
from django import forms
from accounts.models import AccountType, Account
import dateutil.parser
from django.forms.models import model_to_dict


class AccountForm(forms.Form):
    account_name = forms.CharField(max_length=200, label='Account Name',
                                   widget=forms.TextInput(attrs={'class': 'required', 'minLength': 2}))
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

    def to_account_model(self, account_type, new_tag, account):
        date_opened = dateutil.parser.parse(self.cleaned_data['date_opened'])
        date_closed = dateutil.parser.parse(self.cleaned_data['date_closed'])
        account.account_name = self.cleaned_data['account_name']
        account.account_number = self.cleaned_data['account_number']
        account.company = self.cleaned_data['company']
        account.description = self.cleaned_data['description']
        account.website = self.cleaned_data['website']
        account.is_auto_payment = self.cleaned_data['is_auto_payment'] or False
        account.auto_payment_method = self.cleaned_data['auto_payment_method']
        account.year_opened = date_opened.year
        account.month_opened = date_opened.month
        account.day_opened = date_opened.day
        account.year_closed = date_closed.year
        account.month_closed = date_closed.month
        account.day_closed = date_closed.day
        account.pin_number = self.cleaned_data['pin_number']
        account.username = self.cleaned_data['username']
        account.password = self.cleaned_data['password']
        account.rewards_number = self.cleaned_data['rewards_number']
        account.name_on_the_account = self.cleaned_data['name_on_the_account']
        account.address_on_the_account = self.cleaned_data['address_on_the_account']
        account.phone_on_the_account = self.cleaned_data['phone_on_the_account']
        account.special_phrase_on_the_account = self.cleaned_data['special_phrase_on_the_account']
        account.has_recurring_activity = self.cleaned_data['has_recurring_activity'] or False
        account.is_active = self.cleaned_data['is_active'] or False
        account.account_type_ref = account_type
        account.tag_ref = new_tag

        return account


