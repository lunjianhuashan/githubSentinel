import requests

class GitHubClient:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'token {self.token}'
        }
        
    def get_latest_release(self, repo):
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()  # 这里返回的JSON中会包含最新的版本信息
        else:
            return None
