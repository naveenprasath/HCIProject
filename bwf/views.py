from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required




class IndexView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('home')

        return super(IndexView, self).dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "home.html"

home = login_required(HomeView.as_view())

class SignupView(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = 'home'



