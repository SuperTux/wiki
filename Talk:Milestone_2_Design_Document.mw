== Single-sprite Tux ==

The single-sprite may look better normally, but in my opinion, the split sprite is more expressive. You can see Tux's arms still carrying stuff while he's ducking, for example. --[[User:Mathnerd314|Mathnerd314]] 00:01, 6 May 2008 (UTC)

== Options are evil ==

You expect the level designer to test them with several screensize and the size of the projected area? Get realistic, I'm glad I find time to create levels at all. 2560x1600? Did you win the jackpot? Keep 800x600 the recommended and tested size where every level has to work. Otherwise we get some levels optimized for one setting and other levels for another one.
:Basically everything is resolution-independent now. Try searching for SCREEN_WIDTH or SCREEN_HEIGHT in the source code - it's all effects and removing off-screen particles. The main thing, when I tested it, was that you have to add a few more bottom and top tiles to the levels so that they fill up the entire screen instead of leaving black bars at the top/bottom. Of course, since all Milestone2 levels are supposed to have some verticalness, that shouldn't be a problem.
:Oh, it's also necessary to completely hide secret areas so users don't get a peek and an unfair advantage. (But hey, they paid for their large screens for a reason...) Don't forget, you're free to make whatever levels you want. It's just that only levels following the guidelines will be accepted. I'd be happy to make levels if you don't. (once I get an editor working...) --[[User:Mathnerd314|Mathnerd314]] 01:27, 11 May 2008 (UTC)
::SOME verticalness? Dude at 1920x1200, that's 60x38 tiles, which is way overkill, three times horizontally and over two times vertically the 20x15 of 640x480 and way more than the minimum viewing area required to plan most jumps. And designing levels for this go beyond just vertical resolution. This causes several enemies to fall off a cliff before the player reaches them, depending on the resolution the enemy will die before the player even sees them. Which can make a level either easier or harder (in the case an enemy is to be used as jumping aid). 
::I think the screen area should be limited to a minimum of 20x15 tiles and a maximum of 30x20, anything else should be downscaled or upscaled from that. If you're worried that owners of large screens will be displeased, stop being lazy and start working on some damn 64x64 tiles.
::Remember on Command & Conquer, originally a 320x240 game, which got turned into 640x480 by simply changing the resolution, giving the players a hard time clicking on those tiny soldiers? Same idea, who wants to play supertux on a huge 1080p screen just to have a tiny tux which can barely jump across 1/5 of that? --[[User:Jack Mcslay|Jack Mcslay]] 20:10, 18 December 2009 (UTC)
::Yeah, but not all resolutions work on all computers. It is not hard to make all reasonable resolutions work.

Just a question: is supertux still alive?  Waited long time for milestone 2

== Supertux's life/game over management ==

On milestone 1, the management of lives is so-so
On the current release of milestone 2 (0.3.1) it's too generous
On the current design document, it is just plain preposterous!!!

Frankly, having no lives and no checkpoints drastically detracts from the "classic" feeling of the game, freedom of level designers (as every large level becomes an undesirably frustrating one, forcing them to reduce the level's size to keep them enjoyable), not to mention it defeats the purpose of having coins (shop for items? hell no, doesn't fit the game at all)

I suggest something like this:
* Extra lives caught on any level can only be used on the same island it was caught on (avoid the player from getting lots of lives on easy levels to make further levels easier)
* Players are awarded an extra life for every 100 coins caught on the same level (Mario 64 style). 
* Coins increase the default ammount of lives for every 1000 caught, this means that on the next game over, the player will have more lives to begin the level than the standard 5
* If finishing a level with fewer lives that the current default, reset the life ammount to the default. Same occurs when aborting a level.
* The total of coins accounted for increasing the standard ammount of lives is the sum of the maximum number of coins the player has caught on all the levels he played (banjo-kazooie style).
* Players do lose lives when dying before a checkpoint, but keeps the coins he had caught on the level before dying
* Players restart the level with all the stuff he had on the start or last checkpoint. That is, if he was a big tux on the last checkpoint, and the timer was at 89, he restarts as a big tux with the timer at 89.
* Reaching a checkpoint on a level, or finishing it, restarts any other level you had reached a checkpoint, and stores the ammount of coins if greater than the previous ammount
--[[User:Jack Mcslay|Jack Mcslay]] 20:10, 18 December 2009 (UTC)
