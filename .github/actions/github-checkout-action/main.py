import os
import subprocess

repo = os.getenv("INPUT_REPOSITORY")
ref = os.getenv("INPUT_REF")
token = os.getenv("INPUT_TOKEN")

print("Running custom GitHub checkout action...")

if not repo:
    repo = os.getenv("GITHUB_REPOSITORY")

clone_url = f"https://x-access-token:{token}@github.com/{repo}.git"

#clone repository
subprocess.run(["git", "clone", clone_url])

repo_name = repo.split("/")[-1]

#checkout the branch if ref is provided
if ref:
    subprocess.run(["git", "checkout", ref], cwd=repo_name)

print(f"Checked out {repo} at ref {ref if ref else 'default branch'}")