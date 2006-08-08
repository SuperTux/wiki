==How should timeouts affect the player?==
MS1 behaviour: Kill tux on timeout.

Current r4079 behaviour: Shrink Tux and kill him immediately on timeout.

The timeout should be extended the safe time from shrinking so that annoying time critical levels are somewhat less annoying.  The safe time might be less than normal so that it doesn't fudge it too much.  [[User:Tuxdev|Tuxdev]] 22:48, 24 Jul 2006 (BST)

: Shrinking Tux on timeout seems a little absurd. IMHO shrinking should only happen when Tux is hurt. If we need something to extend Tux' time, maybe after reaching zero on the clock, the game could make Tux lose one coin per second, up to 25 seconds, before killing him. --[[User:Sommer|Sommer]] 23:50, 24 Jul 2006 (BST)
: That is a good option, and shrinking when Tux hasn't actually touched anything does seem a bit absurd, now that you mention it.  25 seconds seems too much of a fudge factor, I propose 5 coins/sec for 5 secs. --[[User:Tuxdev|Tuxdev]] 00:24, 25 Jul 2006 (BST)
::Good idea, with me preferring Tuxdev's option. I also kind of prefer the current timeout idea, except maybe extend or reduce the time to accomodate the level, eg. the "No More Mr. Ice Guy" level was very short, yet it had a time limit of 300, it would've been a good idea to shorten the time limit. --[[User:FlyingPenguins|FlyingPenguins]] 07:43, 25 Jul 2006 (BST)
:::[https://developer.berlios.de/patch/index.php?func=detailpatch&patch_id=1251&group_id=3467 Tuxdev's Patch] gives you up to 5 sec for 5¤/sec. Thus making a level simpler if you are up to 5 sec late. But if you are too slow it will cost you 50¤ instead of 25¤. No idea about side effects if remaining time is < 0. --[[User:WolfgangB|WolfgangB]] 16:17, 8 Aug 2006 (BST)
::::That is the case if you have more than 25 coins.  If you have less, you end up with less fudge time than the full 5 secs.  However, since everybody has pratically infinite lives now, it is almost always the case that the full 5 secs are available. --[[User:Tuxdev|Tuxdev]] 17:11, 8 Aug 2006 (BST)

No Timelimit. At least not in any level on a worldmap. --[[User:Superdev|Superdev]] 23:13, 24 Jul 2006 (BST)

Yes, we want to avoid time limits, but sometimes they are critical to the level.  Example level "Train Leaves in One Minute", or bonus1/abendigo4.  [[User:Tuxdev|Tuxdev]] 23:40, 24 Jul 2006 (BST)
:That was the "straight line with zillions of badguys on it" level? If thats the kind of level you get with timelimit I'd say remove timelimit completely. --[[User:WolfgangB|WolfgangB]] 21:18, 25 Jul 2006 (BST)
::Well, that's because of the lack of vertical scrolling. Also, what about making time optional, just for nostalgic reasons? It could either make the game easier or harder; this would create a sense of balance for players, making everyone happy. --[[User:FlyingPenguins|FlyingPenguins]] 00:30, 26 Jul 2006 (BST)
