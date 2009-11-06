== The trouble with lightmaps ==
Why remove "Levels that use lightmaps"? T
: Because they cause weird bugs on Windows, and even on Linux they don't work perfectly. --[[User:AnMaster|AnMaster]] 08:53, 28 Sep 2006 (CEST)
::They don't work? Which levels are we talking about here? --[[User:WolfgangB|WolfgangB]] 00:53, 29 Sep 2006 (CEST)
:::"Light and Magic" crashes at unpredictable intervals upon entering the level. No time to investigate yet, so it's an optional bonus level for now --[[User:Sommer|Sommer]] 12:48, 14 Nov 2006 (CET)
::::The magic blocks in l&m are planned for ghost forest IIRC. Are they in 1.9 at all? --[[User:WolfgangB|WolfgangB]] 21:59, 14 Dec 2006 (CET)
:::::Light and Magic hasn't crashed for me and I am a windows user. The blocks that are solid when only a correct color lantern is near are great. the ghost rendering is also good.
::::::That level is working perfectly on my Ubuntu. I didn't see any problem.
:::::::Its crashing alot on my MACCCCCC--[[User:Rabbit67890|Rabbit67890]] 01:08, 31 December 2008 (UTC)

==Problems with alpha installer for Windows==
The alpha installer by delta___ doesn't seem to use the tools/innosetup/supertux.iss file. The editor depends on the game using this one to build the installer (as the installer for the editor checks for some ids to make sure supertux is installed). --[[User:AnMaster|AnMaster]] 10:22, 5 Oct 2006 (CEST)

==Entering Small Island on World 2==

There is a small island on the top right corner of world2, how do you enter it?
: It's a secret island that can be reached via a teleporter in [[World 2]]. It wouldn't be a secret island if I told you how to reach it, now would it? Besides, it would spoil all the fun searching for it! --[[User:Sommer|Sommer]] 12:44, 14 Nov 2006 (CET)
:: I don't see a teleporter, is it invisible?
::: Yes, it is hidden behind a tree --[[User:Sommer|Sommer]] 13:32, 16 Nov 2006 (CET)
::::What about the small island in World 1? The teleport there doesn't seem to work. How can I get there?
:::::The teleport works. It's just not where one might suppose it to be --[[User:Sommer|Sommer]] 21:12, 21 Dec 2006 (CET)
I found the teleport on island 2! Also, in bonus island 2, on the secret island that has the level 'End of the Ice Age' there is another path to the right of it. does it lead anywhere and if so please give me a small hint to where the teleporter is.

World 1 hint: if I told you I would be leading you into a dead end.[[User:Atomic1fire|Atomic1fire]] 04:33, 10 Jan 2007 (CET)

Answer: Go to "Trees sheets to the wind" and go left.

==Editor Error==

When you try to open a level or worldmap in the windows 0.3.0 editor, you get an error "Error loading level: Exception has been thrown by the target of an invocation" Any solutions?
: You might be trying to open a SuperTux 0.1.x level. Sadly, the editor cannot import those yet. <br />Converting SuperTux 0.1.x levels to the new 0.3.x format isn't too hard to do (just open an old and a new level in a text editor to see the differences), but I wrote a short Scheme script to do the conversion for you. You can download it at from svn.berlios.de/viewcvs/*checkout*/supertux/branches/supertux/0_3_x/tools/levelconverter-0.1.3_0.2.0.scm?rev=4257<br />Alternatively. mail me the old level and I'll mail back a converted version to you. --[[User:Sommer|Sommer]] 13:37, 16 Nov 2006 (CET)
:: A 0.1 level would not result in that error message. The message would be: "Couldn't load level: Old Level Format not supported". What I suspect is that you haven't set the path to the supertux data directory correctly. But without details I can't say what it is. What is needed is: the message shown after clicking on the small "+" in front of the text "Details" in the error message box and the level level file itself. --[[User:AnMaster|AnMaster]] 13:53, 16 Nov 2006 (CET)

