## Badguys of Icy Island

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


Mr. Snowball
========

![](img/badguy/icons/Snowball.gif "Snowball.gif")

Snowball is a straight forward walking enemy, when reaching an edge he will fall down and continue walking on the platform below. Jumping on him will squish him and thus kill him.

-   Appearance=A walking snowball with eyes and boots on.
-   Behaviour=Walks around. Falls down from all cliffs.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes


Mrs. Snowball (smartball)
=========================

![](images/SmartSnowballSprite.png "SmartSnowballSprite.png")

Mrs. Snowball behaves like [Mr. Snowball](Mr._Snowball "wikilink"), but instead of walking off a platform she will turn around when reaching the edge.

![smartball](img/badguy/icons/Mrs._Snowball_(smartball).png)

-   Appearance=A walking snowball with eyes and boots on.
-   Behaviour=Walks around. Stays on platforms.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes


Captain Snowball
================

![Captain Snowball](img/badguy/icons/Captain_Snowball.png)

A snowball who claims to be captain of a ship despite not having set foot on one himself. Captain Snowball behaves just like Mr. Snowball but once faced with a slope or the edge of a platform, he will attempt to jump over it. Sometimes he succeseds, sometimes he doesn't.

-   Appearance=A walking pirate snowball with eyes and boots on.
-   Behaviour=Walks slower then the average snowball. Falls down from
    all cliffs.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes


Bouncing Snowball
=================

![](images/BouncingSnowball.png) ![](img/badguy/icons/Bouncingsnowball.png)

A leg-less snowball with eyes that moves forward in a constant bounce
motion like a ball. It's jump height is big enough that Tux can
pass under him safely, while making it difficult to jump on him or
(potentially) outright impossible when he is at the highest point.

### Comments

