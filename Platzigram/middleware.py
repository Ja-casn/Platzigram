"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls.base import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platfrom
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_reponse = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is call."""
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in  [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_reponse(request)
        return response