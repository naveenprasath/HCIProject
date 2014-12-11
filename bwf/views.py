from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from bwf.models import User, Bill 
from django.contrib.auth.decorators import login_required
from bwf.forms import UserCreationForm


class IndexView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('home')

        return super(IndexView, self).dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(HomeView, self).get_context_data(**kwargs)
        context['friends'] = user.friend_set.all()
        context['owe_me'] = Bill.objects.owe_me(user)
        context['owe_them'] = Bill.objects.owe_me(user)
        return context

home = login_required(HomeView.as_view())

class SignupView(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = 'home'