Here is the info:
<pre>
"Exception has been thrown by the target of an invocation."
in <0x0010e> System.Reflection.MonoCMethod:Invoke (System.Object obj, BindingFlags invokeAttr, 
    System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture)
in <0x0001c> System.Reflection.MonoCMethod:Invoke (BindingFlags invokeAttr, System.Reflection.Binder binder,
    System.Object[] parameters, System.Globalization.CultureInfo culture)
in <0x00035> System.Reflection.ConstructorInfo:Invoke (System.Object[] parameters)
in <0x00043> LispReader.LispRootSerializer:CreateObject (System.Type Type)
in <0x000ca> LispReader.LispRootSerializer:Read (Lisp.List list)
in <0x0002d> LispReader.LispSerializer:ReadType (System.Type type, Lisp.List list)
in <0x000ff> LispReader.LispSerializer:Read (System.IO.TextReader Reader, System.String Source)
in <0x00042> LispReader.LispSerializer:Read (System.String FileName)
in <0x00032> Application:Load (System.String fileName)

--Caused by--
"Couldn't load resource 'images/tiles.strf'"
in <0x000b2> Resources.DefaultResourceManager:Get (System.String ResourcePath)
in <0x00015> Util:Load (System.String Filename, System.String RootElement)
in <0x00113> Tileset:.ctor (System.String Resourcepath)
in <0x0003e> Level:.ctor ()
in <0x00000> <unknown method>
in (wrapper managed-to-native) System.Reflection.MonoCMethod:InternalInvoke (object,object[])
in <0x0008d> System.Reflection.MonoCMethod:Invoke (System.Object obj, BindingFlags invokeAttr, 
    System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture)

--Caused by--
"Directory 'E:\Program Files\Super-Tux0.3.x\/images' not found."
in <0x00211> System.IO.StreamReader:.ctor (System.String path, System.Text.Encoding encoding,
    Boolean detect_encoding_from_bytemarks, Int32 buffer_size)
in <0x00026> System.IO.StreamReader:.ctor (System.String path)
in (wrapper remoting-invoke-with-check) System.IO.StreamReader:.ctor (string)
in <0x0003e> Resources.DefaultResourceManager:Get (System.String ResourcePath)
</pre>

:"Directory 'E:\Program Files\Super-Tux0.3.x\/images' not found." is the problem. Please set the path to the SuperTux data dir in the editor preferences correctly. It should be "E:\Program Files\Super-Tux0.3.x\data" (if you have SuperTux 0.3 in E:\Program Files\Super-Tux0.3.x). --[[User:AnMaster|AnMaster]] 22:28, 17 Nov 2006 (CET)

