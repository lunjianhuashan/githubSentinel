from github_client import GitHubClient
from reporter import Reporter
import json
import time

def main(): 
 # 读取 config.json 配置
    try:
        with open('config/config.json') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: config.json file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in config.json.")
        return

    github_client = GitHubClient(config['github']['api_token'])
    reporter = Reporter(github_client)

    while True:
        for repo in config['github']['repos']:
            report = reporter.generate_report(repo)
            print(report)
        
        # 根据设置的频率睡眠，默认每天一次
        if config['schedule']['frequency'] == 'daily':
            time.sleep(86400)  # 每天一次
        elif config['schedule']['frequency'] == 'weekly':
            time.sleep(604800)  # 每周一次

if __name__ == "__main__":
    main()
