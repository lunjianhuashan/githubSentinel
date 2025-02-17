import time
from github_client import GitHubClient
from notifier import Notifier
from reporter import Reporter
from subscriber import Subscriber
from config import config

def main():
    github_client = GitHubClient(config['github']['api_token'])
    subscriber = Subscriber(config['github']['repos'])
    notifier = Notifier(config['notifications'])
    reporter = Reporter()

    while True:
        updates = github_client.get_updates(subscriber.get_subscribed_repos())
        report = reporter.generate_report(updates)
        notifier.send_notification(report)
        
        if config['schedule']['frequency'] == 'daily':
            time.sleep(86400)  # 每天一次
        elif config['schedule']['frequency'] == 'weekly':
            time.sleep(604800)  # 每周一次

if __name__ == "__main__":
    main()
