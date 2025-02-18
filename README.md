# GitHub Sentinel

GitHub Sentinel 是一个开源工具类 AI Agent，专为开发者和项目管理人员设计，旨在自动化定期获取并汇总 GitHub 仓库的最新动态。该工具提供以下主要功能：

仓库订阅管理：允许用户订阅多个 GitHub 仓库，实时跟踪它们的更新。
自动更新获取：定期获取和汇总订阅仓库的最新提交、问题、拉取请求等信息。
通知系统：通过电子邮件或其他方式推送仓库更新通知，确保团队成员及时了解最新动态。
报告生成：生成定期的更新报告，帮助团队了解仓库的变化情况，提高团队协作效率。
GitHub Sentinel 适用于需要跟踪多个仓库更新的开发者、项目经理或团队，旨在通过自动化流程提升工作效率，确保项目始终保持最新状态。

## 功能
- 订阅管理
- 更新获取
- 通知系统
- 报告生成

## 安装
1. 克隆项目：
    ```
    git clone https://github.com/your-username/GitHubSentinel.git
    ```

2. 安装依赖：
    ```
    pip install -r requirements.txt
    ```

3. 配置 GitHub API token 和仓库订阅信息，编辑 `config/config.json` 文件。

4. 运行项目：
    ```
    python src/main.py
    ```
