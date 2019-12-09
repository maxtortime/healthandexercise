from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.shortcuts import redirect
from django.utils.timezone import now
from django.views.generic import CreateView, MonthArchiveView

from healthandexercise.models import Exercise


class CreateExerciseView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ('name', 'exercise_at')
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        form.instance.exerciser = self.request.user
        return super().form_valid(form)


class IndexView(LoginView):
    template_name = 'healthandexercise/login.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    timezone_now = now()
    template_name = 'healthandexercise/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(settings.LOGIN_REDIRECT_URL)


class BoardView(MonthArchiveView):
    model = Exercise
    date_field = 'exercise_at'
    allow_future = True
    template_name = 'healthandexercise/board.html'
