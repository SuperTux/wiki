Before you start pushing your changes to SuperTux, you should read this. We can't force you to read it, but if you are at all new to git then you will almost certainly mess up at some point. This should help to avoid some mistakes that may be specific to Supertux.

Here are some of our recommendations for working with git:

- **Do not use the `master` branch to make pull requests**
  - This will tie said branch to the pull request. It might happen that other stuff gets added to the SuperTux master branch while your pull request is under review. In that case, resolving conflicts to getting your master branch to work for your next pull request is hard.
- Make sure that the remote origin is really the main SuperTux remote
  1. Use `git remote -vv` to show your remotes. `git remote rename <old name> <new name>` to rename a remote
  2. `git branch master --set-upstream-to origin/master` or `git branch master -u origin/master`
  3. `git pull`
- **When you want to change something, create a branch first**
  1. Make sure that you are on the master branch by `git branch -vv`
  2. Create a branch by `git branch <branch name>`
  3. Switch to your newly created branch by `git checkout <branch name>`
  4. Change whatever you want and commit it
  5. Push it to your fork by `git push --set-upstream <remote>/<branch>` the first time you do this. After that push only by `git push`. The `<remote>` should be the name of your fork, usually your nickname. Use `git remote -vv` to get the names of all your remotes
  6. Make a pull request
- **Do not merge branches, or pull without --rebase**
  - Merges create extra merge commits we don't need and want in our main repo
  - Rebase your changes instead. So when you want to make your pull request up-to-date with master, use `git pull --rebase origin master` rather than a simple `git pull origin master`
  - If you rebased your changes, you will want to use `git push --force-with-lease` to push your changes to your fork
- When you want to test someone's changes
  - `git branch <branch name>` and `git branch <branch name> -u <remote>/<branch name>`
  - Make sure that you are on the root of that branch. Otherwise DO NOT push your merge commit!

## How to rebase your commits

Unless you have more than 20 commits in one pull request, don't squash normal commits down until asked. This makes it easier to check your code for problems if any occur. When it is agreed that your pull request is worth adding to the project, then you may be asked to rebase.

For a tutorial on rebasing look [here](https://help.github.com/articles/about-git-rebase/).

In order to get the rebase changes to take effect you will have to force push to your fork of supertux. **Only force push to your own fork of Supertux**.

## Other things you should respect

- Never force-push to a shared branch
- Don't constantly ask other people to update their content
- Use only constructive criticism, as being rude or acting annoyed could scare off a potential developer!
- Don't beg anyone to teach you something. Instead, ask them for guidance if you encounter a problem when following an online tutorial
- Don't revert other people's work unless you're told to do so
- Don't push erroneous commits to master
- Don't be too vague, try to be as specific as possible
- When you make a big change, push it to your forked GitHub repository and make a pull request
- Owners: Try not to push more than 3 commits straight to master at once. For small changes it should be rebased first and for big changes it should be put in a pull request
