from github_client import GitHubClient

class Reporter:
    def __init__(self, github_client):
        self.github_client = github_client
    
    def generate_report(self, repo):
        release_info = self.github_client.get_latest_release(repo)
        if release_info:
            return f"Latest release version for {repo}: {release_info['tag_name']}, Released at: {release_info['published_at']}"
        else:
            return "Could not retrieve release info."
