[[Template:Attention|s=<big>'''Please click on the "+" above or use [http://supertux.lethargik.org/wiki/index.php?title=Talk:Editor_FAQ&action=edit&section=new this link] if you want to ask about a separate issue.'''</big>]]

== Reset point/checkpoint ==
Hi. I don't want to be a pain, so I apologize if this is stupid. How do you place the checkpoint or midpoint of a level?
:I assume you mean a reset point (that is a point that if you die at you will start again at it). Place a "Reset Point" object where you want it. Can be found in the object list just below the bad guys.<br />Note that this FAQ is for the SuperTux-sharp editor for SVN and '''not''' for the editor built into SuperTux 0.1.2/0.1.3. ''If'' you are using the 0.1.3 built in editor: you can't place a reset point, use flexlay instead or edit the file by hand.<br />--[[User:AnMaster|AnMaster]] 16:03, 24 Oct 2006 (CEST)

== Windows: Path problems ==
I wasn't able to get the windows version of the SVN level editor as linked at [http://supertux.lethargik.org/wiki/Download/Installation] to work, as it will not accept the provided directory defaults - I think it may be due to the dos directory convention of using "\" instead of "/"  ? (my windows pc is out of action at the moment but it appeared to say something to the effect of "cannot find E:\SuperTux\/whatever") -R A
:The full error message is needed for us to help you. It worked for me last time I tested on windows. And as far as I remember the editor converts \ to / and vice versa as needed. Anyway please use the [http://supertux.lethargik.org/bugs/ bug tracker] for bugs. It should not go on the editor faq talk page. --[[User:AnMaster|AnMaster]] 07:29, 19 January 2007 (PST)

== Ubuntu: Old mono ==
The version of Mono in the Ubuntu repositories seems to be to old to run the editor, resulting in the "Object reference not set to an instance of an object" error. How can I get a version of Mono in Ubuntu that works with the editor?
:Hm I don't run Ubuntu so I don't know, I will ask people some who use Ubuntu next time I see them. --[[User:AnMaster|AnMaster]] 08:02, 1 February 2007 (UTC)
:: Runs fine for me on Ubuntu 6.06 LTS. I don't recall installing anything specific (other than the Mono packages from Ubuntu but possibly Multiverse - can't remember)

