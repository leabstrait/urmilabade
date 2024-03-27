import subprocess


def git_commit_push(commit_message):
    commit_message = commit_message or "autocommit - update repo"

    # Commit changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])

    # Pull changes with rebase and autostash
    subprocess.run(["git", "pull", "--rebase", "--autostash"])

    # Push changes
    subprocess.run(["git", "push"])


if __name__ == "__main__":
    commit_message = input("Enter the commit message: ")
    git_commit_push(commit_message)
