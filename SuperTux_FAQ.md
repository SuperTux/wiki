When will the next version of SuperTux be released?
---------------------------------------------------

This is by far the most frequently asked question of all, and the answer is simple:

**When it's done.**

Honestly, we don't have a release date yet. Just like many of you, we'd like to see SuperTux finished and released to the public as soon as possible, but since we all are busy with other, probably less interesting things, the amount of time we are able to put into this game is limited. Please be patient.

When will Milestone 3 be released?
----------------------------------

We plan to release the Linux version on 2038-11-30. Not sure if we will do a GNU Hurd version by then, too. The schedule is a bit sketchy right now.

What's new in SuperTux 0.3?
---------------------------

Most information on these Wiki pages is about what's new in SuperTux 0.3. Just browse around, and feel free to add your own ideas. :-)

How do I use SDL in the development version?
--------------------------------------------

OpenGL was and is the current default renderer. However, 0.3.1 added in support for multiple renderers. The command line option `--renderer sdl` will use the SDL renderer. Note that this is usually slower and does not display some images/levels correctly.

How do you get to or past level x?
----------------------------------

Please see [SuperTux FAQ/Spoilers](SuperTux_FAQ/Spoilers "wikilink").

How do I create levels in 0.3.x?
--------------------------------

The level editor was removed (again), but you can now use the C\# editor instead, which is distributed as a separate package. See [Editor FAQ](Editor_FAQ "wikilink") for some hints on how to use it. You can also create levels in 0.1.3 and play them in 0.3.x.

Why is 0.3.1 considered unstable?
---------------------------------

Please read the [Versioning scheme](Versioning_scheme "wikilink"). It clearly states that all odd release branches are unstable development versions. Now, as to why there isn't a 0.4.x release...

SuperTux 0.3.1? 0.1.3? Subversion?
----------------------------------

Please see our [Versioning scheme](Versioning_scheme "wikilink") page.

How can I get in touch with you?
--------------------------------

Depending on who you want to reach - and for what purpose - you can either join our [IRC channel](Contact#IRC "wikilink") or write to one of the [mailing lists](Contact#Mailing_List "wikilink") (but currently there's just one). Please note that due to massive amounts of spam, we had to set the mailing lists to subscribers-only. If you send emails to the lists and are not subscribed then you will get an automated reply saying that your message is waiting for approval, but it's very likely that we will miss your e-mail in all the spam (we're very sorry about that), so better subscribe before posting to the list.

How can I help?
---------------

-   [Create game content](Contributing "wikilink") in the form of sounds, music, [translations](Translation "wikilink"), [images](Contributing#Artists "wikilink"), and [levels](Contributing#Level_designers "wikilink") - see [Contributing](Contributing "wikilink") for details
-   Write [code](Contributing#Programmers/Code "wikilink") for new features
-   Proofread and improve the program's and the levels' translation (See [Translation](Translation "wikilink"))
-   Work on the story and the settings (all around the wiki, mostly in [:Category:Design](:Category:Design "wikilink"))

There's many things to be done - even besides actually creating game content:

-   Post good [ideas](User_ideas "wikilink") to the wiki
-   Help keep these pages up-to-date and free of spam (See <Special:Recentchanges>)
-   Test the game on a variety of platforms (please read [I found a bug in the developer version!](#I_found_a_bug_in_the_developer_version! "wikilink") first) Check [OldBugs](OldBugs "wikilink") and the [\[Template:MediaWiki:bugtracker-url]([Template:MediaWiki:bugtracker-url "wikilink") bug tracker\] which supersedes that page before posting to see if your problem is already there.
-   Write and/or maintain documentation for [users](User_Manual "wikilink") and [developers](Game_Engine "wikilink")

If you want to help, just [get in touch](Contact "wikilink") and ask.

Is there a preview of the next SuperTux version?
------------------------------------------------

Yes. [Milestone 1.9](Milestone_1.9 "wikilink") is a snapshot of SuperTux without certain buggy features. There are currently Windows and Linux installers.

Why aren't you SuperTuxKart?
----------------------------

Good question. But try <http://supertuxkart.sourceforge.net/> instead.

I found a bug in the developer version!
---------------------------------------

Well, that's not really a question, but great anyway. Keep in mind, however, that SuperTux is bound to have lots of bugs at this stage of development. Actually, chances are quite high that a particular bug is already known but not yet fixed because we just didn't have the time yet.

If you find a bug you think has escaped our attention, make sure you have as much information about when it occurred as possible. This might include steps to reproduce the bug, constellations where the bug won't show, a [backtrace](Providing_a_backtrace "wikilink") of the call stack if you got an exception (use a debugger for this), etc. Then add an entry to the [\[Template:MediaWiki:Bugtracker-url]([Template:MediaWiki:Bugtracker-url "wikilink") bug tracker\].

SuperTux “stable package” version (0.1.3) has a minor error when compiling:
---------------------------------------------------------------------------

That is not a question either, but we do know that you have to change line 210 of menu.h: void Menu::get\_controlfield\_key\_into\_input(MenuItem \*item); becomes void get\_controlfield\_key\_into\_input(MenuItem \*item);

This fix is currently in the 0.1.x branch and [will be released in 0.1.4](http://lists.lethargik.org/pipermail/supertux-devel-lethargik.org/2010-March/002941.html) as soon as someone can find the time to actually make the release.

I'm having sound problems on a system that uses PulseAudio
----------------------------------------------------------

There is a workaround for this problem. Edit the file ~/.alsoftrc (which may not exist) and add the line:

` drivers = oss`

I'm thinking about buying SuperTux.
-----------------------------------

If you have paid for SuperTux, you have been ripped off. Supertux is available for free download at [Download/Installation](Download "wikilink"). An equivalent Live CD, to be downloaded free of charge, is available under [Links](Links "wikilink"). If you *want* to pay for SuperTux, you can make a donation, which would be highly appreciated, but we're not making you pay.

Where did the Forest levels go?
-------------------------------

Versions *0.3.0* and *0.3.1* contained the [Forest world](Forest "wikilink"). In an attempt to get development up to speed after a period of idleness, the focus was narrowed. Development of the Forest world has been moved to [Milestone 3](Milestone_3 "wikilink"). The *0.3.\** and eventually the *0.4.\** versions implement the [Milestone 2 Design Document](Milestone_2_Design_Document "wikilink"), i.e. a game without the Forest world.

The old Forest world is still included in the *0.3.2* version, but it's no longer part of the main game nor our current development focus. To access the Forest world, go to:

  
Contrib Levels → Forest World

\_\_NEWSECTIONLINK\_\_

Can I use the SVN version for Intel Macintoshes?
------------------------------------------------

Yes you can! go to this link: <http://supertux.lethargik.org/wiki/Download/Supertux_SVN_Version_Mac> And follow the instructions.

[Category:For Users](Category:For_Users "wikilink") <Category:FAQs>
