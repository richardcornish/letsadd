from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ProfileForm
from .models import Profile


class ProfileDetailView(DetailView):
    model = Profile


class ProfileListView(ListView):
    model = Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
