from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from accounts.models import Account
from django.template import RequestContext
from django.db import transaction
from accounts.forms import AccountForm, AccountType
from fm.models import Tag


def index(request):
    """Returns list of accounts"""
    account_list = Account.objects.order_by('account_name')
    return render(request, 'accounts/account_list.html', {'account_list': account_list})


def account_detail(request, account_id):
    """Returns account details"""
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account_to_update = get_object_or_404(Account, pk=account_id)
            handle_account_save(request, form, account_to_update)

        updated = "Saved"
    else:
        account = get_object_or_404(Account, pk=account_id)
        form = AccountForm.get_AccountForm(account)
        updated = ""

    return render_to_response("accounts/manage_account.html", {
        "form": form,
        "header": "Manage Account",
        "updated": updated
    },
        context_instance=RequestContext(request))


def add_account(request):
    """This method handles the logic of creating an account"""
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            new_account = handle_account_save(request, form, Account())

            return HttpResponseRedirect(reverse('accounts:account_detail', args=(new_account.id,)))
    else:
        form = AccountForm()

    return render_to_response("accounts/manage_account.html", {
        "form": form,
        "header": "Add New Account"
    },
        context_instance=RequestContext(request))


@transaction.commit_on_success
def handle_account_save(request, form, account):
    """ Handles the db logic to update tag, account type, and account, used by both add and update account
    :param request: the passed request
    :param form: the validated form object
    :return: the saved account object
    """
    db_tag = list(Tag.objects.filter(tag_name=request.POST['tag'])[:1])
    if not db_tag:
        db_tag = Tag(tag_name=request.POST['tag'],
                     tag_description=request.POST['tag_description'])
        db_tag.save()
    else:
        db_tag = db_tag[0]

    account_type = AccountType.objects.get(pk=request.POST['account_type_ref'])

    edited_account = form.to_account_model(account_type, db_tag, account)
    edited_account.save()

    return edited_account