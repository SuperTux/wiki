There are known bugs in older releases. See [Bugs](Bugs "wikilink") for newer versions.

Website
-------

-   The titlebar of the browser in this wiki shows “Wikipedia” instead of “SuperTux” when logged in.
      
    Can't reproduce that problem. Works fine here. --[WolfgangB](mediawiki/Users/wolfgangb) 00:30, 15 Sep 2006 (BST)

      
    I've sometimes noticed with certain sites that exiting a tab (in Firefox) will not update the titlebar. Right now the CSS on the wiki is messed up for me, but I know it is just me. --[Tuxdev](mediawiki/Users/tuxdev) 00:48, 15 Sep 2006 (BST)

      
    It's still there. I'm using Opera 9 on Ubuntu Dapper

      
    So am I, but I don't experience anything like it. Maybe a custom skin? Can you give steps to reproduce? --[84.146.251.243](mediawiki/Users/84.146.251.243) 14:02, 29 Oct 2006 (CET)

      
    I simply log in, and when logged in every single page has “Wikipedia” instead of “SuperTux”. I am not using any custom skin or such. --Shylence 18:24, 3 Nov 2006 (CET)

      
    Well I see SuperTux when I login. **Nowhere** does it say Wikipedia. Can you please tell where exactly you see Wikipedia on any page? --[AnMaster](mediawiki/Users/anmaster) 20:35, 3 Nov 2006 (CET)

    Probably because you set the Wiki to output non-english content. Wikimedia comes in 86 different languages and SuperTux-specific strings were only added for some of them. The Wiki now forces an english locale for all users until we have localizations for the rest of the supported languages. --[Sommer](mediawiki/Users/sommer) 13:50, 4 Nov 2006 (CET)

      
    I was using Italian language pack, works fine with English one. Sorry for the trouble. --Shylence 17:09, 4 Nov 2006 (CET)

Development version
-------------------

### Closed

-   4426: Console is operational during the main menu, which means you can use 'kill()' to kill Tux; the level fades out and does not fade back in again, resulting in a quiet, black background with the main menu (which still works).
      
    The console is a debugging tool, you can mess up any game using it as you can call any function that you could call using a script. And as normal users would never use the console I don't think that this seems like an important bug. Also having the console reachable from anywhere in the game is good for debugging (and that is what the console is meant for, it isn't for cheating...). --[AnMaster](mediawiki/Users/anmaster) 12:25, 29 Oct 2006 (CET)

    Not a bug.

<!-- -->

-   If you jump through a non-solid block into a solid one, you go through the solid blocks. (This is kind of hard to explain. We need a site where we can post levels to demonstrate bugs...)
      
    You might be experiencing a new feature of ST engine, unisolid tiles. Example level is “Detour”, for the tree branches. --[Tuxdev](mediawiki/Users/tuxdev) 18:11, 20 Dec 2006 (CET)

    I already knew about unisolid tiles. This wasn't a bug in supertux, just a bug in my level - I had put some foreground tiles over unisolid ones thinking they were just plain solid tiles next time I looked at that level.

<!-- -->

-   4328, 0\_3\_x branch: crash when trying to load “Light and Magic”.
      
    Works for me in 4446. Fixed or hard to reproduce?

      
    Fixed, or at least worked around.

<!-- -->

-   4496: Finish World1, solve a wold2 level, Quit game. Load game. Game starts on world1.

<!-- -->

-   4496: get\_light() does not work if resolution is not default

  
fixed in r4541

-   4531: The pushbuttons do not work anymore. (Maybe it was the gravity patch? It worked in r4529)

  
test/pushbutton.stl works as expected with r4555

-   3657: Infoboxes cause “Restarting audio source because of buffer underrun” errors
      
    that's because they do their own eventloop, they really should plug into MainLoop somehow

  
  
Hacked for 0.3.

-   4117: Wind with x speed 0 is really x speed -1 . in order to get tux move vertically, set x-speed to 1 (or fix it ;-D)
      
    Might be related to the problem that sometimes when tux stands still and jumps, he land slightly behind where he stood before.

  
  
