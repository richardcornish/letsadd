from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView

from .forms import PostForm, ProfileForm
from .models import Post, Profile


def post_create(request):

    # Find currently logged-in user's profile
    # If user is not logged in, we should redirect to the login URL, but 
    # because we don't have a fully fledged auth installed, we will simply get 
    # the first Profile instance instead.
    # (A basic profile object is provided in a fixture.)
    # if request.user.is_authenticated:
    #     profile = request.user.profile
    # else:
    #     return redirect(settings.LOGIN_URL)
    try:
        profile = Profile.objects.get(pk=1)
    except Profile.DoesNotExist:
        profile = None
    if request.method == "POST" and profile is not None:
        form_list = [
            ProfileForm(request.POST, instance=profile),
            PostForm(request.POST)
        ]
        form_list_is_valid = True
        for form in form_list:
            if form.is_valid():
                form.instance.profile = profile
                obj = form.save()
            else:
                form_list_is_valid = False
        if form_list_is_valid:
            obj = form_list[-1].instance
            return redirect(reverse('initial:post_detail', args=[str(obj.pk)]))
    else:
        if profile is not None:
            form_list = [
                ProfileForm(instance=profile),
                PostForm()
            ]
        else:
            form_list = []
    return render(request, 'initial/post_create.html', {
        'form_list': form_list,
        'profile_list': Profile.objects.all(),
        'post_list': Post.objects.all(),
    })


class PostDetailView(DetailView):
    model = Post


class ProfileDetailView(DetailView):
    model = Profile
