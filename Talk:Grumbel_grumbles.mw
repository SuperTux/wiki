== Some comments ==

Why is hitbox in .sprite called 'hitbox', when all I want is affect the offset/hotspot of the sprite and why should I supply a width/height parameters when I don't need them? hitbox and offset should really be two seperate concepts in a .sprite file.

: It's one and the same concept engine-wise. A sprite's anchor point is always the top left corner of its hitbox. Aligning sprites is impossible without knowing the logical width and height of a sprite, so these are also always needed. Using the physical width when an offset is applied leads to undesired alignment.

:: hitbox and align are concepts that should be seperate, since there isn't a hard connection between look and collision, they happen to be the same from time to time, but often enough not, beside:<br /><br />(align center 0 0)<br />(align bottom-center 0 0)<br />(align top-left 0 0)<br /><br />'''much''' more readable and typeable then hitbox<br />--[[User:Grumbel|Grumbel]] 04:52, 8 Jul 2006 (BST)

::: For 99% of the sprites, there is a hard connection between looks and collision: A hitbox defines an imaginary rectangle within which a sprite will be considered "solid" by the engine. If this rectangle is too big, the sprite will float in the air. If it is too small, the sprite will appear to be stuck in the ground. --[[User:Sommer|Sommer]] 21:39, 8 Jul 2006 (BST)

If stuff kills Tux it would actually be usefull if it looks deadly, which most stuff simply doesn't (I mean you spike tiles...).

: I think the spikes fit the cartoonish look of the game perfectly. There's meaner-looking versions in the trunk, even gory versions, but they just don't fit.

:: a) the current spike is super ugly and primitve -> doesn't fit<br />b) blood/rust from the other spike could be removed, fits much better<br /> --[[User:Grumbel|Grumbel]] 04:52, 8 Jul 2006 (BST)

::: Agreed. Although between the current version and the gory one, I consider the former the lesser evil.<br /> --[[User:Sommer|Sommer]] 21:39, 8 Jul 2006 (BST)

Difficulty, some of the current SuperTux levels that Ikaruga look like a game for kiddies... there really needs to be done *A LOT* to make SuperTux playable again. It would be nice to put a bit of fun back into SuperTux, currently its a frustrating mess.

: Making hard levels easier is simply a matter of widening platforms and removing badguys; making easy levels harder is much more difficult. So most of the levels in the trunk are harder than they have to be.

:: Might be true, but just removing badguys can also wreak havok to a level (christoph4), since it will leave some parts that depended on badguys rather useless, its best to design levels from the start for a certain difficulty<br /> --[[User:Grumbel|Grumbel]] 04:52, 8 Jul 2006 (BST)

::: There are indeed some levels that cannot be adjusted in this way, e.g. "The Castle of Nolok": Take out the flames and not much remains. I'd count christoph4 to those levels. It is more of a techdemo than a playable level.<br /> --[[User:Sommer|Sommer]] 21:41, 8 Jul 2006 (BST)

Is there a way to load a sprite without having a sprite file? If not, why not? Writing the same boring sprite syntax over and over again is both error prone and relativly useless.

: Using a plain picture and guessing a sprite's properties might be OK for a few sprites, but most really need the extra information.

:: The extra information is something that should be addable in a later development process, being force to supply info right from the start is annoying<br /> --[[User:Grumbel|Grumbel]] 04:52, 8 Jul 2006 (BST)


This page sound like Supertux sucks big time.

: Heard of [http://en.wikipedia.org/wiki/Constructive_criticism "constructive criticism"]? Need a link? "In collaborative work, this kind of criticism is often a valuable tool in raising and maintaining performance standards." Hmm... --[[User:Djwings|DJ Wings]][[User_talk:Djwings|<sub>Freesyle here</sub>]] 16:20, 16 January 2007 (PST)

== filenames full of spaces ==

You could just bename the files if you don't like the spaces. But no, you just grumble about it. Everyone but you in this project is stupid anyway so why not tell the world about it.

: Oh yeah, right, just rename them, great idea without even knowing where they were renamed in the first place... Did it cross your mind that there might have been a reason to rename this files in the first place and that changing them back might not be in the interest of those who renamed them? I prefer to reach some consense about what do to before actually doing it and not just making life harder for everyone... -- [[User:Grumbel|Grumbel]] 14:51, 26 Jul 2006 (BST)
::Better don't write articles when having a bad day ;) -- [[User:Penma|Penguinmaster]] 19:18, 4 Oct 2006 (CEST)

== Where are my L/R buttons? ==

Default is DELETE/END and joystick button 4/5. --[[User:WolfgangB|WolfgangB]] 16:31, 26 Jul 2006 (BST)

== GUI .sprite tool? Hmm... If nobody else will... ==

...I might try out my [Python|Tk|bash|C++] skills to make an [app|script] to edit .sprite files. I doubt I'll get around to it, but know that it ''is'' on my list. --[[User:Djwings|DJ Wings]][[User_talk:Djwings|<sub>Freesyle here</sub>]] 12:12, 16 January 2007 (PST)

: Update: I've started on it. The source will be available (obviously...), once I get it to do something useful. I'm using Glade, the app's called GSprite.
