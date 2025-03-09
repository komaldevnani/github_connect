from django.urls import path
from .views import github_profile, github_repo, github_create_issue

urlpatterns = [
    path("github/", github_profile, name="github_profile"),
    path("github/<str:repo_name>/", github_repo, name="github_repo"),
    path("github/<str:repo_name>/issues/", github_create_issue, name="github_create_issue"),
]