Fixed in r4532

-   4249: If you jump on Poison Ivy (green thing on the ground), the leaves fly around. If you walk on the orange thing, it doesn't.

  
  
Different Badguys behave different. Not a bug.

-   4249: In “Tree Fortress” level: sometimes when Zeekling hits first Mr Tree Mr Tree can suddenly appear on wooden border and, of course stuck there. (Quite hard to reproduce)
      
    This is a general problem when badguys stack - it always looks a bit out of place. SuperTux might be better off either letting badguys walk through each other or having badguys get squished when another badguy steps on their head. --[131.188.73.150](mediawiki/Users/131.188.73.150) 14:08, 26 Sep 2006 (BST)

  
  
Badguys squish each other r4435

-   Mac OS X on Intel: dock icon looks wacky. This is an SDL problem; will submit a bug report ASAP.

  
No bug in supertux.

-   4162: Error in drawing of tilemap-to-lightmap on Windows. Doesn't happen on Linux. See [screenshot](images/Lightmap_error_on_Windows.png "wikilink") for details.
      
    4251: A similar thing (but not so ugly) happens on Ubuntu Dapper in world2/light+magic.stl, in the dark area near the end, when walking up/down.

      
    Should be fixed with bigger lightmap in r4443.

      
    This makes that level unplayably slow for me. I think that the lightmap needs to be block-aligned (it'll need to be slightly wider and taller), with appropriate changes to the pixel lookup code.

  
  
Seems to go away with \#define LIGHTMAP\_DIV 5 instead of 4 (light lines) or 1 (too slow on some machines)

### Open

-   3771: Possible to die after winning a level if not invincible (happens in yeti level)

<!-- -->

-   4033: Dart traps sometimes shoot right through walls, instead of hitting them.
      
    Seems to happen when a dart hits near the border between two tiles

<!-- -->

-   4041: Tux gets stuck for a few seconds climbing certain staircases in the level that's automatically played in the background on the main menu.
      
    yes at x 3762 y 256 and x 8288 y 1024, and sometimes other places too.

<!-- -->

-   4107: Editor: Placing a left-switch is difficult, the switch moves to the left in the game compared to the editor.

<!-- -->

-   4107: Enemies may be pushed in the ground by other objects (e.g. in world2/updown.stl, near the beginning, the snail may be pushed underground by the platform if upside-down).

<!-- -->

-   4107: Tux can get stuck in the “roof” of data/levels/world2/level2.stl at x 4160, y 656.001 when the level is flipped. Slopes still doesn't work when level is flipped.

<!-- -->

-   4107: When two slopes of opposite directions of the snow-tileset are connected to eachother on their lower side, when running from right to left it works, from left to right you get stuck.

<!-- -->

-   4236: When there are multiple stalactites in a row, they often disappear instead of falling (e.g. bonus2/level7.stl)

<!-- -->

-   4245: If you switch the camera to manual mode and scroll it so that Tux would be off the screen, Tux actually gets pushed into the water by the left edge of the screen.

<!-- -->

-   4245: Since r4208 Smalltux spawns below the spawnpoint. So reset points are no longer activated if restarting a level there. (activate firefly, kill tux. tux starts at firefly, but firefly shows inactive image)

<!-- -->

-   4249: I found a secret bonus level on the south-west ice island, but when I won it, SuperTux crashed. SVN 23 sept. -- smallfoot-

<!-- -->

-   4251: When Bigtux crushes a wooden box by jumping, enemies on that box do not die, but fall on his head.

<!-- -->

-   4249: Squirrel function wait() counts real seconds, not game seconds - so cutscenes can end up deadly for Tux of time synchronisation doesn't fit. -- [Penguinmaster](mediawiki/Users/penma) 23:42, 30 Sep 2006 (CEST)

<!-- -->

-   4327: Forest worldmap has a level off the path, and says that “tilemap data is buggy” when I get near it.--[DJ Wings](mediawiki/Users/djwings "wikilink")[<sub>Freesyle\ here</sub>](User_talk:Djwings) 15:34, 1 Oct 2006 (CEST)

<!-- -->

-   4437: Only one Mr. Icebox will die, if two are fired at each other. (Different behaviour than in 0.1.3)

<!-- -->

-   4438: Level time stops (and the counter at the top disappears) if you go to another sector.

Release 0.3.0
-------------

### Closed

-   When I quit the same on world 2, and then relaunch it, I am back on world 1.
      
    Fixed in SVN --[Sommer](mediawiki/Users/sommer) 22:21, 2 Jan 2007 (CET)

<!-- -->

-   Don't start: a error occurs because no OpenAL32.dll on my Windows XP SP2.
      
    Download the OpenAL windows installer from www.openal.org/

<!-- -->

-   Doing a backflip while in fire Tux mode causes Tux to lose the fire mode. If this is the intended behavior, it's not documented in the user manual.
      
    Now it is --[Sommer](mediawiki/Users/sommer) 22:21, 2 Jan 2007 (CET)

<!-- -->

-   I've got an Nvidia TNT2 (I'm using legacy drivers version 1.0.7184+2.6.17.6-1 in kubuntu edgy). When I start supertux I get “Fatal: Unexpected exception: Couldn't set video mode (800x600-0bpp): Couldn't find matching GLX visual”.
      
    I don't think that's SuperTux' fault --[Sommer](mediawiki/Users/sommer) 22:21, 2 Jan 2007 (CET)