I got another error:-(

<pre>
"Exception has been thrown by the target of an invocation."
in <0x0010e> System.Reflection.MonoMethod:Invoke (System.Object obj, BindingFlags invokeAttr, System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture)
in <0x000c0> System.Reflection.MonoProperty:SetValue (System.Object obj, System.Object value, BindingFlags invokeAttr, System.Reflection.Binder binder, System.Object[] index, System.Globalization.CultureInfo culture)
in <0x0001d> System.Reflection.PropertyInfo:SetValue (System.Object obj, System.Object value, System.Object[] index)
in <0x00019> LispReader.FieldOrProperty+Property:SetValue (System.Object Object, System.Object value)
in <0x0028d> LispReader.LispRootSerializer:Read (Lisp.List list)
in <0x0002d> LispReader.LispSerializer:ReadType (System.Type type, Lisp.List list)
in <0x00010> LispReader.LispSerializer:Read (Lisp.List List)
in <0x00141> Sector:CustomLispRead (Lisp.Properties props)
in <0x00b73> LispReader.LispRootSerializer:Read (Lisp.List list)
in <0x007e2> LispReader.LispRootSerializer:Read (Lisp.List list)
in <0x0002d> LispReader.LispSerializer:ReadType (System.Type type, Lisp.List list)
in <0x000ff> LispReader.LispSerializer:Read (System.IO.TextReader Reader, System.String Source)
in <0x00042> LispReader.LispSerializer:Read (System.String FileName)
in <0x00032> Application:Load (System.String fileName)

--Caused by--
"GLU.dll"
in (wrapper managed-to-native) OpenGlUtil.glu:_ErrorString (uint)
in <0x0000d> OpenGlUtil.glu:ErrorString (UInt32 error)
in <0x00090> Drawing.GlUtil:Assert (System.String message)
in <0x0007f> Drawing.Texture:SetTextureParams ()
in <0x000da> Drawing.Texture:CreateFromSurface (IntPtr surfacep, UInt32 glformat)
</pre>
: What did you do to get that one and what graphic card do you use? All I can say from that message is that it is OpenGL related and that it happened somewhere in code outside the SuperTux code itself (in the system file "GLU.dll"). Even with the info of what you did to make it happen, it would probably be quite hard to debug that one. --[[User:AnMaster|AnMaster]] 09:42, 18 Nov 2006 (CET)

I have been expriencing 410 errors for the last 6 weeks. Was anything up with the site? Anyways, I have a Trident Cyberblade XP Ai1 video card and I got this error by trying to open a level.

If you say the problem is GL related, is there an editor that uses SDL?

Doesn't Matter - just install the NEWEST version of mono.

== Release Date ==

We should release Milestone 1.9 soon. Best case this or next weekend, but at least before Xmas, then we can work on MS2 during the holidays and fix the newly reported problems.
: Been there, done that --[[User:Sommer|Sommer]] 01:11, 18 Dec 2006 (CET)

== Mac Binary ==

I'm not too sure on all the details and workings of Mac OS X app bundles, but I think I may have a semi-working binary.  I'll have to give it a test on another system to make sure 3rd party deps don't need to be installed with the binary.  Also need to make it a UB as right now it's compiled for Intel only.  If anyone has any more experience with this, please let me know (msg jayson or EvilGlowingApple in #supertux).  I'll post back when i have a fully working version.
--[[User:EvilGlowingApple|EvilGlowingApple]] 02:44, 18 Dec 2006 (CET)

==Difference between green and orange poison ivy==

What is the difference beetween the green and the orange poison ivys? Infact, they look more like Venus Fly traps.

: The green poison ivy will happily walk off any ledge, even if this means certain death. The orange poison ivy is somewhat smarter: It will never drop from ledges. By the way: SuperTux 0.3.0 also knows a third type of ledge behaviour which is still smarter. Some badguys, like Mr. Iceblock, will only drop off ledges if they do not fall offscreen. Also, badguys in SuperTux 0.3.0 always behave the same; it's no longer up to the level author to define whether badguys should stay on platforms --[[User:217.231.215.83|217.231.215.83]] 07:30, 7 Jan 2007 (CET)

Thanks!

See [[Poison Ivy]] and [[WalkingLeaf]].

== Recent BerliOS Outages ==

The people of BerliOS have managed to get a statement online regarding the recent Server outages:  https://developer.berlios.de/bugs/?func=detailbug&bug_id=9846&group_id=1

==Secret area in level "A mouldy grotto"==

I got a peek at a secret area in AMG but I can't seem to find the entrance?

Start at the beginning. Fall down the first waterfall. Continue towards the right. Go up the sliding bar. There you will see 4 "?" boxes with a bomb on top.  Stand on the 4 boxes and jump into the wall on the right!

== We're Stuck!! ==

First of all, thank you so much to the open source developers who have contributed so much to this project. We love milestone 1.9.  We were motivated to look for it first when we first completed "Nolok's Castle" and then couldn't build or install it because of an uncompatable GLIBC.
Just this past weekend we went looking again due to persistent crashes of the previous version on
our Windoze based laptop and to our suprise discovered the 0.3.0 windoze binaries (that worked great upon subsequently discovering openAL32.dll at DLLsRUS (??).  Still awaiting binaries for SUSE 9.2 and 10.0 x64, as I'm not going to mess with my GLIBC any time soon.

I have several questions directly related to playing the game.  First, we can't go back to levels that we have already won. Is this intended behavior? Second, with that in mind, and given the layout of the new first world, we have become stuck at "under the stars" after completing it and its adjacent neighbors via a circuitous route. Is this intended behavior?

:Installing a dll from somewhere on the internet is usual a good way to have to install windows from scratch fast. Get the installer from http://openal.org/downloads.html. Whats wrong with the autopackage, any error message? It is possible to go back to finished Levels. Did you use the 'up' key? Or did you map 'jump' there? See controler configuration and use whatever you mapped to 'up'.That should work.

::First of all, many thanks for a quick and informative reply! We did resolve the navigation difficulties...I had remapped the cursor keys to conform with the milestone 1 standard, assigning 'up' to the spacebar. Sure enough, using all the keys to navigate resolves all difficulties.  Regarding the mystery DLL advice...you were right...we started havinga  trouble with the sound this evening. Luckilly, it was just a clean program crash back into the normally functioning windows OS without any obvious residual damage. I went DLL hunting again and found links to 'find and resolve windows registry errors' ... loaded it...found 108...'lite version fixes a maximum of 15...fix all by purchasing the full version...

::The reason that we went looking for a mystery DLL in the first place is because the link for the windows installer at creative labs (your recommendation and our original first attempt) is frozen...it was frozen last weekend and still is this evening. Do I have to register as a developer at creative labs to get the windows installer? Do you have any insight on that?

:: For me, the OpenAL 1.9.9 download just never starts. You could try downloading it from one of several mirrors on the net, e.g. from [http://www.planetnvidia.com/downloads/drivers/creative/openal/oalinst.exe], [http://www.tweaksrus.com/index.php?option=com_docman&task=doc_download&gid=804&Itemid=1] and [http://www.top10-racing.org/index.php?file=Download&nuked_nude=index&op=do_dl&dl_id=50]. No idea if they're trustworthy, though. --[[User:Sommer|Sommer]] 17:30, 23 January 2007 (UTC)

::: I turned off the sounds/music and then, after my son tried several times, I played "via nostalgia" until waayy:00 am...finally mastering it. Then, I was bound and determined to resolve the openAL thing before shutting down and going to sleep. Finally, having seen a reference to opensource.creative.com was able to obtain openAL10SDK.exe (windows installer) via anonymous ftp. Its in the 'pub' directory. Thanks to all who commented --[[User:Izmirlig|Izmirlig]] 17:51, 23 January 2007 (UTC)

For some reaon on my Windows i can't even install version 0.3.0 because it says it can't find a "OpenAL32.dll" What's going on ?

http://opensource.creative.com/pipermail/openal/2007-January/010151.html

:Maybe you don't have OpenAL on your machine? Go to http://openal.org/downloads.html get the "OpenAL Installer for Windows" and install OpenAL. Why do you think that hint is right next to the download link?

== SuperTux Live! ==

Development has (re)started on [[User:Djwings/SuperTux Live!]], a project that tries to make a Linux-based Live CD for running SuperTux Milestone 1.9. See the project page (under construction ATM) for more details. --[[User:Djwings|DJ Wings]][[User_talk:Djwings|<sub>Freesyle here</sub>]] 18:06, 2 April 2007 (UTC)

== Feedback ==

Some points I noticed while watching my little sister playing:

* We should provide some way to make up-key for jumping still work nicely... She was really used to the 0.1.3 default keymappings...
* Some last minute changes in badguy behaviour made some iceworld levels incredibly hard! Tweak the levels again
* Enable cheat console by default... One of the first things she asked me was about cheats (because she died 10 times in a row or so in a level)
* She missed the editor
* It was not clear to her that she had to download OpenAL separately
* She liked the new music
* She liked that she could go backward now
* She liked that the game is german

----

Well I don't know if this is the place for posting comments, but let's go. These are things which I noticed when playing with version 0.3.0
* '''plus'''
** the linux installer worked just fine
** Tux riding on a boat is a good idea &amp; other gadgets
** the new woodworld is cool!
** it's also in German
** OpenGL mode gives new possibilities
* '''minus'''
** Linux SiS users have no OpenGL at all! ''Keep old (sdl) engine please''!
** OpenGL textures and fonts are displayed incorrectly with nvidia drivers (Ti4200)
** I almost get seasick whith the new scrolling mode. ''Please'' create at least an alternative scrolling mode where Tux is always a bit under the center (let's say at (400,200)) until he reaches the edge of a level. "Peek Left" &amp; "Peek Right" should be toggle.
** had to swap space and up-key in key settings to play it properly
** Would be nice if Mr Icecube does not get killed if he lets explode a bomb. Now you cannot sweep everything away with only one Mr Icecube (which was fun with 0.1.3).
[[User:87.160.233.231|87.160.233.231]] 12:17, 8 April 2007 (UTC)

== More Feedback ==

#Somebody already said this. The view makes me seasick too. I would love it if the view would just keep Tux in the center. Or scroll the view when Tux gets within a few hundred pixels of the edge.
#Only 25 coins as a penalty on death is way too easy. Remember, it's 4x as easy as in Milestone 1, when 100 coins were worth a life.
#Is there really a good reason for up and jump to be seperate keys? I like to use the up cursor key both as a jump key and to get around in the maps. If there must be an "up" key that is seperate from the "jump" key, then make the cursor keys control the map no matter what the game controls are. This drove me crazy when I set my jump key to 'up' and up/climb key to 'space' and found I couldn't get around the map.
#The bell needs a sound.
#Why does Mr. Icecube do different things depending on exactly how he's hit? The Milestone 1 behavior made a lot of sense: first jump freezes the ice cube, second jump makes it slide. Milestone 2 seems to sometimes skip the "stun" phase and go straight to sliding if Tux hits just wrong.



== how come there's no editor for mac? ==

I see a editor for others but none for mac PLAESE HELP!
:The binary should work on Mac if you have mono or another .NET environment. If that does not work, how about installing Linux?  --[[User:Superdev|Superdev]] 01:01, 19 October 2009 (UTC)
::This is currently being discussed in the bug tracker: http://supertux.lethargik.org/bugs/view.php?id=88 (work seems to be progressing slowly) --[[User:Mathnerd314|Mathnerd314]] 03:52, 19 October 2009 (UTC)

== ==

Other than that, Milestone 2 looks great and I can't wait to get to the forest levels.

: I agree with 2 and 3, but I'm not saying I disagree with the rest. --[[User:Djwings|DJ Wings]][[User_talk:Djwings|<sub>Freesyle here</sub>]]: N0 PH33R 19:28, 13 June 2007 (UTC)

: I agree with 2 and 3, even though for 3 I don't think merging them is a good solution but jump should be up, I have modified my local supertux source (in a hackish way) to make this work correctly on worldmap. Still no good way for climb though. I ''strongly'' disagree with 1. --[[User:AnMaster|AnMaster]] 19:52, 13 June 2007 (UTC)

What if there was possible to switch view easy (between centered and how it`s now) by a command or something? Or maybe it would be too much work to have 2 different views inplemented. Just an idea. --[[User:Arthur|Arthur]] 20:34, 13 June 2007 (UTC)

In SVN you can use camera.cfg hidden somewhere in the data dir iirc. NOTE: It is only your own fault if you mess up by changing it. --[[User:AnMaster|AnMaster]] 20:46, 13 June 2007 (UTC)
: Translation: Hack away, but make a backup first. --[[User:Djwings|DJ Wings]][[User_talk:Djwings|<sub>Freesyle here</sub>]]: N0 PH33R 12:59, 17 June 2007 (UTC)

== Impossible Level! ==

On forest world level 2, there is an impossible-to-jump wall!!!! Does anyone know how to get over it?

Take the spring, carry it near the wall. Jump on it.

:Is it that level? [[SuperTux_FAQ/Spoilers#Bouncy_Coils]]
