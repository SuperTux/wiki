**The Subversion (SVN) repository is no longer in use. For the most recent code under development see the [ Git repository](Download/Git "wikilink") instead.**

------------------------------------------------------------------------

Repository
----------

SuperTux development is coordinated with the help of the Subversion version control system. In a nutshell, it's a file-storing facility that can be used by multiple users simultaneously, keeping track of changes and archiving old versions of files. You can find out more about Subversion in general on their [homepage](http://subversion.apache.org/).

Getting the data (anonymous read-only access)
---------------------------------------------

Anonymous read access to the repository is granted to everybody. Once you have installed Subversion, all you have to do to get your hands on the data is to use the following command:

`svn checkout http://supertux.lethargik.org/svn/supertux/trunk/supertux`

This will create a new directory named *supertux* which contains the latest versions of the SuperTux source code and data. Once this is complete, you can use

`svn update`

inside the *supertux* directory to update to the latest version in the repository. This will only download changed files to save bandwidth.

### Locations inside the Subversion repository

Checking out the path above will get you all you need to contribute to SuperTux. However, if you don't want to check out the entire repository, you can just check out the pieces you need. For example, the media directory is notably large and it only necessary if you are working on sounds or graphics.

|                                                                             |                                                                       |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------|
| |**`http://supertux.lethargik.org/svn/supertux/trunk/htdocs`**              | Website source                                                        |
| |**`http://supertux.lethargik.org/svn/supertux/trunk/media`**               | Additional media files, including source files for audio and graphics |
| |**`http://supertux.lethargik.org/svn/supertux/trunk/supertux`**            | Latest SuperTux source                                                |
| |**`http://supertux.lethargik.org/svn/supertux/trunk/supertux-milestone1`** | SuperTux Milestone 1 source                                           |
| |**`http://supertux.lethargik.org/svn/supertux/trunk/supertux-portable`**   | [SuperTux Portable](SuperTux_Portable "wikilink")                     |
| |**`http://supertux.lethargik.org/svn/supertux/trunk/supertux-editor`**     | Official SuperTux level editor that runs under both Mono and MS .NET. |
| |**`http://supertux.lethargik.org/svn/supertux/branches/supertux/0_3_x`**   | SuperTux [Milestone 1.9](Milestone_1.9 "wikilink") branch             |

Creating Patches
----------------

There's a whole section about [creating patches](Contributing#Programmers/Code "wikilink").

Web Access
----------

If you just want to browse through the source a bit, then you can use the [Repository HTTP Interface](http://supertux.lethargik.org/viewvc/viewvc.cgi/trunk/supertux/) which should work well with your web browser.

Developer SVN access
--------------------

If you have submitted some good patches and want to get actively involved in the SuperTux project, [contact](SuperTux_FAQ#How_can_I_get_in_touch_with_you.3F "wikilink") us for write access to the repository. You will then have to issue the following command in the *supertux* directory:

    svn switch --relocate http://supertux.lethargik.org/svn/supertux/trunk/supertux \
      svn+ssh://&lt;your_lethargik_username&gt;@lethargik.org/home/supertux/svn/supertux/trunk/supertux

After running an `svn update` to make sure everything went smoothly, you can start checking in your changes:

`svn commit -m `“`Totally`` ``changed`` ``src/main.cpp`` ``to`` ``implement`` ``HTCPCP!`”

If you only want to commit changes to some files, add their names to the end of the command.

### Move from BerliOS

Contact [sik0fewl](http://supertux.lethargik.org/bugs/view.php?id=8#32) to get developer access if you used to have it on BerliOS. Also sik0fewl is responsible for adding new developers (but other developers have to agree with it first).

When switching to the new SVN from BerliOS (using `switch --relocate`) make sure to be on revision 4542 - **NOT** any later revision (else you will get a checksum error). You can use `svn update -r4542` to downgrade.

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

I have provided a link to download packaged SVN builds for mac: [Download/Supertux SVN Version Mac](Download/Supertux_SVN_Version_Mac "wikilink") [Monstertux](User:Monster "wikilink") 21:03, 13 April 2011 (UTC)

<Category:Development> <Category:Meta> <Category:SuperTux>