<!-- -->

-   carrying an ice cube no longer protects Tux from other badguys. Is this an intended change? It was useful in the previous release.
      
    Intended behaviour --[Sommer](mediawiki/Users/sommer) 22:21, 2 Jan 2007 (CET)

<!-- -->

-   Big Tux can't go through places that are only as high as the small Tux. In previous version Big Tux was able to go through that by ducking, in this version Big Tux reverts back to the small Tux.
      
    Intended behaviour --[Sommer](mediawiki/Users/sommer) 22:21, 2 Jan 2007 (CET)

<!-- -->

-   When I cancel a level, Tux gets back on the map to the level I have finished before starting this level. I would prefer that Tux gets to the level I have just canceled.
      
    Fixed --[Sommer](mediawiki/Users/sommer) 23:15, 8 Jan 2007 (CET)

### Open

-   When Tux is standing on an elevator moving down next to a wall, and he walks into the wall, if the wall ends while the elevator is still moving down, Tux will get crushed! I made this level to demonstrate: fast.filespace.org/blublu/crushbug.stl
-   Several sounds are very quiet in the win32 version (noticably the jump sound, crates crashing, coin sounds, yetis gna and probably others). I didn't check with the source yet, but I assume it's all sounds without position. The OpenAL driver on that box is from NVIDIA: Standard OpenAL(TM) Library, NVIDIA Corporation, 5.10.2917.0, English
-   Performance degradation although the computer is able to handle the game. Noticed on a 1.3 GHz box with geforce 2/mx card on win XP: The game often goes down to 40-50fps and gets laggy although cpu usage is only at 30-40%. Seems like that idling code is problematic, don't know why... This also doesn't seem to be win32 specific, I've heard similar reports from Linux people and we got a patch submitted that removes the idling code because of that.
-   Crash every time I try to start the “Tux the builder” level in the Forest area. stderr messages (maybe unrelated): Warning: Couldn't create audio source: Invalid Value
-   The vertical movement of the screen in world 2 is too sensitive. Eg, tux jumps onto a small block and then back down, and the screen moves up and back down with him. This makes me feel a bit seasick at times!
-   Crashes in the 'Short visit' level in world 2: near the shooting arrows sometimes, and near the lava every time. Message on top of the screen about sounds.
-   Only a small Bug, but nevertheless mentionable: If you eat a snowball to become the great Tux and you are immediately killed afterwards (so you have eaten the snowball, but the effect has not yet started to work), you start as great Tux at the beginning of the level.
-   Running the game with the open source ATI graphics driver, there are colored lines shown where tiles meet. This happens in both the world maps and the levels themselves. The closed-source ATI drivers fix this problem, but for those with older ATI hardware, this will look bad.
      
    This also happens to me using the NVIDIA drivers. Either this is a off-by-one error in SuperTux that happens to be negated by a similar bug in the ATI drivers, or is a bug in the open source and NVIDIA drivers that is exposed by SuperTux. --[Tuxdev](mediawiki/Users/tuxdev) 05:46, 27 Dec 2006 (CET)

    This is the graphics card or the drivers doing anti aliasing with the pixels on the edge, although antialiasing shouldn't be needed as the image widths and heights are only whole pixels. We should be able to work around these bugs by producing images with the border pixels doubled (go from 32x32 to 34x34, put the original image into the middle and diplicate the border pixel lines, you can see how this stuff could work in the windstille sources for example)

