import requests
from django.conf import settings

GITHUB_API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {settings.GITHUB_ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user_data():
    url = f"{GITHUB_API_URL}/users/{settings.GITHUB_USERNAME}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_repos():
    url = f"{GITHUB_API_URL}/users/{settings.GITHUB_USERNAME}/repos"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_repo_details(repo_name):
    url = f"{GITHUB_API_URL}/repos/{settings.GITHUB_USERNAME}/{repo_name}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def create_issue(repo_name, title, body):
    url = f"{GITHUB_API_URL}/repos/{settings.GITHUB_USERNAME}/{repo_name}/issues"
    data = {"title": title, "body": body}
    response = requests.post(url, json=data, headers=HEADERS)
    return response.json()
