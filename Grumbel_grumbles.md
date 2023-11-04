![](images/Grumbel.png)

This is a list of issues, problems, ideas and stuff that Grumbel has about SuperTux.

Why is **hitbox** in .sprite called 'hitbox', when all I want is affect the offset/hotspot of the sprite and why should I supply a width/height parameters when I don't need them? hitbox and offset should really be two seperate concepts in a .sprite file.

Somebody should replace all that two-pixel large 'smoke/dust' with a proper dust sprite.

If stuff kills Tux it would actually be usefull if it looks deadly, which most stuff simply doesn't (I mean you spike tiles...).

Where is the consistency? Sometimes tiles are used for background, then they are used for the foreground or even interactive layer, its a mess.

Water... yeah, have a pinguin and then no ability to swim, not even collision with water, how stupid is that?

Trash, junk and other garbage and we call it 'levels'. The svn needs really some large cleanup to seperate the useless testing stuff from the usefull ones and the testing from the actually playable.

Reset point uglyness, they don't look good and not even like a reset point...

Difficulty, some of the current SuperTux levels that Ikaruga look like a game for kiddies... there really needs to be done \*A LOT\* to make SuperTux playable again. It would be nice to put a bit of fun back into SuperTux, currently its a frustrating mess.

Where are my L/R buttons? Autoscroll is ok, but a way to manipulate it manually would be really usefull.

  
*Peek U/D/L/R is implemented.*

The wingling coloring stinks (to much white), as does is behaviour, kamikaze dive is neither fun nor good looking

Forest tile repetition... if you want to go blind, looking at the forest tiles is a good way to acomplish that, somebody should either remove the repetition or redraw that mess completly.

Where is the dedicated run animation? Graphical hints are always a good thing.

Animation? None found. SuperTux, the game as a whole, not just the sprite, looks horrible, all static, with no fun animations around, boring.

Where are the tile-backgrounds? Huge bitmap graphics are soooo ugly..

Why have doors so small and Tux so fat? Tux just doesn't fit through a door by any means.

The bomb certainly wins a price for ugliest gamesprite ever...

  
*It has been changed in SVN.*

Is there a way to load a sprite without having a sprite file? If not, why not? Writing the same boring sprite syntax over and over again is both error prone and relativly useless.

How do I rotate a sprite? We should have OpenGL up and running, shouldn't we?

How about align\_center, align\_right, align\_top\_left, etc.? Instead of exact pixel positions?

How about a GUI tool to edit .sprite files?

Compiling SuperTux today tages \*AGES\*, far far longer then needed, this is because for example src/badguy/badguy.hpp includes tons and tons of completly unneeded header files. The reason for this is to reduce the needed \#include directives in the badguy files itself, which is cool, but comes at a \*high\* price, little changes in one of those include files will require a huge recompile, even so if very few files actually depend on those changes. Possible solution: Precompiled header files, should allow to both keep \#includes to a minimum and reduce compile times a lot.

Some experiments with precompiled headers and ccache (compiling badguy/ subdirectory):

`ccache:`
` real    0m10.645s,  user    0m5.932s, sys     0m1.764s`
`g  `
` real    1m40.436s, user    1m13.833s, sys     0m5.352s`
`precompiled header, gch`
` real    0m51.715s,  user    0m40.583s, sys     0m3.432s`
` real    0m4.490s,   user    0m3.860s,  sys     0m0.308s`

Flexlay is up and running again, need a bit of testing if it can actually save levels, loading at least seems to work, probally time to move ClanLib over into the flexlay repository.

![Things to avoid in leveldesign](images/Howtonotdesignlevels.jpg "fig:Things to avoid in leveldesign") ![Some more things to avoid in leveldesign](images/Hallofshame.jpg "fig:Some more things to avoid in leveldesign")

Badguys must not collide or at least not like they do today (ie. stack), best seen in world1/27 where the snowballs and yeti colliding results in compltetly unpredictable and unavoidable patterns, thus killing the player far to often.

Why the \*juck\* do we have filenames full of spaces and other useless junk in data/levels/world1/, what is that good for, except to make working with those levels harder? Duplicate information should be avoided and those “levelnames in filenames” is really doing nothing good.

Enemy Criticts
--------------

-   i don't like cherrybomb, old wasn't better, but I prefer my bombsprite (mrbomb.xcf)
-   i don't like zeekling, basic design is ok, but sprite and behaviour are ugly
-   igle should go into trashcan
-   angrystone looks ugly
-   dart is to small, almost invisible, needs larger sprite
-   fluffy looks damn cool, but what about behaviour?
-   snail should go to trashcan, but might be fixable
-   new spiky behaviour might not batch with M1 levels, needs testing
-   tumbleweed is ugly
-   I want my Homer S. Yeti
-   darttrap really does not belong into the forest, but castle
-   jumpy looks more like a castle enemy, but is used all over in M1
-   mrtree breaking up is a nice idea on paper, but awefull in practice (to many enemies on the screen at once)
-   poison ivy -&gt; trash
-   stlalactites are ugly, maybe they should be shiny and blink?
-   dispenser is ugly and overused
-   flame is ugly, trail and actual fire might help
-   ghosts look mighty cool, but behaviour?
-   kirby is cool, but probally for wasteland, not forest
-   mr\_fluffy? -&gt; use fluffy instead, that seems a duppe
-   nolok doesn't caputure the essence of the statue
-   spidermite -&gt; trash
-   stony -&gt; ok, but not great
-   waterdroplet, a bit ugly -&gt; behaviour?
-   colory -&gt; kind of cool -&gt; behvaviour?
-   flamefish -&gt; lame, use classic fireball instead
-   granito -&gt; ugly eyes
-   kugelblitz -&gt; ugly
-   iceblock -&gt; black ugly surround
-   penny -&gt; animation
-   skullyhop might need another leg or a better leg
-   totem, ugly and behaviour at the moment questionable
-   willowisp, ugly, but idea is cool, maybe make it friendly for dark areas?
-   Rockets being sqished? Never heard of that.

Features
--------

New Milestone2 features that look usefull:

-   wind, which can blow Tux around
-   switches that can be used to trigger stuff
-   unstable platforms, that break when Tux stands on them
-   candles, that can go on and off, what are they good for?
-   moving platforms, Tux can stand on them and get moved around
-   Dart enemies, they attach to a wall and shoot arrows
-   auto scroll
-   vertical/horizontal scroll
-   stacking, not sure if that is actually usefull
-   lightmapping

Bugs
----

-   ![Unsymetric Tux Hitbox](images/Unsymetrichitbox.png "fig:Unsymetric Tux Hitbox")
-   Boat is not heading left when sailing back to island