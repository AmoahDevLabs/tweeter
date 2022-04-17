from django.shortcuts import render, get_object_or_404, redirect

from tweets.forms import TweetForm
from tweets.models import Profile, Tweet


def dashboard(request):
    form = TweetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets:dashboard')
    followed_tweets = Tweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')
    return render(request, 'tweets/dashboard.html', {'form': form, 'tweets': followed_tweets})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'tweets/profile_list.html', {'profiles': profiles})


def _profile(request, slug):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'tweets/profile.html', {'profile': profile})
