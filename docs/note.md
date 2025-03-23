1. 小而频繁的提交：每次完成一个功能模块或修复一个问题时进行提交。提交信息要清晰，例如：
`git commit -m "Add function to visualize sorting algorithm"`
`git commit -m "Fix bug in merge sort visualization"`


2. 有意义的提交信息：遵循简单的约定，比如“动词 + 描述”（如 “Add”, “Fix”, “Update”），方便后期查看历史。


3. 使用分支, 即使是一个人开发，分支仍然很有用，可以让你在不破坏主代码的情况下尝试新功能。

4. 主分支（通常是 main 或 master）：保持稳定，用于存放可运行的代码。 
5. 功能分支：为每个新功能或实验创建一个分支，例如：
```bash
git branch feature/sorting-visualization
git checkout feature/sorting-visualization
```

6. 完成后合并到主分支：
```bash
git checkout main
git merge feature/sorting-visualization

# 删除不再需要的分支
git branch -d feature/sorting-visualization。
```


7. 推送至 GitHub

```bash
# 将本地仓库关联到远程仓库：
git remote add origin <GitHub仓库URL>
git push -u origin main

# 定期推送代码到 GitHub（例如每天结束时或完成一个功能时）
git push
```


8. 一个人开发自己的项目的 Git 工作流

```bash
# 开发新功能
git checkout -b feature/xxx
# 编写代码并提交
git add .
git commit -m "Add xxx feature"
# 合并到主分支
git checkout main
git merge feature/xxx
# 推送到远程
git push
```
