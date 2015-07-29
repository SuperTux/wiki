== Repository ==
SuperTux development is coordinated with the help of the Git version control system. In a nutshell, it's a file-storing facility that can be used by multiple users simultaneously, keeping track of changes and archiving old versions of files. You can find out more about Git in general on their [http://git-scm.com/ homepage].

The SuperTux Git repository is accessible through GitHub, available [https://github.com/SuperTux/ here].

== Getting the data (anonymous read-only access) ==
Anonymous read access to the repository is granted to everybody. You will first need to install Git; downloads, tutorials for setting up, and information about using Git are available on the [http://git-scm.com/ Git website]. Once you have installed Git, all you have to do to get your hands on the data is to use the following command in your terminal:

 <nowiki>git clone --recursive https://github.com/SuperTux/supertux.git</nowiki>

This will create a new directory named ''supertux'' which contains the latest versions of the SuperTux source code and data. 
inside the ''supertux'' directory to update to the latest version in the repository. This will only download changed files to save bandwidth.

== Building from Source Code ==
After you obtain the data from the repository, you will need to go through the building process to make a playable version of the game.  Follow the instructions in the ''INSTALL'' file located in the ''supertux'' directory to do this.

Note that after any subsequent update from the Git repository you will likely need to repeat the building process to ensure that all new features are available.

== SuperTux Level Editor ==
Data for the SuperTux level editor is also available through the Git repository.  Accessing the code in Google Code is done by changing the repository from ''default'' to ''editor''.  To obtain a local clone of the editor code use the command:

 <nowiki>git clone https://github.com/SuperTuxTeam/supertux-editor.git</nowiki>

You will need to follow the installation instructions provided with the repository data.

== Ubuntu Repository ==
An Ubuntu repository for the SVN version of SuperTux exists as a [https://launchpad.net/~stownsend42/+archive/supertux-svn Launchpad PPA] To install SuperTux from this repository, add ppa:stownsend42/supertux-svn to your Software Sources, then install the supertux-svn package. At this time, new packages are only being built for lucid (10.04) and maverick (10.10).

NOTE: THIS REPOSITORY IS NO LONGER MAINTAINED. NO NEW BUILDS WILL BE UPLOADED.

If anyone else would like to take up this project, please feel free to do so. If you need help, contact me at stownsend42@sbcglobal.net

== Debian Repository ==
First add the public key to authenticate the repository by running the following:
 <code><nowiki>wget -q https://supertux.lethargik.org/apt/supertux.key -O- | sudo apt-key add -</nowiki></code>

Then add the following to your repository sources (/etc/apt/sources.list or your favorite editor)
 <code><nowiki>deb http://supertux.lethargik.org/apt VERSION contrib</nowiki></code>
Replace VERSION with your Debian version, e.g. lenny/squeeze/sid or stable/testing/unstable.

Finally, install the "supertux-svn" package.

== Gentoo Linux ==
If you have any problems with supertux on [http://gentoo.org/ Gentoo] or trouble understanding the instructions below, please contact <tt>binki</tt> on [[Contact#IRC|<tt>#supertux</tt>]]. He'll be glad to help if he can and to know that his ebuilds are useful ;-).

=== Get the Overlays ===

To install the latest and greatest development versions of supertux and supertux-editor, please grab [http://ohnopub.net/~ohnobinki/gentoo#overlay my overlay]. It includes a few other things than the live supertux ebuild, but if you're not running ~arch (you'll know if you are) this shouldn't affect your Gentoo installation. If you have any issues with the overlay itself, just contact <tt>binki</tt> or [https://ohnopub.net/bugzilla/enter_bug.cgi?product=ohnobinki_overlay file a bug]. To install my overlay, first set up layman. Make sure that the <code>subversion</code> and <code>mercurial</code> useflags are set in <code>/etc/make.conf</code> before emerging layman:

 <code><nowiki>emerge -va layman</nowiki></code>

After layman is installed, it should print out instructions for modifying your <code>make.conf</code>. This will enable portage to see ebuilds in layman-managed overlays. Recent versions of layman will suggest to add something lik the following to <code>make.conf</code>:

 <code><nowiki>source /var/lib/layman/make.conf</nowiki></code>

Then, install the overlays. SuperTux and its dependencies are spread between my overlay and the somewhat more official [http://overlays.gentoo.org/proj/sunrise Sunrise User Overlay].

 <code><nowiki>layman -f -a ohnobinki -a sunrise</nowiki></code>

=== Unmask and Emerge ===

Then, add the necessary package (dependencies of supertux and supertux itself) to <code>/etc/portage/package.keywords</code>. If <code>package.keywords</code> doesn't exist, you may create it in <code>/etc/portage</code>. Deposit the following lines into this file:

 <code><nowiki>dev-libs/findlocale
dev-libs/tinygettext
games-arcade/supertux
dev-games/supertux-editor</nowiki></code>

Now just emerge supertux and/or supertux-editor :-)

 <code><nowiki>emerge -va supertux supertux-editor</nowiki></code>

If you are brave and want builds straight from SVN, place <code>**</code> after the supertux and supertux-editor packages in <code>package.keywords</code>:

 <code><nowiki>games-arcade/supertux **
dev-games/supertux-editor **</nowiki></code>

===Getting the SVN for mac===

I have provided a link to download packaged SVN builds for mac: [[Download/Supertux SVN Version Mac]] [[User:Monster|Monstertux]] 21:03, 13 April 2011 (UTC)

[[Category:Development]]
[[Category:Meta]]
[[Category:SuperTux]]

[[Category:Development]]
[[Category:Meta]]
[[Category:SuperTux]]
