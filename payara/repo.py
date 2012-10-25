import subprocess
import os
import settings

def clone(repo_name, repo_user):
    # create repo dir if it doesn't exist
    if not os.path.exists(settings.REPOS_ROOT):
        os.makedirs(directory)

    os.chdir(settings.REPOS_ROOT)
    subprocess.call('git clone --depth 1 ssh://%s/%s/%s' % (settings.GIT_HOST, repo_user, repo_name), shell=True)

def pull(repo_path):
    os.chdir(repo_path)
    subprocess.call('git pull -f', shell=True)

def update(repo_name, repo_user):
    repo_path = os.path.join(settings.REPOS_ROOT, repo_name)
    if os.path.exists(repo_path):
        pull(repo_path)
    else:
        clone(repo_name, repo_user)
