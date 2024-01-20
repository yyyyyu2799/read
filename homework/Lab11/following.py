from github import Github

# 替换成你的GitHub token
token = "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"

# 创建GitHub实例
g = Github(token)

# 获取当前用户
user = g.get_user()

# 获取你关注的人列表（而不是关注你的人）
following = user.get_following()

# 存储你关注的人的仓库数据到本地文件
with open("following_repos.txt", "w", encoding="utf-8") as file:
    for followed_user in following:
        file.write(f"Following: {followed_user.login}\n")
        repos = followed_user.get_repos()
        for repo in repos:
            file.write(f"  - Repo: {repo.full_name}\n")

print("Data has been stored to following_repos.txt.")