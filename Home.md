> **Note:** This Wiki is converted from the previous Mediawiki format, this conversion is not
  complete, but progressed far enough that this Wiki is ready to be used again, a lot of outdated
  information does however remain. If you find some, don't delete it, update it and/or move it to
  an appropriatly titled archive page.

This Wiki is used to document the current state of [SuperTux](https://www.supertux.org) as
well as keep track of proposed additions and changes.

This Wiki is targeted towards developers of the game, users are however free to check out what
is going on behind the scenes.

The now unavailable [old Mediawiki based Wiki](http://supertux.lethargik.org/wiki/Main_Page) has been merged
into this Wiki.

Guidelines and tips for using this Wiki
---------------------------------------

* [[News]] is for keeping track of what is going on in SuperTux
  development. Every substantial addition or change to the game should
  be documented there.

* Do not delete information from this Wiki, prefer moving it over to [[Ideas]],
  [[Rejected Ideas]] or another appropriate place instead.

* Use Markdown (`.md`) for the Wikipages.

* Use line-breaks at around 80 characters, the `.md` files are meant to
  be viewed and edited in a text editor.

* Run the [validator.py](https://raw.githubusercontent.com/wiki/SuperTux/supertux/validator.py)
  in the Wiki repository to check for broken links.

* New pages should go to the [[_Sidebar]] for easy access.

* Prefer big pages, don't fracture content over too many small pages.

Making changes to the wiki
--------------------------

* Users without write access: Directly editing this Wiki is restricted to developers, you have to
  submit a pull request. Go to the [wiki repository](https://github.com/SuperTux/wiki) and try to
  edit; GitHub will automatically make a fork for you. Then submit a pull request to the wiki
  repository through the Github UI. Or you can check it out locally and edit, it's just a git repo.

* Developers with commit access: You can edit the wiki directly through the edit interface in the top
  right corner; a hook will push changes to the wiki repository. To make local changes, clone the wiki
  repository linked above and push as normal; a hook will push the changes to the supertux.wiki repository.
  Pull requests can be merged as normal, since they will also be synced via the hook. If the hook screws
  up, clone the wiki repo and add a wiki remote: `git remote add wiki https://github.com/SuperTux/supertux.wiki.git`
  or `git remote add wiki git@github.com:SuperTux/supertux.wiki.git.` Then merge the origin and wiki remotes
  and push to both, `git pull origin; git pull wiki; git push origin master; git push wiki master`. You may
  need to force push if you rebased instead of merged.

---

General Links
-------------

* [Download The Game](https://supertux.org/download.html)
* [Source Code](https://github.com/SuperTux/supertux)
* [Contact Us](https://www.supertux.org/contact.html)

For Players
-----------

To learn how to play, check out the [[User Manual]].

Chat on the [SuperTux Forum](http://forum.freegamedev.net/viewforum.php?f=66&sid=7d271ca537028e81027e0b3cdab4f0ca)
or our [Discord](https://discord.gg/AcvtHWz)

For Level Designer
------------------

Share your levels on the [SuperTux Forum](http://forum.freegamedev.net/viewforum.php?f=66&sid=7d271ca537028e81027e0b3cdab4f0ca),
or our [Discord](https://discord.gg/AcvtHWz) and if we like the look of them, you may be able to submit levels to the official game.

Submit your own level packs or worlds to the [Add-on Repository](https://github.com/SuperTux/addons) so more players can see and play
your levels. [More info](https://github.com/SuperTux/supertux/wiki/Add-ons)

For Coders
-----------

[Build the game](https://github.com/SuperTux/supertux/wiki/Building), and get started.

Fix some [easy bugs](https://github.com/SuperTux/supertux/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%3Aeasy).
