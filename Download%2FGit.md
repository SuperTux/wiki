Repository
----------

SuperTux development is coordinated with the help of the Git version control system. In a nutshell, it's a file-storing facility that can be used by multiple users simultaneously, keeping track of changes and archiving old versions of files. You can find out more about Git in general on their [homepage](http://git-scm.com/).

The SuperTux Git repository is accessible through GitHub, available [here](https://github.com/SuperTux/).

Getting the data (anonymous read-only access)
---------------------------------------------

Anonymous read access to the repository is granted to everybody. You will first need to install Git; downloads, tutorials for setting up, and information about using Git are available on the [Git website](http://git-scm.com/). Once you have installed Git, all you have to do to get your hands on the data is to use the following command in your terminal:

`git clone --recursive https://github.com/SuperTux/supertux.git`

This will create a new directory named *supertux* which contains the latest versions of the SuperTux source code and data. inside the *supertux* directory to update to the latest version in the repository. This will only download changed files to save bandwidth.

Building from Source Code
-------------------------

After you obtain the data from the repository, you will need to go through the building process to make a playable version of the game. Follow the instructions in the *INSTALL* file located in the *supertux* directory to do this.

Note that after any subsequent update from the Git repository you will likely need to repeat the building process to ensure that all new features are available.

SuperTux Level Editor
---------------------

Data for the SuperTux level editor is also available through the Git repository. Accessing the code in Google Code is done by changing the repository from *default* to *editor*. To obtain a local clone of the editor code use the command:

`git clone https://github.com/SuperTuxTeam/supertux-editor.git`

You will need to follow the installation instructions provided with the repository data.

Ubuntu Repository
-----------------

An Ubuntu repository for the SVN version of SuperTux exists as a [Launchpad PPA](https://launchpad.net/~stownsend42/+archive/supertux-svn) To install SuperTux from this repository, add ppa:stownsend42/supertux-svn to your Software Sources, then install the supertux-svn package. At this time, new packages are only being built for lucid (10.04) and maverick (10.10).

NOTE: THIS REPOSITORY IS NO LONGER MAINTAINED. NO NEW BUILDS WILL BE UPLOADED.

If anyone else would like to take up this project, please feel free to do so. If you need help, contact me at stownsend42@sbcglobal.net

Debian Repository
-----------------

First add the public key to authenticate the repository by running the following:

`wget -q https://supertux.lethargik.org/apt/supertux.key -O- | sudo apt-key add -`

Then add the following to your repository sources (/etc/apt/sources.list or your favorite editor)

`deb http://supertux.lethargik.org/apt VERSION contrib`

Replace VERSION with your Debian version, e.g. lenny/squeeze/sid or stable/testing/unstable.

Finally, install the “supertux-svn” package.

Gentoo Linux
------------

If you have any problems with supertux on [Gentoo](http://gentoo.org/) or trouble understanding the instructions below, please contact `binki` on [`#supertux`](Contact#IRC "wikilink"). He'll be glad to help if he can and to know that his ebuilds are useful ;-).

### Get the Overlays

To install the latest and greatest development versions of supertux and supertux-editor, please grab [my overlay](http://ohnopub.net/~ohnobinki/gentoo#overlay). It includes a few other things than the live supertux ebuild, but if you're not running ~arch (you'll know if you are) this shouldn't affect your Gentoo installation. If you have any issues with the overlay itself, just contact `binki` or [file a bug](https://ohnopub.net/bugzilla/enter_bug.cgi?product=ohnobinki_overlay). To install my overlay, first set up layman. Make sure that the `subversion` and `mercurial` useflags are set in `/etc/make.conf` before emerging layman:

`emerge -va layman`

After layman is installed, it should print out instructions for modifying your `make.conf`. This will enable portage to see ebuilds in layman-managed overlays. Recent versions of layman will suggest to add something lik the following to `make.conf`:

`source /var/lib/layman/make.conf`

Then, install the overlays. SuperTux and its dependencies are spread between my overlay and the somewhat more official [Sunrise User Overlay](http://overlays.gentoo.org/proj/sunrise).

`layman -f -a ohnobinki -a sunrise`

### Unmask and Emerge

Then, add the necessary package (dependencies of supertux and supertux itself) to `/etc/portage/package.keywords`. If `package.keywords` doesn't exist, you may create it in `/etc/portage`. Deposit the following lines into this file:

`dev-libs/findlocale` `dev-libs/tinygettext` `games-arcade/supertux` `dev-games/supertux-editor`

Now just emerge supertux and/or supertux-editor :-)

`emerge -va supertux supertux-editor`

If you are brave and want builds straight from SVN, place `**` after the supertux and supertux-editor packages in `package.keywords`:

`games-arcade/supertux **` `dev-games/supertux-editor **`

### Getting the SVN for mac

I have provided a link to download packaged SVN builds for mac: [Download/Supertux SVN Version Mac](Download/Supertux_SVN_Version_Mac "wikilink") [Monstertux](mediawiki/Users/monster) 21:03, 13 April 2011 (UTC)

<Category:Development> <Category:Meta> <Category:SuperTux> <Category:Development> <Category:Meta> <Category:SuperTux>
