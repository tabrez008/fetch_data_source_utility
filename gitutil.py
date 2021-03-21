import git
import os
import sys

try:
    repo = git.Repo.clone_from(
        "git@github.com:tabrez008/Rating-System.git", "src", branch="master"
    )
except Exception as e:
    print("Oops!", sys.exc_info()[0], "occurred.")
    pass

    # print(e)

# branch = repo.git.checkout("-b master")
repo = git.Repo("src")
# branch = repo.git.checkout("-b master")
# print(branch)
# repo = git.Repo.init('my_new_repo')
repo.remotes.origin.pull("master")
# g = git.Git('git@github.com:tabrez008/Rating-System.git')
# g.pull('origin','master')
# List all branches
for branch in repo.branches:
    print(branch)


def find_files(search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if "swagger" in dir:
            #    print(files)
            print(str(dir))
            print(os.listdir(root + "/swagger"))
            files_in_dir = os.listdir(root + "/swagger")
            for file in files_in_dir:
                print(os.path.join(root + "/swagger", file))
                result.append(os.path.join(root + "/swagger", file))
        #    result.extend(os.path.join(roo , file))

    #    print(root,dir,files)
    #    result.append(os.path.join(root, filename))
    return result


#    for roots,dirs,files in os.walk('C:\\Users\\lifei\\Desktop\\Papers'):
#                     print(roots,dirs,files)


# Create a new branch
# repo.git.branch('my_new_branch')
# You need to check out the branch after creating it if you want to use it
# repo.git.checkout('my_new_branch3')

# To checkout master again:
branch = repo.git.checkout("master")
print(branch)
print(os.getcwd())
# os.chdir("src")
print(os.getcwd())
dir = os.path.isdir(repo.working_tree_dir)
repo_dir = repo.git_dir.startswith(repo.working_tree_dir)
print(repo_dir)

# print(find_files(os.getcwd()))