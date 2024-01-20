from github import Github

# 替换成你的GitHub token
token = "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"

# 创建GitHub实例
g = Github(token)

# 获取当前用户
user = g.get_user()

# 获取关注者列表
followers = user.get_followers()

# 存储关注者的仓库数据到本地文件
with open("followers_repos.txt", "w", encoding="utf-8") as file:
    for follower in followers:
        file.write(f"Follower: {follower.login}\n")
        repos = follower.get_repos()
        for repo in repos:
            file.write(f"  - Repo: {repo.full_name}\n")

print("Data has been stored to followers_repos.txt.")