== Mac OS X: Intel ==
Is there any way to run this under Mac OS X (@Intel)?
-Shylence 19:28, 13 March 2007 (UTC)
: Yes if you can get Mono working, see also the section [[Editor FAQ#Does the editor work under Mac OS X?|Does the editor work under Mac OS X?]] --[[User:AnMaster|AnMaster]] 08:07, 11 June 2007 (UTC)
:Okay, but where is the mac level editor? --[[User:Queser|AnQueser]] 08:07, 11 June 2007 (UTC)

== OpenSuse: GTK# version ==
Re:the comments about OpenSuse - version 10.2 comes with gtk-sharp2-2.8.0* etc and afaics this is what generates the problem - installing gtk-sharp2-2.10.* glade-sharp2-2.10.* and glib-sharp2-2.10.* from the appropriate architecture in http://download.opensuse.org/distribution/SL-OSS-factory/inst-source/suse/ seems to do the trick! - Derek [[User:85.210.6.69|85.210.6.69]] 19:14, 4 August 2007 (UTC)

== White Box ==

I'm sorry if this is stupid, but my editor is working fine. There's just one small problem: there's a white box sort of on the map where you draw the tiles in and I can't see what I've already done. It's there, but I just can't see it! Who can help me???

:I have same problem on my Ubuntu 8.04. ATI graphic card can be problem?

::I have the same problem, Ubuntu 8.04. --[[User:194.144.37.128|194.144.37.128]] 15:28, 20 June 2008 (UTC)
::It works fine if I compile from source, svn. --[[User:194.144.37.128|194.144.37.128]] 16:23, 20 June 2008 (UTC)

:::I can't compile :( is there easier way?
::::Which editor did you try? The Autopackage from [[Download/Unstable#Release_0.3.0]] or one that comes with your distribution? --[[User:WolfgangB|WolfgangB]] 18:47, 27 June 2008 (UTC)
::::I can't find a supertux-editor package in the repositories; so i belive it was intalled from autopackage... I have the same white box, it only displays (for .2 seg) when changing the window or left clicking. It seems it is a distro/library problem. Ubuntu 8.04.
:::::@I have same problem on my Ubuntu 8.04. ATI graphic card can be problem?
 No, MacPro's come with those and they're powerful. I get that stupid problem too.

== scrolling and no thing under bad guys ==

hi, dont want to be annoying. how do you make the level scroll in the editor? and, i cant find anything else apart from bad guys in the menu. HELP!!!! i am using the built in editor. 0.1.3.

:There should be some arrows in the top left/right corners to let you scroll. Tiles are under various categories from the tilegroups portion. Have you tried reading the editor help? --[[User:Mathnerd314|Mathnerd314]] 23:53, 5 May 2008 (UTC)

== Windows vista ==

I have installed mono, but when I try to open the editor it suddenly closes. What other gtk packages are you mentioning in the FAQ.( I´m using supertux editor 3.0
reply---10/5/10
I had a problem like that. try uninstalling your editor, then reinstalling. if it asked for your directory, remember to select the data folder.  But now I have a black box where the tlemap should be... someone can hep me with that I hope.

== mono == 

Where do you get mono? -- unsigned comment by [[User:Jacob|Jacob]].

You can get mono from http://www.mono-project.com/Main_Page --[[User:AnMaster|AnMaster]] 11:47, 8 July 2008 (UTC)

Thanks!
Okay, but there is a bunch of them. The one that has the right stuff is [url=http://ftp.novell.com/pub/mono/archive/]here[/url] so just select the right one for your OS. --[[User:Queser|Queser]] 11:32, 6 October 2010

==  Script Question ==

Can someone find all the actions that can happen in a script.
:This sentence [http://supertux.lethargik.org/wiki/index.php?title=Talk%3AEditor_FAQ&diff=10578&oldid=10577 had] no verb.
:Look at the [[Scripting reference]] pages for the list (or the source code in the src/scripting folder for most-up-to-date) --[[User:Mathnerd314|Mathnerd314]] 01:46, 23 December 2008 (UTC)
:Um, there is a bunch of them... which one? -[Queser]-

== Another scripting question ==

How do you register local variables when a badguy execs "DeadScript"?.And How to use control statements (if,while...)?
:That would be in the [http://squirrel-lang.org/default.aspx#doc Documentation]; also try looking at any of the existing scripts in current levels. 
:Local variables are something like <code>local a</code>, creating variables is <code>a <- 0</code> (the variable will stay around as long as the current sector), and to assign an already-created value is <code>a = 0</code>. (<- also works for assignment, however)
:You can create global (currently lasting over the lifetime of execution) variables by getting the parent of the sector table: <code>::parent.whatever</code>. There is currently no way to create level-persistent or world-persistent variables. --[[User:Mathnerd314|Mathnerd314]] 01:33, 24 December 2008 (UTC)
::No world-persistent variables? Then why do the keys still work? --[[User:Superdev|Superdev]] 08:36, 24 December 2008 (UTC)
:::I used "persistent" to mean that the variable is shared across running instances. The keys are currently execution-persistent, meaning that they stay loaded until you close the game. (Try going to world1 and world2, then to the main screen. You can still do <code>display(state)</code>, the persistent table)
:::The state table is also persistent in that it is saved and reloaded by world.cpp into the saved game data, which is why the keys work. The problem is that currently data is either sector-persistent, which is too short for any cross-sector scripting, or execution-persistent, which is much too long a time. --[[User:Mathnerd314|Mathnerd314]] 16:28, 24 December 2008 (UTC)
:::Miniswig also needs a bit of a rewrite, as Squirrel 2.2 adds true constants to the language (<code>const x = 4; a <- x</code> will compile directly to <code>a <- 4</code>), and templates could eliminate most of miniswig's work, if anyone is interested. (Try looking at create_wrapper.cpp create_*_constant_* code) --[[User:Mathnerd314|Mathnerd314]] 16:28, 24 December 2008 (UTC)
::[http://supertux.lethargik.org/viewvc/viewvc.cgi/trunk/supertux/data/levels/world2/village.stl?view=markup world2/village.stl] looks like it is using level persistent variables. --[[User:Superdev|Superdev]] 14:52, 25 December 2008 (UTC)
::No, those are sector-persistent, since they disappear once you switch sectors. (I assume you mean hint_displayed and bridge_active?) That level illustrates another problem: Tux falls off the screen during cutscenes. (Comment out Camera code and turn on debug_collrects to see) --[[User:Mathnerd314|Mathnerd314]] 01:54, 26 December 2008 (UTC)

== Bug on SuperTux Level Editor crashes while attempting to play the levels that I made ==

I am on Linux Ubuntu 10.04 lucid 32 bit. The supertux level editor is labeled as supertux-editor-svn in the synaptic package manager. I don't know have to do a "Full Backtrace" or the version "Mono, GTK, or GTK#" With further instructions, I would post that info. <small>-- unsigned request by [[User:Aaron]] 01:22, 13 September 2010</small>
        I figured it out.

== Level Editor help!!! ==

I don't have a PC so I can't use the level editor for the new version of ST. Could some one compile a version and send the link to me? (I have a intel mac BTW.)

== Mac Super Tux editor (Intel) ==

I read the post about where to find ST LE for MAc intel but I didn't understand it. please help ASAP!!!

you need to download the things it said, but I can't find them all. Can anyone send us links of where to download all those things? any help is appreciated. I found the website mono, but there is so many things to download there that I got confused.
:If you can't figure out what files you need from the descriptions in the instructions, you're better off waiting until the stable version comes out. SuperTux development is really focused on Linux. -- Qwood [[Special:Contributions/Qwood|(contribs)]] [[User talk:Qwood|(talk)]] 22:24, 4 July 2011 (UTC)

== Editor error ==

When I launch the editor, I select "Tiles" but nothing show up! I went to settings (under editor) and I selected the data file and the actual game, restarted level editor but nothing happened. just blackness.

Windows XP
Editor for 0.3.0

Here's a screenshot of it.

[http://i52.tinypic.com/x36zhk.png http://i52.tinypic.com/x36zhk.png]

HELP!!! PLEASE RESPOND!

What did you set the data folder?
--[[User:Hume|Hume]] 09:45, 23 January 2011 (UTC)

== Missing DLLs ==

Hello, It seems that I'm missing some DLL files for the editor. One of them is GLU.dll. If you could please give me the files, I would really appreciate it. Thanks!
:When I used Windows and I needed a DLL, I went to [[www.dll-files.com]] and downloaded it from there. -- Qwood [[Special:Contributions/Qwood|(contribs)]] [[User talk:Qwood|(talk)]] 03:10, 7 June 2011 (UTC)

== Missing brushes ==

When he looked jesm editor-in help how to use brushes, I found there that I find the brushes in the "trunk / SuperTux-sharp / data / brushes". What nonsense! This folder doesn't exist! Moreover, it will not know the structure of the file, so I do not know what to do! Can I at least know the structure of the document, as I saw it in a text editor, so I could make a brush?
--[[User:Hume|Hume]] 09:48, 23 January 2011 (UTC)
Hmm. Maybe you could search your computer to try to find them? DOwnloading the source of a windows version might help... [[User:Monster|Monster]] 23:43, 8 April 2011 (UTC)

== Breakable blocks ==

I can create everything except breakable blocks. Another thing is, when I have brick blocks(those which you can usually break) nothing happens when I am small tux, but when I am large, money comes out.

Anyone else experienced the same trouble?

cyborgsmurf@hotmail.com
