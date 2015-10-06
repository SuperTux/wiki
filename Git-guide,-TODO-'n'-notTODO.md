Before you start pushing your changes to SuperTux, you should read this. We can't force you to read that, but after someone tells you that your changes are 90% wrong, you get why is it there.

## Do not use your master branch.
This will disable your master branch, so the branch master will be the SuperTux master. Note that you need a permission to access the master branch, so you have to create your own branch after that.

1. Make sure that the remote origin is really the original SuperTux remote.
 * Use `git remote -vv` to show your remotes. `git remote rename <old name> <new name>` to rename a remote.
2. `git branch master --set-upstream-to origin/master` or `git branch master -u origin/master`
3. `git pull`

When you want to change something, create a branch first.

1. Make sure that you are on the master branch by `git branch -vv`.
2. Create a branch by `git branch <branch name>`.
3. Switch to your newly created branch by `git checkout <branch name>`.
4. Change whatever you want and commit it.
5. Push it to your fork by `git push --set-upstream <remote>/<branch>` the first time you do this. After that push only by `git push`. The `<remote>` should be the name of your fork, usually your nickname. Use `git remote -vv` to get the names of all your remotes.
6. Make a pull request.

## Do not mess up with merges.
Rebase your changes instead. So when you want to make your pull request up-to-date with master, then don't use `git pull origin master`, but `git pull --rebase origin master` instead. After that use `git push -f` to push your changes to upstream.

When you want to test someone's chenges, then `git branch <branch name>` and `git branch <branch name> -u <remote>/<branch name>`. Make sure that you are on the root of that branch. Otherwise DO NOT push your merge commit!

## How to squash your commits
Please, squash your commits in pull requests when possible.

Type `git rebase -i HEAD~<number of commits>` and it opens you a kind of gui with the given number of last commits. `pick` means that the commit is visible. If you want to squash the commit into another commit, change the `pick` to `fix` or `f`. After you are done, save it and force-push `git push -f`.

## Other things you should respect
* Do never force-push to a shared branch.
* Don't force/ask/beg other people to update their content.
* Use only constructive criticism.
* Don't beg anyone to learn a new ability.
* Don't revert other people's work unless you're told to do so.
* Don't push errorous commits to master.
* Don't mess up with vague suggestions.
* We don't need any visionaries. Being productive in suggestions those someone could do is dangerous here.
* When you make a big change, don't push it immediately to master. Put it into a pull request and wait for other people's feedback.