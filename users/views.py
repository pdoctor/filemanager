# Create your views here.
from users.forms import LoginForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def create_user(request):
    pass


def index(request):
    pass


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/fm/')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_on_success_to = request.GET.get('next')
                    return HttpResponseRedirect(redirect_on_success_to)
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
        else:
            return render_to_response("users/login.html", {
                                      "form": form,
                                      },
                                      context_instance=RequestContext(request))
    else:
        form = LoginForm()
    return render_to_response("users/login.html", {
        "form": form,
    },
        context_instance=RequestContext(request))
