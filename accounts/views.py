from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from accounts.models import Account
from django.template import RequestContext
from django.db import transaction
from accounts.forms import AccountForm, AccountType
from fm.models import Tag
from django.forms.models import model_to_dict


def index(request):
    account_list = Account.objects.order_by('account_name')
    return render(request, 'accounts/account_list.html', {'account_list': account_list})


def account_detail(request, account_id):
    """Returns account details"""
    account = Account.objects.get(id=account_id)
    form = AccountForm.get_AccountForm(account)

    return render_to_response("accounts/account_detail.html", {
        "form": form,
    },
        context_instance=RequestContext(request))


def add_account(request):
    """This method handles the logic of creating an account"""
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                new_tag = Tag(tag_name=request.POST['tag'],
                              tag_description=request.POST['tag_description'])
                new_tag.save()

                account_type = AccountType.objects.get(pk=request.POST['account_type_ref'])

                new_account = form.to_account_model(account_type, new_tag)
                new_account.save()

            return HttpResponseRedirect(reverse('accounts:account_detail', args=(new_account.id,)))
    else:
        form = AccountForm()
    return render_to_response("accounts/add_account.html", {
        "form": form,
    },
        context_instance=RequestContext(request))

