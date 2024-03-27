import subprocess


def git_commit_push():
    # Commit changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Automatic commit"])

    # Pull changes with rebase and autostash
    subprocess.run(["git", "pull", "--rebase", "--autostash"])

    # Push changes
    subprocess.run(["git", "push"])


if __name__ == "__main__":
    git_commit_push()
