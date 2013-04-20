from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from accounts.models import Account
from django.template import RequestContext
from django.db import transaction
from datetime import datetime 
from django.forms.util import ErrorList
from accounts.forms import AccountForm, AccountType
from fm.models import Tag
import dateutil.parser

def index(request):
    account_list = Account.objects.order_by('account_name')
    return render(request, 'accounts/account_list.html', {'account_list': account_list})

def account_detail(request, account_id):
    """Returns account details"""
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'accounts/account_detail.html', {'account': account})    

def add_account(request):
    """This method handles the logic of creating an account"""
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                new_tag = Tag(tag_name = request.POST['tag'],
                    tag_description = request.POST['tag_description'])
                new_tag.save()

                account_type = AccountType.objects.get(pk=request.POST['account_type_ref'])
            
                date_opened = dateutil.parser.parse(request.POST['date_opened'])
                date_closed = dateutil.parser.parse(request.POST['date_closed'])
            
                new_account = Account(account_name = request.POST['account_name'],
                    account_number = request.POST['account_number'],
                    company = request.POST['company'],
                    description = request.POST['description'],
                    website = request.POST['website'],
                    is_auto_payment = request.POST.get('is_auto_payment', False),
                    auto_payment_method = request.POST['auto_payment_method'],
                    year_opened = date_opened.year,
                    month_opened = date_opened.month,
                    day_opened = date_opened.day,
                    year_closed = date_closed.year,
                    month_closed = date_closed.month,
                    day_closed = date_closed.day,
                    pin_number = request.POST['pin_number'],
                    username = request.POST['username'],
                    password = request.POST['password'],
                    rewards_number = request.POST['rewards_number'],
                    name_on_the_account = request.POST['name_on_the_account'],
                    address_on_the_account = request.POST['address_on_the_account'],
                    phone_on_the_account = request.POST['phone_on_the_account'],
                    special_phrase_on_the_account = request.POST['special_phrase_on_the_account'],
                    has_recurring_activity = request.POST.get('has_recurring_activity', False),
                    is_active = request.POST.get('is_active', False),
                    account_type_ref = account_type,
                    tag_ref = new_tag)
                new_account.save()       

            return HttpResponseRedirect(reverse('accounts:account_detail', args=(new_account.id,)))
    else:
        form = AccountForm()
    return render_to_response("accounts/add_account.html", {
        "form": form,
    },
    context_instance=RequestContext(request))
    return ""
