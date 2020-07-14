from django.shortcuts import render
from django.views.generic import TemplateView
from apps.mainsite.app_models.users import User

class Home(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'user': User,
        }