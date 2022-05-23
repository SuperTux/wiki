[[Template:Attention|s=Please use the [http://supertux.lethargik.org/wiki/index.php?title=Talk:TODO&action=edit&section=new Edit+] button to add content]]

== Jam uninstall ==

A "jam uninstall" target seems unnecessary to me. You can easily install in a separate prefix folder or use something like [http://relink.sourceforge.net/ relink]. - [[User:MatzeB|MatzeB]]
:Be it as it may, we need *some* way of uninstalling SuperTux once it's installed. How many times did I meet a package that didn't have an uninstall target? Too often for my taste... <nowiki>~~</nowiki>[[User:RavuAlHemio|Ravu]] 19:38, 11 Oct 2005 (BST)

::There is stow, relink, checkinstall, --prefix, DESTDIR, dpkg, rpm and probally a bunch of other ways to manage clean uninstalls, 'jam uninstall' or a 'make uninstall' is completly unnecessary and simply extremly bad design in my eyes. As you said yourself, 'uninstall' isn't something that you can depend upon, because its hardly ever working correctly, people should just learn to get used checkinstall and friends if they want to have a clean uninstall. -- [[User:Grumbel|Grumbel]] 20:20, 11 Oct 2005 (BST)

== this_file.cpp vs ThisFile.cpp ==

this_file.* vs ThisFile.* has the strong advantage that it works portably, if you go with ThisFile instead its just a matter of copying a few times between Windows and Linux to get a broken source tree since many filesystems out there don't preserve case very well. I am also strongly in favour of .hpp instead of .h, since the second one requires annoying guess work to figure out the correct file type, while the other one simply says it streight away. It makes 'find -name "*.?pp" also a lot easier to type. Anway, source is already organized that way. -- [[User:Grumbel|Grumbel]] 20:28, 11 Oct 2005 (BST)
: In fact SVN takes care of it, you never copy directly between the systems, you allways check out/commit to svn. There are other reasons to do that and one is svn:eol-style = native. --[[User:AnMaster|AnMaster]] 00:28, 30 Jul 2006 (BST)

== Spelling error ==

geysir is spelled geyser in English

== Only developers should edit this page. ==

If we really want to enforce this, make sure all devs have admin rights and change page to protected.

== Outdated ==

Some of the content here is outdated... Tux sprites have been replaced, test levels have been somewhat cleaned up, Mr. Ice Block has been repainted, coins fade out, ?-blocks tilt, lisp readers have been fixed, worldmap teleporters can pan, peeking works, and the menu has been improved. When will this page be updated? --[[User:Mathnerd314|Mathnerd314]] 23:11, 2 March 2008 (UTC)

== Wiimote support  ==

Today (6 April 2008) on #supertux:

<pre>
<jonaskoelker> Hi all.  I'm trying to play supertux with my wiimote and nunchuk (using wminput); supertux says no joysticks found.  Anyone got a clue?
<jonaskoelker> (not me :D)
<jonaskoelker> I'm thinking I should poke around /dev, maybe do the magic mknod dance...?
<leftStanding> jonaskoelker: we were just talking about the wiimote
<leftStanding> no development has started yet, but if you are using cwiid along with wminput you may be able to get it to map the buttons
<jonaskoelker> yeah yeah, the buttons work fine with wminput
<leftStanding> ok, so you are able to play the game?
<jonaskoelker> Yeah, perfectly.  But not with the nunchuk joystick :\
<jonaskoelker> I like holding it sideways, left thumb for D-pad and right thumb for 1 and 2
<jonaskoelker> ... though I pretend they're labeled A and B :D
<leftStanding> yep, the joystick option refers to traditional computer joysticks detected through SDL
<leftStanding> really wminput is trapping wiimote data and impersonating the mouse and keyboard
<jonaskoelker> > wminput is an Linux event, mouse, and *joystick* driver for the wiimote
<jonaskoelker> emphasis added
<jonaskoelker> I think it should be able to be made to work
<leftStanding> for sure
<jonaskoelker> you.clue != NULL?
<leftStanding> invalid syntax
<jonaskoelker> ^_^
<jonaskoelker> you have a clue as for how?
<leftStanding> oh, i'll mess around with it for a few minutes
<leftStanding> wminput mentions a configuration file which may allow you to remap how things are
<jonaskoelker> meanwhile, I'll install xserver-xorg-input-joystick :)
<jonaskoelker> I think I got wminput down
<leftStanding> yeah, getting the nunchuk to work through the supertux options menu is out of the question
<jonaskoelker> jstest responds fine to the nunchuk on /dev/input/js0
<leftStanding> i can get the directional buttons to work using wminput
<leftStanding> how did you map the other buttons to controls in the game?
<jonaskoelker> I'll show you my ".wminputrc"
<leftStanding> pastebin
<jonaskoelker> http://rafb.net/p/HFdOto41.html
<jonaskoelker> of course pastebin :)
<leftStanding> ha, do you use dvorak?
<jonaskoelker> yeah
<jonaskoelker> oh, and I map caps lock to escape
<jonaskoelker> in that way, the home button gives the "supertux home menu" :)
<leftStanding> cool i use dvorak too
<jonaskoelker> neat
<jonaskoelker> come join us in #dvorak :)
<leftStanding> how did you get the configuration file to load?
<leftStanding> i've tried it as the usual .wminputrc and also -c .wminputrc but the latter complains the file doesn't exist
<leftStanding> what version of wminput do you have?
<jonaskoelker> 0.6.00
<jonaskoelker> it's ~/.cwiid/wminput/name-of-dash-c-argument
<jonaskoelker> leftStanding: strace told me :)
<jonaskoelker> have you played around with joysticks before?  Do I need xserver-xorg-input-joystick in order to use it?
<jonaskoelker> This doesn't seem likely: jstest worked fine without it
<leftStanding> its more a question of how SDL supports joysticks
<jonaskoelker> do you know, when I put my wiimote in discoverable mode and only n < 4 LEDs blink, is that indicating the power level?
<leftStanding> i don't know, i've only used the controller a handful of times with my laptop
<leftStanding> i don't own a wii
<jonaskoelker> :)
<jonaskoelker> (well, I've only seen n < 4 LEDs blink with my PC, so it's not a wii question)
<leftStanding> hmm its hard to justify coding wiimote support into supertux if wminput handles it for you
<leftStanding> i should have looked into configuring wminput more before beginning the code
<jonaskoelker> leftStanding: agreed.  Except maybe rumble?
<leftStanding> rumble would be cool for any damage tux takes
<jonaskoelker> it would
<jonaskoelker> heh, patch idea for wminput: on sigusr1, starts rumble; on sigusr2, stops rumble
<jonaskoelker> :)
<jonaskoelker> then supertux can kill(2) it
<leftStanding> ha keep on toggling the signals back and forth
<leftStanding> supertux then needs to have knowledge of wminput and if its there/not there. it may warrant adding wiimote support -> go to options ->setup wiimote {detect wiimotes, configure buttons}
<jonaskoelker> supertux could fork off a wminput instance?
<leftStanding> that could work too
<leftStanding> these are all design questions and would love for a supertux developer to join in the discussion
<leftStanding> *hint hint*
</pre>