> [[Grumbel|User#grumbel]]: Jump height and width in the current
> implementation could be tweaked a bit to make it easier to stand
> below it. Placement in the levels is the biggest problem, should
> only be used in open spaces, not closed ones where it hits the
> ceiling and bouncing becomes unpredictable. It could also move
> faster and jump higher, at the moment it is far to easy to just jump
> on it.


Flying Snowball
===============

![](img/badguy/icons/Flyingsnowball.png)

A snowball with a propeller underneath and a pilot hat and goggles.
Flies up and down constantly.

-   Appearance=A sowball with a propeller underneath, a pilot hat and goggles.
-   Behaviour=Flies up and down.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes


Jumpy (snowjumpy)
=====

![](images/SnowJumpySprite.png)

Jumpy jumps up and down and stays stationary on the same position. His viewing direction follows [Tux](Tux "wikilink"). The simplest way of avoiding him is usually to run below him or jump over him at the right time.

-   Appearance=A spiky grey ball with a spring underneath.
-   Behaviour=Jumps up and down.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=yes

### Comments:

> [[Grumbel|User#grumbel]]: We have way too many variations of
> snowballs, making things look a little boring. I tend to prefer the
> Milestone 1 Jumpy for it's visual distinctiveness.
>
> ![](images/Jumpy.png)

Spiky (armoredsnowball)
=======================

![](images/SpikySprite.png "fig:SpikySprite.png") ![Sleeping Spiky](img/badguy/icons/Sleeping-left.png)

Spiky behaves just like *Mr. Snowball*, but he carries a spiky helmet which makes him invulnerable against jump attacks as well as hurting Tux.
They can sometimes be found asleep waiting for their enemy to approach. Once awoken, they behave the same as always.

-   Appearance=A walking snowball with a spiky helmet.
-   Behaviour=Walks or sits around. Turns at ledges if about to fall offscreen.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=yes


Mr. Iceblock
============

![](img/badguy/icons/Mr_iceblock.gif)

Like *Mr. Snowball*, Mr. Iceblock is a simple straight forward enemy. He will not stay on platforms. When jumped upon he will get knocked out and become a portable item that one can use to throw or be kicked at other enemies. Continually squishing Mr. Iceblock will eventually kill him. Since version 0.3, he only walks off a cliff if there is something safe on which he can land.

-   Appearance=A cube of ice with eyes and legs.
-   Behaviour=Walks around. When jumped on once, it becomes a kickable and portable block of ice.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes

### Behavior in [Milestone 1](Milestone_1 "wikilink")

![Old image of Mr. Iceblock](images/Mriceblock-left-2.png "fig:Old image of Mr. IceBlock")

If Mr. IceBlock is eliminated, Tux is awarded 100 points. If destroyed via repeated squishes, Tux can get up to 550 points.

When carrying Mr. IceBlock, Tux is granted a “get out of jail free” card: if he hits another, non-invincible badguy, both Mr. IceBlock and the other badguy are killed, leaving Tux unharmed. A minor glitch occurs: Mr. IceBlock is scored as 0 points.


Mrs. Iceblock (smartblock)
==========================

![](img/badguy/icons/Mr_iceblock.gif)

Similar to Mrs. Snowball, Mrs. Iceblock behaves as Mr. Iceblock but will turn around when reaching the edge of a platform instead of walking off.

* Image=Mrs iceblock.gif
* Appearance=A pink cube of ice with eyes and legs.
* Behaviour=Walks around. When jumped on once, it becomes a kickable and portable block of ice.
* Squish=yes
* Buttjump=yes
* Freeze=no
* Burnable=yes


Snowman
=======

![](images/SnowmanSprite.png "fig:SnowmanSprite.png")

A snowman is build out of a base body combined with a Mr. Snowball as its head, if the body is destroyed, the Mr. Snowball on top will fall out and continue moving around.

-   Appearance=A walking snowman with eyes.
-   Behaviour=Walks around. Falls off platforms. When jumped on, it turns into Mr. Snowball.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes


Kamikaze Snowball (snowshot)
============================

![Snowshot|right](img/badguy/icons/Kamikaze-left2.png "fig:Snowshot|right")
The Kamikaze Snowball shoots out of a [cannon](Cannon "wikilink") and flies a straight line until crashing. He is very angry, or very “wise”, and so can levitate through the force of his will. He is so concentrated on this, however, that he cannot turn or adjust his velocity.

-   Appearance=A flying snowball with a fierce facial expression.
-   Behaviour=Flies in straight line until he crashes in something. Can be shot from a cannon
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes

![Old version of Kamikaze Snowball.](images/Kamikaze-left.png "Old version of Kamikaze Snowball")


Crystallo
=========

![](images/Crystallo.png "Crystallo.png")

Another very basic enemy, but unlike the Mr. Snowball or Mr. Iceblock he doesn't walk around in a straight pattern, but walks forward and backward around a fixed position.

-   Appearance=An ice crystal.
-   Behaviour=Moves around but doesn't leave a certain point.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes

### Comments:

> [[Grumbel|User#grumbel]]: As is, it's behaviour is pretty useless,
> needs a complete overhaul. Doing a ice version of the [Stony in
> Wall](images/Stony_wall.png) would be an option.


Ice Crusher
============================

![Iceblock](img/badguy/icons/Iceblock.png)

Ice Crushers are enemies that are hanging on the ceiling or walls. When Tux gets within one tile they will attempt to crush Tux into the nearest wall or floor. After they hit a wall, they slowly drift back up. On this “return trip,” Tux may safely climb on top of them and hitch a ride. When in their resting position, their eyes shall follow Tux.

There are two kinds of Ice Crushers, differentiated by their size: Krush (2x2 tiles) and Krosh (4x4 tiles).

-   Appearance=An ice block (2x2 for Krush, 4x4 for Krosh) making an angry face.
-   Behaviour=Stationary until [Tux](Tux "wikilink") is in range. Then moves with unstoppable force.
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no

### Concept art

This concept art is for a big version that could serve as a miniboss.

![Concept art for *Ice Crusher*](images/Icecrusher-concept-art.png "Concept art for Ice Crusher"){width="400"}


Stalactite
==========

![Stalactite|right](images/Falling.png "fig:Stalactite|right")

The stalactite stays stuck to the ceiling until Tux walks near it, then begins shaking. After a bit of shaking, it falls down in an attempt to hurt Tux, while also harming badguys that get in the way.

Note: They can also be triggered when hit with a fireball and cause freezable enemies to be frozen upon impact!

-   Appearance=An icicle hanging from the ceiling and underneath
    platforms.
-   Behaviour=Falls down when Tux gets near.
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no


Yeti
====

![](images/Yeti2.png "Yeti")

The Yeti is the boss enemie that awaits Tux in the first castle. For more information on bosses, see [Bosses](https://github.com/SuperTux/supertux/wiki/Bosses#Yeti)

### Concept art

![](images/Yetiboss.jpg)

![](images/Yeti2.jpg)

![](images/Yeti-concept.png)

![](images/Yeti-scan-roughs.png)

![](images/Yeti-concept-throw.png)


List of icy island's badguys in SuperTux 0.1.3
----------------------------------------------

[[Badguy.1 category](:Category:Badguy.1 "wikilink")](Template:See_also "wikilink")

The following badguys are available in the stable 0.1 release.

-   [Bouncing Snowball](Bouncing_Snowball "wikilink")
-   [Flame](Flame "wikilink")
-   [FlyingSnowball](FlyingSnowball "wikilink")
-   [Jumpy](Jumpy "wikilink")
-   [Mr. Bomb](Mr._Bomb "wikilink")
-   [Mr. IceBlock](Mr._IceBlock "wikilink")
-   [Snowball](Snowball "wikilink")
-   [Spiky](Spiky "wikilink")
-   [Stalactite](Stalactite "wikilink")
-   [Fish](Fish "wikilink")


See also
--------

-   [Proposed Badguys](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Badguy Ideas)
-   [Badguys concept art](Badguys_concept_art "wikilink")
-   [Worlds](https://github.com/SuperTux/supertux/wiki/Worlds)
-   [Bosses](https://github.com/SuperTux/supertux/wiki/Bosses)

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

[Category:For Users](Category:For_Users "wikilink") <Category:Design> <Category:Badguy>
