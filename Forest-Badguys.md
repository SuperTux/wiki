## Badguys of Rooted Forest

A badguy in SuperTux is a foe of Tux. They may not be "bad" in the way
that a hedgehog isn't really bad, but they can certainly hurt Tux.
Most of the badguys are creatures, like Snowballs with varying
characteristics, but some are more like objects (Stalactite for
example) or phenomena like Flame.

Tux will try to avoid approaching badguys if possible. If he runs into
one or one drops on his head, he is hurt. When hurt Tux will lose a
powerup or, if Tux has no powerups left, he will be killed.

Many of the badguys Tux can knock out by jumping on them and squishing
them. Others are only stunned by this for a short while or are
insusceptible to this and hurt Tux instead. As a rule of thumb,
badguys with a spiky head or helmet can usually not be jumped on. For
a list of badguys that can be squished take a look at the squishable
badguys category. Most badguys can be killed with the fire- or
iceflower power up.

This page shall describe all enemies, old and new, in as much detail
as possible. We also need to settle down on proper names for enemies,
since currently there is a lot of confusion. If you want see on real
names, click [here](real_badguys_names "wikilink").

##### Further references

* [Milestone 2 Design Document/Enemies](http://supertux.lethargik.org/wiki/Milestone_2_Design_Document/Enemies)
* [Proposed badguys](http://supertux.lethargik.org/wiki/Proposed_Badguys)
* [Badguy concept art](http://supertux.lethargik.org/wiki/Badguys_concept_art)
* [Worlds](https://github.com/SuperTux/supertux/wiki/Worlds)
* [Bosses](http://supertux.lethargik.org/wiki/Bosses)


Poison Ivy
==========

**Poison Ivy** is a [badguy](badguy "wikilink") found in the
[Forest](Forest "wikilink") of world 2. The plant roams around at the
ground, falling from platforms.

### Proposed behavior

-   Advanced forms of Poison Ivy could have the ability to flap their
    leaf-wings, then (after some flapping) do a short hop towards Tux

### See also

-   [Walking tree](Walking_tree "wikilink")
-   [Walking leaf](Walking_leaf "wikilink")


Walking Leaf
============

**Walking Leaf** is a [badguy](badguy "wikilink") in the
[Forest](Forest "wikilink") world. It is a bit smarter than the ordinary
badguy because it does not fall off of platforms. The leaf will hurt
[Tux](Tux "wikilink") on contact and can be killed the usual ways. Since
it is more careful, it is walks a bit slower than the average badguy.


Mr. Tree (walkingtree)
======================

**Walking tree** (sometimes also **Mr. Tree**) is a
[badguy](badguy "wikilink") in the [Forest](Forest "wikilink"). When
jumped on by [Tux](Tux "wikilink"), breaks into two [Poison
Ivy](Poison_Ivy "wikilink") and one [Stumpy](Stumpy "wikilink").

### Design considerations

:   *This section may be outdated.*

Hurt [Tux](Tux "wikilink") Option 1: Run over him.

Hurt [Tux](Tux "wikilink") Option 2: Runs over him and throws harmful
objects at him. Mr.tree starts throwing fire balls after being hit with
a fire shot from Tux.

Hurt [Tux](Tux "wikilink") Option 3: Mr.Tree throws (spawns) harmful
leaf/hair clump creatures by pulling clumps from his head. These
leaf/weed creatures attack Tux.

Hurt the enemy Option 1: Jump onto it.

Hurt the enemy Option 2: Knock down Mr.Tree by throwing a Snail shells
at him. Snails creatures can be stunned and then thrown at the tree. If
Mr.Tree is hit with fire the animation changes and Mr.tree starts
throwing fire balls at Tux. It is not a good idea for the player to
light trees on fire, it just makes Mr.Tree mad.

Additional and/or Future Gameplay Ideas: [Tux](Tux "wikilink") could
jump into the tree from under and control them since they're hollow, but
only if Tux is invulnerable. However, he can't jump inside them, other
than out of them.

Side Notes: normal trees in the background may shake their branches to
disturb [Tux](Tux "wikilink") and other creatures. Also, nonwalking
trees in the background might shake their branches disturbing Tux and
other creatures.

There might be rolling logs as well. Floating logs could also be useful
when crossing a river/waterfall; Tux could control them if he jumped on
them.

### Proposal for burning Mr. Tree

When Mt. Tree is hit by a fireball, it might be set on fire. A burning
Mr Tree runs around, killing small enemies (like Poison Ivies) and
setting on fire other Mr Trees and straw blocks. If a burning tree hits
Mr Bomb, they both die (Mr Bomb explodes). After a while, Mr Tree's
leaves will burn completely, reducing it to a normal Stumpy (or killing
it). A burning tree might be immune to fireballs.

### Proposal for Spooky Mr Tree

In Ghost forest, Mr Tree could have no leaves and have a carved out,
spooky face with jagged branches. In Milestone 0.3, Mr Tree releases one
or two Poison Ivies when jumped on. Spooky Mr Tree could release bats or
some such thing.

### Proposal for Branches

Mr Tree could have a thin branch sticking out either side of him which
Tux can stand on to be carried around. This could serve a purpose if
there was something that badguys could walk through but Tux couldn't.


Snail
=====

**Snail** or **Slow Snail** is a [badguy](badguy "wikilink") found in
the [Forest](Forest "wikilink"). When jumped upon, flips over. When
flipped over, further jumps on it will kick it around, hurting
everything in its way. Dies when [buttjumped](buttjump "wikilink") or
after being squished for a number of times.

### Design considerations

The *Snow Snail* should be an enhanced counterpart to [Icy
Island](Icy_Island "wikilink")'s [Mr.
IceBlock](Mr._IceBlock "wikilink"). They currently share the same
behaviour, i.e. Tux can jump on it to make it stop, carry it around
and/or kick it to use it as a projectile. In addition to that, the Snow
Snail could stop from time to time and excrete puddles of slime that
cover the ground and disappear after a certain amount of time. Whenever
Tux steps into such a puddle, his movement is slowed down and he cannot
jump until he slowly worked his way out of the trap or the puddle
disappears by itself.

The Snow Snail should move slower than Mr IceBlock and speed up whenever
Tux is in its visible area, especially when he's trapped in a slime
puddle.

Since the Snail is used in the forest world, the name might be changed
to Slow Snail

-   Proposed modified behaviour:
    -   When flipped over and bumped horizontally, the Snail will just
        flip back on its feet
    -   When flipped over and jumped on one end, the Snail will fly not
        only horizontally but also vertically
    -   When it hits a wall while flying it will turn back on its feet


Igel
====

**Igel** is a [badguy](badguy "wikilink") in the second world of
*SuperTux*, the [Forest](Forest "wikilink"). Igel cannot be squished or
[buttjumped](buttjump "wikilink") due to its spines but they can be shot
with a [fireflower](fireflower "wikilink") when facing
[Tux](Tux "wikilink").

The term “Igel” is German for “hedgehog”, which is precisely why the
*Igel* in the game look like hedgehogs.

### Proposed behavior

:   ''Note: The behavior described below differs from the behavior
    currently implemented in the development version of *SuperTux*.''

Although basically vulnerable to shots that hit the soft head, Igel will
immediately curl up for some seconds as soon as being shot at, thus
either absorbing or deflecting the shot.

Upon reaching a ledge or when [Tux](Tux "wikilink") stands less than 5
tiles behind Igel, Igel will slowly turn around, facing the camera and
thus exposing the only weakness: When hit by a bullet while facing the
camera, Igel will flip over for some seconds and can be squished by
jumping on the exposed belly.


Jumpy (woodjumpy)
=================

![](images/SnowJumpySprite.png)

Jumpy is a wooden barrel with metal spikes attached to it. He jumps up and down and stays stationary on the same position. His viewing direction follows Tux. The simplest way of avoiding him is usually to run below him or jump over him at the right time.

| Property       | Status |
|----------------|--------|
| Squishable     | no     |
| Buttjumpable   | no     |
| Burnable       | yes    |
| Freezable      | yes    |

Fish
====

![](images/IceFish.png "fig:IceFish.png")

Already in the code, but not
much used in Milestone1 Levels. This badguy shouldn't be used in
Icyland, it is a forest enemy.

![Fish](img/badguy/icons/FishBlue.png)

| Property       | Status |
|----------------|--------|
| Squishable     | no     |
| Buttjumpable   | no     |
| Burnable       | yes    |
| Freezable      | yes    |

**Fish** is a [badguy](badguy "wikilink") that jumps out of water. When
[Tux](Tux "wikilink") has to cross the water he has to pay attention to
the fish so he doesn't get caught.

### Proposed changes

<Template:Proposed>

Maybe a different color can be used in the forest world than in the
[Icyisland](Icyisland "wikilink").

Also, possibly there should be a few different types of fish:

1.  Standard up-and-down movement
2.  Curving Jump landing in a different place, going back and forth
3.  Archer Fish
    -   Stays below the surface of the water, but follows tux when he is
        on platforms above
    -   Shoots high pressure water which can break blocks and knock Tux
        into water where the archer fish can get him
4.  Swordfish
    -   Curving Jump following Tux and jumping higher when there is a
        chance to get Tux

### Comments

> [[Grumbel|User#grumbel]]: Doesn't look dangerous enough, not obvious
> if he can be jumped up on. Maybe make it bigger and actually eat Tux.


Mole
====

The **Mole** is a [badguy](badguy "wikilink") found in the
[Forest](Forest "wikilink"). He's usually underground, so that only his
molehill can be seen. He throws out small rocks in random directions
that can hurt [Tux](Tux "wikilink"). From time to time, he peeks out
which is the time in which Tux can squish him by jumping on him.


Owl
===

![](images/Owl.png "fig:Owl.png")

A flying enemy that can carry things around and let them drop on Tux. One thing it is throwing might be *SkyDive*.

Some initial code is available from the [SVN](SVN "wikilink") repository since [6558](Template:Revision "wikilink"). Graphics are still pretty much a to-do. —[octo](User#octo "wikilink") 17:25, 6 March 2010 (UTC)

![Owl](img/badguy/icons/Owl.png)

| Property       | Status |
|----------------|--------|
| Squishable     | yes    |
| Buttjumpable   | yes    |
| Burnable       | yes    |
| Freezable      | no     |

The Owl is a [badguy](badguy "wikilink") from the [Milestone 2
Design Document](Milestone_2_Design_Document "wikilink"). It flies high
up in the air and carries badguys around. When Tux is below it, it will
drop whatever it is carrying.

This badguy is in the [SVN](SVN "wikilink") repository since
[6558](Template:Revision "wikilink"). The graphics for this badguy still
need to be improved. The graphics currently in SVN are colorized
versions of the concept graphics, basically.


Zeekling
========

**Zeekling** is a [badguy](badguy "wikilink") found in the
[Forest](Forest "wikilink"). It flies left and right in a straight path,
usually near the top of the level. When [Tux](Tux "wikilink") is below
it, will dive down to hit him. Tux can avoid being hit by hiding
underneath platform and other solid blocks.

Should be removed from Forest World for now.


Skullyhop
=========

![](img/badguy/icons/Standing-0.png)

| Property       | Status |
|----------------|--------|
| Squishable     | yes    |
| Buttjumpable   | yes    |
| Burnable       | yes    |
| Freezable      | yes    |

**Skullyhops** jump around and chase Tux.

![Iced skully hop.](images/Skullyhop-iced-left.png "Iced skully hop.")


Dart Trap
=========

-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A skull mounted to the wall.
-   Behaviour=Static. Shoots darts at regular intervals.
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no

The **Dart trap** is a [badguy](badguy "wikilink") in form of a skull.
In regular intervals it shoots darts out of its mouth. The darts fly in
a straight line, hurt [Tux](Tux "wikilink") and cannot be destroyed but
must be avoided. The *Dart trap* is mostly found in castles in the
[Forest](Forest "wikilink") world.

### To be done

<Template:outdated>

-   mechanical sound when dart is loaded
-   hissing sound when dart is fired
-   clicking sound when dart hits the wall

:   i belive this is already implemented in milestone 1.5 & subversion
    --[Disk](User#disk "wikilink") 18:51, 30 August 2007 (UTC)


Spidermite
==========

-   Image=Spidermite0.png
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A spider hanging from the ceiling.
-   Behaviour=Moves up and down.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes

**Spider** is a [badguy](badguy "wikilink") available in SVN. It flies
up and down vertically, hurting Tux on contact, although Tux can squish
him like a [Snowball](Snowball "wikilink"). It is themed to appear in
the [Forest](Forest "wikilink") world but is not (widely) used yet.


Livefire
========

...


| Property       | Status |
|----------------|--------|
| Squishable     | no     |
| Buttjumpable   | no     |
| Burnable       | no     |
| Freezable      | yes    |


Will-o-wisp
===========

The **Will-o-wisp** is a mean little [badguy](badguy "wikilink") found
in the haunted regions of the [Forest](Forest "wikilink"). When
[Tux](Tux "wikilink") comes close, it will start to follow him slowly.
Once it reaches Tux, he will be teleported to another, possibly
dangerous part of the level. If Tux manages to get out of reach of the
*Will-o-wisp*, it will stop following him.


Ghost Tree
==========

The ghost tree is the planned boss enemy that awaits Tux in the second castle. It is not fully implemented yet and only an unfinished version of it and its graphics incomplete can be found in the game. For more information on bosses, see [Bosses](https://github.com/SuperTux/supertux/wiki/Bosses#Ghost_Tree).

![](images/Forestboss.jpg "forestboss.jpg")

-   The tree is walking left/right, there will be platforms around the tree so tux can jump these to avoid getting hit
-   The tree is growing roots from the ground to attack you
-   The tree is glowing in a color that changes from time to time
-   The tree is sucking in colored will-o-wisp like things that have the same color as himself
-   Sucked in will-o-wisps make him grow
-   You destroy the tree by throwing something in a different color at him (lamps or arcorns?)

Sketch 2
--------

Less blue, more brown

![](images/Forestboss2.png "Forestboss2.png")

List of rooted forest's badguys as of SuperTux 0.6.2
----------------------------------------------------

-   Poison Ivy
-   Walking Leaf
-   Leafshot
-   Snail
-   Igel
-   Jumpy
-   Fish
-   Mole
-   Owl
-   Zeekling
-   Skullyhop
-   Dart Trap
-   Spidermite
-   Livefire
-   Will-o-wisp
-   Ghost Tree

List of rooted forest's badguys in SuperTux 0.1.3
-------------------------------------------------

-   Fish
-   Jumpy


See also
--------

-   [Proposed Badguys](https://github.com/SuperTux/supertux/wiki/Current-Design-Document)
-   [Badguys concept art](Badguys_concept_art "wikilink")
-   [Bosses](https://github.com/SuperTux/supertux/wiki/Bosses)
-   [Worlds](https://github.com/SuperTux/supertux/wiki/Worlds)

[Category:For Users](Category:For_Users "wikilink") <Category:Design> <Category:Badguy>

