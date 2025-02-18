import time
import json
from github_client import GitHubClient
from notifier import Notifier
from reporter import Reporter
from subscriber import Subscriber
# from config import config
import requests

# proxies = {
#     "http": "http://104.234.0.191:port",  # 替换为你的代理地址
#     "https": "https://104.234.0.191:port",  # 替换为你的代理地址
# }

# 在请求时使用代理
# response = requests.get("https://www.google.com")


# 加载配置文件
with open('config/config.json') as f:
    config = json.load(f) 

github_client = GitHubClient(config['github']['api_token'])
subscriber = Subscriber(config['github']['repos'])
notifier = Notifier(config['notifications'])
reporter = Reporter()

def main():
    print("Starting the GitHub Sentinel...")

    while True:
        updates = github_client.get_updates(subscriber.get_subscribed_repos())
        report = reporter.generate_report(updates)
        notifier.send_notification(report)

          # 生成报告并发送通知
        report = reporter.generate_report(updates)
        notifier.send_notification(report)
        
        if config['schedule']['frequency'] == 'daily':
            time.sleep(86400)  # 每天一次
        elif config['schedule']['frequency'] == 'weekly':
            time.sleep(604800)  # 每周一次

if __name__ == "__main__":
    main()