-   Fall down a pit. Before the death animation happens, press escape and quit to the main menu. When the main menu demo starts playing, Tux will die and the screen fades to black.
-   The crash-when-loading-“Light and Magic” bug noted below for development version 4328 is in 0.3.0.
-   A lot of secret or tactical parts in World 1 levels don't really work or are too easy now that Tux can travel backwards.
-   The background is all messed up on the Mac OSX version.
-   When trying to play a level with Windows version of the editor, it says: “Couldn't start supertux: Object reference not set to an instance of an object”. The same happens when saving.
-   I get a warning that the tilemap data is buggy, when I force Tux to go straight on where the path on the map has a curve.
-   At the end of level I get informations about how much coins (...) I got. But this doesn't seem to work since the information below “Now” and “Record” are the same. Sometimes I don't get these information at all and Tux just gets back to the map.
      
    Level statistics are currently not saved to disk --[Sommer](mediawiki/Users/sommer) 22:21, 2 Jan 2007 (CET)

    Also, no statistics are available when you use a checkpoint after getting killed in a level --[Sommer](mediawiki/Users/sommer) 22:21, 2 Jan 2007 (CET)

      
    Thank you for the explanation, will statistics be added even after using a checkpoint?

-   When a checkpoint is activated this is indicated by an animation. But after Tux got killed and returned to the checkpoint the checkpoint is not animated although it is activated.
-   At certain places in certain levels on my system, everything slows down to 1-2 frames per second, whereas normally the game is very fast and smooth. I have a 1.1 GHz Mac G3. This slowdown happens every time on the 23rd Airborne level. It's slow as Tux is dropping to the ground at the beginning, then once he's on the ground it speeds up to normal. However, once he runs to the right and jumps to the first “mountain”, the game slows back down to 1 or 2 frames/sec. Could my system simply be too slow to play the game?
-   Your new autopackage does not work at all. I double click it but nothing happens. No error message, no supertux installed. I use the latest supertux-0.3.0b.x86.package. The supertux-0.3.0a package at least shows a message that you made a mistake building the package. Please fix this fast, I want to play the new levels.
      
    Did you try manually running the package installer? To do so, open a command line window, change to the directory you downloaded the file supertux-0.3.0b.x86.package to (e.g. “cd ~/Desktop”), then either run “~/.local/bin/package install supertux-0.3.0b.x86.package” or “package install supertux-0.3.0b.x86.package”, depending on where you installed autopackage. --[Sommer](mediawiki/Users/sommer) 23:03, 8 Jan 2007 (CET)

      
    I manually clicked the installer. There is nowhere I have installed the autopackage yet, because it does not work. No error dialog. If I run the package in a terminal it says FAIL:Install the package with the command 'package install' instead. but i don't have a 'package install' command. :-(

Release 0.1.3
-------------

