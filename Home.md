> **Note:** This Wiki is converted from the previous Mediawiki format,
> this conversion is not complete, but progressed far enough that this
> Wiki is ready to be used again, a lot of outdated information does
> however remain. If you find some, don't delete it, update it and/or
> move it to an appropriatly titled archive page.

This Wiki is used to document the current state of
[SuperTux](https://www.supertux.org) as well as keep track of proposed
additions and changes.

This Wiki is targeted at the developers of the game, not users, users
are however free to check out what is going on behind the scenes.

The [old Mediawiki based Wiki](http://supertux.lethargik.org/wiki/Main_Page) has been merged
into this Wiki and has been switched to read-only mode. It is no
longer updated, but it can still be viewed.

Guidelines and tips for using this Wiki
---------------------------------------

* [[News]] is for keeping track of what is going on in SuperTux
  development. Every substantial addition or change to the game should
  be documented here.

* Do not delete information from this Wiki unless it is completely out
  of date or otherwise useless, prefer moving it over to [[Ideas]],
  [[Reject Ideas]] or another appropriate place instead.

* Use Markdown (`.md`) for the Wikipages.

* Use line-breaks at around 80 characters, the `.md` files are meant to
  be viewed and edited in a text editor

* Run the [validator.py](https://raw.githubusercontent.com/wiki/SuperTux/supertux/validator.py)
  in the Wiki repository to check for broken links.

* New pages should go to the [[_Sidebar]] for easy access.

* Prefer big pages, don't fracture content over too many small pages.

Making changes to the wiki
--------------------------

* Users without write access: Directly editing this Wiki is restricted to developers, you have to submit a pull request. First set up a wiki clone using `git clone https://github.com/SuperTux/supertux.wiki.git` and fork the [wiki repository](https://github.com/SuperTux/wiki) and add your fork as a remote. Make your changes locally and push to your fork, or use Github's file editing UI. Then submit a pull request to the wiki repository through the Github UI.

* Developers with commit access: You can edit the wiki directly through the edit interface in the top right corner. To make local changes, set up the clone as above, so that the `origin` remote is `https://github.com/SuperTux/supertux.wiki.git` (or `git@github.com:SuperTux/supertux.wiki.git` for SSH). Then add the wiki repo as a remote: `git remote add wiki https://github.com/SuperTux/wiki.git` or `git remote add wiki git@github.com:SuperTux/wiki.git.` When you push you should push with a `git push origin` first and then follow it up with `git push wiki`. To merge pull requests, ensure that `wiki` is up-to-date with `origin` by doing a `git pull origin; git push wiki`. (If you have local commits you should `git push origin` in the middle). Then you can merge the request to the wiki repository with the GitHub UI and let the GitHub Action merge it back to the origin repo. Or you can fetch the commits to your local clone and do the merge and push like they're your commits.




SuperTux
--------

* [Github Page](https://github.com/SuperTux/supertux)
* [Download](https://supertux.org/download.html)
* [Contact Us](https://www.supertux.org/contact.html)

For players
-----------

Learn how to play with the [[User Manual]]

Chat on the [SuperTux Forum](http://forum.freegamedev.net/viewforum.php?f=66&sid=7d271ca537028e81027e0b3cdab4f0ca)

For level designer
------------------

Publish levels to the [SuperTux Forum](http://forum.freegamedev.net/viewforum.php?f=66&sid=7d271ca537028e81027e0b3cdab4f0ca),
and if we like the look of them, you may be able to submit levels to the official game.

For coders
-----------

[Build the game](https://github.com/SuperTux/supertux/wiki/Building), and get started.

Fix some [easy bugs](https://github.com/SuperTux/supertux/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%3Aeasy)

Join us on [IRC](https://github.com/SuperTux/supertux/wiki/IRC)
