Greetings, I am LMH.  Since I was five-years-old and got my hands on my first NES I've had an interest in designing my own levels for 2D side-scrollers.  Back then it was magic marker on discarded continuous feed paper for recently out-dated dot matrix printers.  Later I deciphered the format of level files for a Mario clone on my TI-89 calculator, which kept me entertained in my less interesting high school lectures (unfortunately those levels are likely lost to time).  When I discovered SuperTux, I was made immediately nostalgic for the simple yet entertaining gaming style of my youth.  When I found out there was an editor, I just had to make my own levels.  I couldn't get the editor working at first, but that's nothing a sophisticated system of spreadsheets can't fix.  As I made more levels, I learned more about how SuperTux works and am now able to make modest contributions to the project.  Below are some of the projects I'm currently working on.

==Add-ons Management==

I intend to devote a consistent effort in maintaining the [[Add-ons]] downloadable through the in-game add-on manager (now stored on [https://code.google.com/p/supertux/source/list?repo=addons google code]).  This is the natural evolution of the add-on collection I maintained while the in-game list was difficult to change.  That collection still exists [http://www.mediafire.com/?k47v61nz6i230 here], which serves as an archive for older versions of SuperTux.  I will also try to maintain one add-on to rule them all, that is all add-ons combined in one for easy activation.  This will need to be manually installed since it is a very large file and I do not think it is appropriate to lag up the game with its download through the in-game add-on manager.

==LMH's Development TODO List==

I've decided to keep a list of all the things I'd like to do (or seen done) in SuperTux.  Instead of randomly throwing these into one of the many existing TODO lists, I've instead elected to keep my personal agenda here to emphasize that these are my own thoughts of what the game could use or needs (thus highly likely to be incomplete or outright inaccurate).  There is no particular order to this list.  Aside from some of the coding and just about all of the sound, these are all things within my ability.  Nevertheless help is more than welcomed :)  

===Coding and Bug Fixes===
====Important/Useful Tasks for Next Milestone====
* Loading/downloading messages for processes that can lag
* Fade in/out on sector change
* Screen resolution/full screen toggle graphics issues
* Make iceflower more functional- pickup/stand on frozen enemies, unfreeze timer, update vulnerabilities, have a default frozen graphic, indication that unfreeze is about to happen, freeze/unfreeze audible cues
* Tux jitter when running up a slope and into a wall
* Camera reset after unpause (try peeking and then pausing)
* Reset worldmap with ability to preserve stats or not
* Work on ungrab behavior for bomb (should be able to be tossed)
* Release images so the terminal doesn't fill up on close
* Reset powerups/coins on "Abort Level"
* Translatable script messages
* Let brick shatter in appropriate directions
* Figure out why Tux sometimes dies in the menu (appropriately end menu.stl before loading a worlmap?)
* Editor support for custom bonus block content, try to mimic dispenser objects?
* Moving tilemaps do not behave the same as platforms, figure out collision physics and fix
* Are the random (position, direction) badguy definitions for old dispenser behavior?  If so they could be removed (some are needed for snowman/mrtree so be careful)
* Tweak or remove some of the voc music
====Other Potentially Useful Coding Ideas====
* Replace backflip sprites with actual rotation
* Dependent add-ons ability, might be useful for custom tilesets
* Ability to download updates for languages
* Put together a smart spiky/unify spiky and sspiky behavior
* Sprite replacement ability e.g. Tux -> Penny/Penny -> Tux for "Play as Penny" (also useful for add-ons)
* Slope behavior needs improvement, perhaps allow Tux to slide
* Standardize grab/ungrab by moving behavior from rock to portable?
* Multiple tilemapping support, perhaps by sector or tilemap instead of level
* Improve how water works
:Swimming like a forced climbing (but fast- Tux is a penguin), think frog suit but controllable
:Bring back splash sound for entering
:extinguish things made of fire (bullet/badguy/etc)
:water badguys
* Optional ability to respawn unstable tile after a set duration
* Generalize badguy behavior - combine with sprite files for highly customized badguys/simpler editor implementation
* Highly customizable mini-boss that can utilize different behaviors/sprites/vulnerabilities
* Level flip sound

===Graphics===
* Frozen enemies
* Improve fish
:it also looks weird when fish disappears in transparent water
:start of the jump should depend on top of water- i.e. be dynamic for moving water tiles
* Animated explosion with particles (pop for short_fuse)
* A finished owl
:Can owl drop bombs? have to check, could then make skydive splat
:Owl could probably drop game objects if this is not already set up
:The editor will need to support owl objects
* Consolidate/cleanup/organize image files and tilesets
* Find a way to make the menu border work
* A waterfall to match the new water look
* Fix tiling issues
:crystal cave tiles
:brown castle tiles
:some blue castle tiles
:ice mountain
:arcticskies background (not tiling, but a line artifact)
* Fill out some of the new tilesets or remove (e.g. blue mtn.)
* Separate out some tilesets (ice/forest/castle/etc.)
* Animate some badguy deaths
* LiveFire final sprite
* Alternative candle sprites (animated background torches, glowing crystals, maybe a brazier/open flame, maybe a light bulb)
* Need parallax versions of backgrounds
* Visual effects for willowisp warp and level flip
* Fix Tux graphics ugliness (floating debris outside of Tux and transparent holes inside)
* Replace airarrow with one that is both visible and isn't confusing (maybe a glowing sprite w/o Tux)
* General icons for jump and action buttons, can be used on billboards and in keybinding menu
:the backflip billboard doesn't work if "jump with up" is not selected

===Regular Level Design===
* Tweak castle and bonus on Icy Island
* Work on Incubator Island -> Icy Island
* Levels to show off glow effects
* A shop to spend coins

===Editor===
Where to begin...  let's just say that the editor needs some work

===Documentation and Distribution===
* Guide to GIT
* Update/consolodate TODO lists
* Remove/replace SVN wiki references
* Building references should be revisited
* Would a ST+editor virtual machine be worthwhile? it would avoid Windows/OS X building falderal
* Put together a how-to for custom graphics (sprites, tilesets), maybe combine/enhance with add-ons
* Start updating "what's new" in-situ so next release we know what to say
* Update credits appropriately

==Mattie's World==

Mattie's World is the collection of all the levels I've developed.  It will be a work in progress so long as I'm making levels.  Although designing levels is my primary interest, it should be fairly evident that I'm easily distracted.  My current plan is to have three worldmaps.

===Mattie's Iceberg===

The original set of levels made for SuperTux and available as an in-game [[add-on]], Mattie's Iceberg is the first worldmap.  Although it has changed considerably over the years, it is likely in it's final state and was made for the SVN version of SuperTux (requiring only compatibility tweaks as SuperTux is further developed).  Set near Antarctica, levels are primarily ice-themed.  The story is that the iceberg has been overrun by the minions of the DOOM Toad who resides in the end castle.

===DOOM Islands===

The rest of the ice-themed levels that I make are expected to live in the worldmap DOOM Islands which is currently under construction.  These frozen islands are to the north of Antarctica, and the stronghold of the DOOM Toad.  There will be more flexibility in path for this worldmap, and my intention is to have a second optional storyline culminating with a unique boss fight.  The main idea is to take out the Toad on his home turf.  Ideally these levels will be optimized for Milestone II.

===Peninsula Inland===

The final worldmap is meant to be a for forest levels and is only in the concept phase.  The general idea is that Tux reaches a peninsula where the DOOM Toad had a new and powerful ally.  There is no ETA on this portion of the project.
