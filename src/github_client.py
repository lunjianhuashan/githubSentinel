import requests

class GitHubClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.github.com/"

    def get_updates(self, repos):
        updates = []
        for repo in repos:
            url = f"{self.base_url}repos/{repo}/commits"
            headers = {"Authorization": f"token {self.api_token}"}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                updates.append(response.json())
            else:
                print(f"Error fetching updates for {repo}: {response.status_code}")
        return updates
