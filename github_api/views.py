from rest_framework.response import Response
from rest_framework.decorators import api_view
from .github_service import get_user_data, get_repos, get_repo_details, create_issue


@api_view(["GET"])
def github_profile(request):
    user_data = get_user_data()
    repos = get_repos()
    data = {
        "username": user_data.get("login"),
        "followers": user_data.get("followers"),
        "following": user_data.get("following"),
        "repos": [{"name": repo["name"], "url": repo["html_url"]} for repo in repos]
    }
    return Response(data)


@api_view(["GET"])
def github_repo(request, repo_name):
    repo_details = get_repo_details(repo_name)
    if "message" in repo_details:
        return Response({"error": "Repository not found"}, status=404)
    return Response(repo_details)


@api_view(["POST"])
def github_create_issue(request, repo_name):
    title = request.data.get("title")
    body = request.data.get("body", "")
    if not title:
        return Response({"error": "Title is required"}, status=400)

    issue = create_issue(repo_name, title, body)
    if "html_url" in issue:
        return Response({"issue_url": issue["html_url"]})
    return Response(issue, status=400)
