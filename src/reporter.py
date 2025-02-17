class Reporter:
    def generate_report(self, updates):
        report = "GitHub Repository Updates\n\n"
        for repo_updates in updates:
            for commit in repo_updates:
                report += f"Commit: {commit['commit']['message']}\n"
                report += f"Author: {commit['commit']['author']['name']}\n"
                report += f"Date: {commit['commit']['author']['date']}\n\n"
        return report