-   When using OpenGL renderer, water transparency is not shown. Using software renderer (SDL), water alpha looks just fine. Could you check out why transparency does not work for some people? Experienced with the binary-only ATI video driver (fglrx) for ATI Radeon X200M video card.
-   If an enemy kills [Tux](Tux "wikilink") and the user elects to abort the level before he falls off the screen, gameplay may continue with negative lives. This happens when Tux looses his last life.
-   The texture.cpp file has an incorrect texture type (GL\_RGB10\_A2). Only ATI (FGLRX) drivers will interpret it correctly and will display a non-transparent waterfall in OpenGL. It's better to use GL\_RGBA here since most drivers (ex. mesa) interpret GL\_RGB10\_A2 as GL\_RGBA
-   Widely experienced bug: After compiling v0.1.3 from source on Ubuntu Linux 5.10 “Breezy Badger”, the game crashes after choosing “Bonus Levels” from the main menu, although going into a 26-level game slot doesn't -djwings
      
    Solved by upgrading to Dapper. --[DJ Wings](mediawiki/Users/djwings "wikilink")[<sub>Freesyle\ here</sub>](User_talk:Djwings) 16:40, 24 Sep 2006 (BST)

-   I was able to walk throug the end of the level without finishing it. It happened while playing witw 12 frames/seconds.
-   The jumping heads with spikes sometimes only jump to the level of a passing cloud.
-   Enter key is completely ignored on a Compaq Pressario, but works fine with other SDL-based games (e.g. Falcon's Eye) (by jessejoe)
      
    Can be worked around by custom-compiling with all SDLK\_RETURN replaced by 271

-   Tux is unable to grab Mr. Iceblock while blinking after losing a bonus (eg. Big Tux -&gt; Small Tux).
-   The Mac OS X version seems to have some transparency problems in OpenGL mode. eg. you can easily see the 'hidden' coins at the end of the first level.
-   supertux doesn't compile with gcc-4.1.1. At line 210 of menu.h the 'Menu::' qualification needs to be removed (it is already a Menu:: member and this is no longer allowed in gcc-4.1.1).
-   Level editor: Object selection tool doesn't work when the last tool used was a badguy; it works fine when following a tile tool. Also, when a badguy's deleted, the property button doesn't gray out; clicking it causes a segment violation/GPF/segfault/crash.
-   Save file gets corrupted (has zero length) when free space on storage device runs out during the game.

### Not a bug

-   After running the configure script without any options and compiling the source in the supertux-0.1.3.tar file, SuperTux crashes with the error 'Couldn't load musicfile', and reports the filename with a complete absolute path (which is correct -- SALCON.mod). Bug produced with a Slackware 9.1 system. -&gt; Your SDL\_mixer library is probably compiled without mikmod support or you grabbed 1 of the versions where mikmod support was broken.
-   Tux can junt to the top and out of the screen when a platform reaches the upper limit. This allowa to bypass certain zones.
      
    Intended behaviour

-   If you have the big Tux, hit a box with a flower and then for some reason you are attacked and reverted to the small Tux, when picking up the flower you'll be big Tux in fire mode.
      
    Intended behaviour

-   Enemies need not to fall down from the platforms. This reduces enemy number.
      
    Eremm... This happens in many Mario games.

    Anyway. Not a bug. If this was a feature request, please add this to the list of [Ideas](Ideas "wikilink")

    Isn't this is a badguy characteristic? Some badguys fall off, others don't. --tuxdev

      
    In [Milestone 1](Milestone_1 "wikilink"), this could be configured separately for each guy on the screen. [Milestone 2](Milestone_2 "wikilink") will have that as a Badguy-dependent setting, i.e. [MrBomb](MrBomb "wikilink") never walk off ledges, [Spiky](Spiky "wikilink") will only walk off if he won't fall offscreen, A [Snowball](Snowball "wikilink") won't care and happily drop off every ledge.

Release 0.1.2
-------------

-   The sound slightly lags. Bug produced with Fedora Core 2.
-   If an enemy kills [Tux](Tux "wikilink") and the user elects to abort the level before he falls off the screen, gameplay may continue with negative lives.
-   When opening hand-edited levels/maps that have incorrect syntax, SuperTux crashes with an unmoveable mouse.
-   SuperTux takes up more memory on each new level/game, until it crashes the systems. Using KDE System Guard suggests that finished maps/levels are not being freed from memory. Bug produced on a Knoppix/Debian system with 128MB of RAM.

<Category:Bugs> [Category:For Users](Category:For_Users "wikilink")
