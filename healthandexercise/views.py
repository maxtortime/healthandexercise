from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from healthandexercise.models import Exercise


class CreateExerciseView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ('name',)
    success_url = '/'

    def form_valid(self, form):
        form.instance.exerciser = self.request.user
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'healthandexercise/user-profile.html'


class IndexView(LoginView):
    template_name = 'healthandexercise/login.html'
    success_url = reverse_lazy('create-exercise')


class BoardView(TemplateView):
    template_name = 'healthandexercise/board.html'
