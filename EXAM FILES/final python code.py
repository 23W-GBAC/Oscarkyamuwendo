# THIS IS MY PYTHON CODE SCRIPT FOR MY AUTOMATION PROJECT
import os
import subprocess

# Installing zsh which works as a shell
def install_zsh():
    os.system("sudo apt-get update && sudo apt-get install zsh")

def install_zsh_mac():
    os.system("brew install zsh")

# the function below installs the zsh-suggestions 
def install_zsh_autosuggestions():
    os.system("brew install zsh-autosuggestions")

def activate_autosuggestions():
    autosuggestions_command = "source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh"
    with open(os.path.expanduser("~/.zshrc"), "a") as f:
        f.write(autosuggestions_command)

# installing vim as my editor 
def install_vim():
    os.system("brew install vim")

#Function which creates ssh key inorder to work with the repository on a local machine
def create_ssh_key(email):
    os.system(f"ssh-keygen -t rsa -b 4096 -C \"{email}\"")

def clone_repository(repo_url):
    os.system(f"git clone {repo_url}")

def push_changes():
    os.system("git add . && git commit -m \"Your commit message here\" && git push origin master")

def create_pull_request():
    # Assuming the user is on the correct branch and has made changes
    os.system("git push origin your_branch_name")

# function calls out functions defined above
def main():
    # Problem 1: Install Zsh
    install_zsh()

    # Problem 1 (Mac): Install Zsh
    install_zsh_mac()

    # Problem 1: Install Zsh Autosuggestions
    install_zsh_autosuggestions()

    # Problem 1: Activate Autosuggestions
    activate_autosuggestions()

    # Problem 2: Install Vim
    install_vim()

    # Problem 3: Create SSH Key
    create_ssh_key("your_email@example.com")

    # Problem 3: Clone Repository
    clone_repository("git@github.com:username/repository.git")

    # Problem 3: Push Changes
    push_changes()

    # Problem 3: Create Pull Request
    create_pull_request()

if __name__ == "__main__":
    main()
