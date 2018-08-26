== Bouncing\_Snowball

-   Name=Bouncing Snowball
-   Image=Bouncingsnowball.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A [Snowball](Snowball "wikilink") with eyes but without
    feet.
-   Behaviour=Jumps around. Jumping is affected by walls and other
    badguys.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.1

**Bouncing Snowball** is a [badguy](badguy "wikilink") in [Icy
Island](Icy_Island "wikilink"). He bounces around, occasionally hitting
Tux or even other badguys. In version 0.1.3, he always bounces in the
same direction, regardless of the angle of the surface that he hits. The
bouncing action in 0.3 and above is more realistic.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Cannon

-   Name=Cannon (dispenser)
-   Image=Dispenser rocket launcher.png
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=Differs, see below.
-   Behaviour=Spawns new badguys at fixed or random intervals.
-   Squish=yes
-   Buttjump=yes
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=Milestone 2

A **Cannon** is a [game object](game_object "wikilink") that spawns new
[badguys](badguy "wikilink"). The interval in which badguys are spawned
is either fixed or random. A cannon can be shot with either the
[fireflower](fireflower "wikilink") (dies) or
[iceflower](iceflower "wikilink") (stops it emitting new badguys).
Whether or not the dispenser is squishable and butt-jumpable depends on
the appearance: The *trapdoor* and *rocket launcher* types are immune to
[Tux](Tux "wikilink") standing or jumping on them, the *cannon* type can
be broken this way.

It is also possible for the cannon to shoot inanimate, non-badguy
objects (even other cannons.)

### Appearance

There are three possible sprites for this object: Trapdoor, cannon and
(in lack of a better word) rocket launcher. Please note that despite the
name, *rocket launcher* is the preferred appearance, at least in [Icy
Island](Icy_Island "wikilink") ([Milestone 2](Milestone_2 "wikilink")).

Image:Dropper.png Image:Working.png Image:Dispenser rocket launcher.png

### Design considerations

:   *This section is possibly outdated.*

### Mechanics

-   Spawns new Badguys
-   Interval: Fixed or random
-   Appearance: Trap door, cannon or invisible
-   Start direction of badguys: Fixed or random
-   Initial velocity of badguys: Fixed or random

### Uses

-   fires rockets
-   drops badguys from a (shootable) trap door
-   spawn badguys in tubes
-   launches molten rocks out of a lava lakes

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Captain\_Snowball

-   Name=Captain Snowball
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A walking pirate snowball with eyes and boots on.
-   Behaviour=Walks slower then the average snowball. Falls down from
    all cliffs.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=

**Captain Snowball** is a [badguy](badguy "wikilink") planned to debut
in version 0.4. There are not yet many levels which feature *Captain
Snowball*, but he will most likely appear in [Icy
Island](Icy_Island "wikilink") levels or other snow-themed levels.

Planned for 0.4. In [SVN](SVN "wikilink") since
[5323](Template:Revision "wikilink").

![](Boarding-nq8.png "Boarding-nq8.png")

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Crystallo

-   Name=Crystallo
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=An ice crystal.
-   Behaviour=Moves around but doesn't leave a certain point.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 2

**Crystallo** is a [badguy](badguy "wikilink") in [Icy
Island](Icy_Island "wikilink"). He moves back and forth in a fixed
range. He is not yet widely used, but he has been implemented in some
test levels and some user-submitted levels.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Dart\_Trap

<Template:NeedSound>

-   Name=Dart Trap
-   Image=
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A skull mounted to the wall.
-   Behaviour=Static. Shoots darts at regular intervals.
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no
-   FirstVersion=0.3

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
    --[Disk](User:Disk "wikilink") 18:51, 30 August 2007 (UTC)

== Fish

-   Name=Fish
-   Image=FishBlue.png
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=A fish jumping out of water.
-   Behaviour=Jumps up out of water regularly.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=Milestone 2

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

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Flame

-   Name=Flame
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=A glowing sphere.
-   Behaviour=Follows a circular path around a certain point.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=no
-   FirstVersion=0.1

**Flames** are [badguys](badguys "wikilink") found in both
[worlds](worlds "wikilink") in *SuperTux*. They move in fixed circles,
hurting [Tux](Tux "wikilink") and other badguys on contact (unless, of
course, Tux is in invincibility mode.) Flames are immune to fire.
However, ice balls can kill them permanently as of version 0.3.4.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Flying\_Snowball

-   Name=Flying Snowball
-   Image=Flyingsnowball.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A [Snowball](Snowball "wikilink") with a propeller
    underneath and a pilot hat and goggles.
-   Behaviour=Flies up and down constantly.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.1

**Flying Snowball** is a [badguy](badguy "wikilink") often found in [Icy
Island](Icy_Island "wikilink"). It is a flying version of
[Snowball](Snowball "wikilink") which doesn't walk around but moves up
and down at random intervals and speeds.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Haywire

-   Name=Haywire
-   Image=MrBombCrazy.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A purple walking bomb.
-   Behaviour=Walks around. When jumped on, it's stunned for a little
    while and its explosion sequence is triggered.
-   Squish=yes
-   Buttjump=yes
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=Milestone 2

**Haywire** is a [badguy](badguy "wikilink") from the [Milestone 2
Design Document](Milestone_2_Design_Document "wikilink"). It is very
similar to [Mr. Bomb](Mr._Bomb "wikilink"): When jumped upon, the
explosion sequence is triggered. In contrast to *Mr. Bomb*, *Haywire*
will not lie still but ran around madly. [Tux](Tux "wikilink") can stun
*Haywire* for a short while by jumping on it again, but should try to
get out of its reach. When it explodes, hurts [Tux](Tux "wikilink") and
other badguys nearby.

When shot with a [Fireflower](Fireflower "wikilink"), explodes
immediately.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Igel

-   Name=Igel
-   Image=
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=Looks like a common hedgehog.
-   Behaviour=Walks around. Stays on platforms.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=

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

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Ispy

-   Name=Ispy
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=A spying eye.
-   Behaviour=Static, looking towards the nearest player.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=no
-   FirstVersion=

**Ispy** is a [badguy](badguy "wikilink") that can be found in all
[worlds](worlds "wikilink") of *SuperTux*. It is a spying eye looking
for the player. When the player can be seen by the eye, i.e. no other
badguys or walls are in the way, an action is triggered, for example
doors close or bridges are removed.

![](ChristophEstart.png "ChristophEstart.png")

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Jumpy

-   Name=Jumpy
-   Image=Left-up.png
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=A spiky grey ball with a spring underneath.
-   Behaviour=Jumps up and down.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=0.1

**Jumpy** is a [badguy](badguy "wikilink") found in many levels. He is
stationary, bouncing up and down on the spot. Unless
[Tux](Tux "wikilink") has a [fireflower](fireflower "wikilink") or an
[iceflower](iceflower "wikilink"), the only way to get past *Jumpy* is
to run below him or jump over him at the right time.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Krush\_and\_Krosh

-   Name=Krush and Krosh (icecrusher)
-   Image=Iceblock.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=An ice block (two by two for Krush, four by four for
    Krosh) making an angry face.
-   Behaviour=Clings to the ceiling until [Tux](Tux "wikilink") is
    underneath. Then drops with unstoppable force.
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no
-   FirstVersion=Milestone 2

**Krush** and **Krosh** are [badguys](badguy "wikilink") found in [Icy
Island](Icy_Island "wikilink"). They are usually found on ceilings. If
Tux comes underneath one, it suddenly drops without warning. If Tux does
not get out of the way fast, he is hurt. After they hit the ground, they
slowly drift back up. On this “return trip,” Tux may safely climb on top
of them and hitch a ride.

Both “icecrushers” are available in [SVN](SVN "wikilink"), but only
Krush is implemented in levels.

### Concept art

![Concept art for
*Icecrusher*](Icecrusher_(concept_art).png "Concept art for Icecrusher"){width="400"}

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Kugelblitz

-   Name=Kugelblitz
-   Image=Flying-0.png
-   FoundIn=*n/a*
-   Appearance=A *ball lightning* with sparks.
-   Behaviour=Moves to the ground, then randomly to the left and right
    within a limited range.
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no

:   *This [badguy](badguy "wikilink") has been removed from the
    [Milestone 2](Milestone_2 "wikilink") branch in
    [6282](Template:Revision "wikilink").*

**Kugelblitz** is a [badguy](badguy "wikilink") not widely used in
*SuperTux* yet. The *Kugelblitz* moves down to the ground and then
randomly left and right within a limited range. After a couple of
seconds it vanishes. Like the [Flame](Flame "wikilink") it cannot be
hurt but [Tux](Tux "wikilink") has to avoid it if possible. “Kugelblitz”
is German for “ball lightning”.

### Design considerations

The *Kugelblitz* (German for [“ball
lightning”](http://en.wikipedia.org/wiki/Ball_lightning)) falls from the
sky without warning; as soon as it hits the ground, it starts moving
back and forth randomly for about two or three seconds in a fixed range,
then vanishes with a pop in a cloud of smoke. Explodes on contact which
hurts Tux. Alternatively, instead of moving at a random pattern, it
could also move between coins or badguys.

The Kugelblitz cannot be hurt, the player has to avoid its radius until
it's gone. With the alternative version, Tux can collect all
coins/destroy all badguys before the Kugelblitz lands to make it
disappear at once. It looks like a yellowish glowing wheel with
animations for falling (with glowing trail), rolling, exploding and
vanishing in smoke. It can be used in Ghost Forest and Forest Castle
settings.

If the Kugelblitz hits water it vanishes and all water tiles get
electrified for a short period of time. During that time, contact with
water causes Tux and badguys to get hurt.

(I chose the German name because it's one of the few words that actually
sound cooler in German than in English, IMHO.)

Variation1
==========

The path of the kugelblitz could be led by looking at surrounding
things. For example the kugelblitz could always go the nearest coin or
enemy in a range of 3 tiles give that it would not need to change it's
direction more than 45 degree or so. This would allow the following 2
situations:

![](Kugelblitz2.jpg "Kugelblitz2.jpg")

The kugelblitz would go down and then go upwards along the 2 coins and
finally killing the 2 spikies and disappearing as there is no object
anymore it could move to.

![](Kugelblitz1.jpg "Kugelblitz1.jpg")

The kugelblitz would come down and start moving in circles from coin to
coin. You could stop this behaviour by collecting 1 of the coins at the
right time.

More Ideas
==========

-   The kugelblitz could be attracted to spikes and if it hits them
    disappear. Like a lightning arrester.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Mole

-   Name=Mole
-   Image=
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A molehill.
-   Behaviour=Static. From time to time, the mole peeks out.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=

:   *This [badguy](badguy "wikilink") has been removed from the
    [Milestone 2](Milestone_2 "wikilink") branch in
    [6281](Template:Revision "wikilink").*

The **Mole** is a [badguy](badguy "wikilink") found in the
[Forest](Forest "wikilink"). He's usually underground, so that only his
molehill can be seen. He throws out small rocks in random directions
that can hurt [Tux](Tux "wikilink"). From time to time, he peeks out
which is the time in which Tux can squish him by jumping on him.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Mr.\_Bomb

-   Name=Mr. Bomb
-   Image=Mrbomb.png
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=A blue walking bomb.
-   Behaviour=Walks around. When jumped on once, it is activated and
    explodes after a short time, killing nearby badguys.
-   Squish=yes
-   Buttjump=yes
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=0.1

**Mr. Bomb** is a [badguy](badguy "wikilink") that can be found in all
[worlds](worlds "wikilink") of *SuperTux*. When Tux or another badguy
hits him, he stops and begins ticking. After a few seconds, he explodes,
hurting all creatures within range. The presence of other Mr. Bombs
during explosion may cause a chain reaction of explosions. He also
explodes if he is hit by one of Tux's fireballs, but if hit by an
[iceball](Iceflower "wikilink"), he freezes without exploding.

<div style="clear: both;">
</div>
![Old image of Mr. Bomb](Mrbomb-left-0.png "fig:Old image of Mr. Bomb")
Due to Grumbel's complaint that “Mr. Bomb is the ugliest badguy ever
created”, user [Poison Ivy](User:Poison_Ivy "wikilink") created a
concept image for a new look by combining features of
[Snowball](Snowball "wikilink") and the old Mr. Bomb in Gimp. This
approach was not accepted either.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Mr.\_IceBlock

-   Name=Mr. IceBlock
-   Image=Mr iceblock.gif
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A cube of ice with eyes and legs.
-   Behaviour=Walks around. When jumped on once, it becomes a kickable
    and portable block of ice.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.1

**Mr. IceBlock** is a [badguy](badguy "wikilink") in [Icy
Island](Icy_Island "wikilink") with moderately complex behavior. In his
ordinary form, he works like an ordinary walking badguy, turning around
upon reaching walls and falling off cliffs. In version 0.3 and above, he
only walks off a cliff if there is something safe on which he can land.

When stomped on for the first time, Mr. IceBlock suddenly stops short.
If he is not stomped again for the next few seconds, he returns back to
normal. However, if he is stomped once more while squished, he suddenly
skids rapidly in one direction, hurting all creatures that he hits. When
skidding, he bounces off walls and falls off cliffs. If another creature
(including Tux) can stomp on him while he is skidding, he stops short
once more (and if he is stomped again, he begins skidding again, and so
on.)

While squished, Mr. IceBlock can also be “kicked,” if Tux runs up right
against him, and “carried” with the Action button. If Tux carries him
and lets go of Mr. IceBlock, he suddenly begins skidding in the
direction Tux is facing.

Continually squishing Mr. IceBlock will eventually kill him.

<div style="clear: both;">
</div>
### Behavior in [Milestone 1](Milestone_1 "wikilink")

![Old image of Mr.
IceBlock](Mriceblock-left-2.png "fig:Old image of Mr. IceBlock") If Mr.
IceBlock is eliminated, Tux is awarded 100 points. If destroyed via
repeated squishes, Tux can get up to 550 points.

When carrying Mr. IceBlock, Tux is granted a “get out of jail free”
card: if he hits another, non-invincible badguy, both Mr. IceBlock and
the other badguy are killed, leaving Tux unharmed. A minor glitch
occurs: Mr. IceBlock is scored as 0 points.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Mrs.\_Snowball

-   Name=Mrs. Snowball (smartball)
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A walking snowball with eyes and boots on.
-   Behaviour=Walks around. Stays on platforms.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 2

**Mrs. Snowball** is a [badguy](badguy "wikilink") found in [Icy
Island](Icy_Island "wikilink"). In contrast to
(Mr.) [Snowball](Snowball "wikilink") she will stay on platforms rather
than falling down. [Tux](Tux "wikilink") can easily handle these
“badgals” by jumping on them, squishing them in the process.

This badguy is planned for [Milestone 2](Milestone_2 "wikilink"). It is
in SVN since [5321](Template:Revision "wikilink").

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Owl

<Template:NeedGraphics>

-   Name=Owl
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A blue owl carrying objects around.
-   Behaviour=Flies left and right. Turns around when it hits a wall.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 2

The **Owl** is a [badguy](badguy "wikilink") from the [Milestone 2
Design Document](Milestone_2_Design_Document "wikilink"). It flies high
up in the air and carries badguys around. When Tux is below it, it will
drop whatever it is carrying.

This badguy is in the [SVN](SVN "wikilink") repository since
[6558](Template:Revision "wikilink"). The graphics for this badguy still
need to be improved. The graphics currently in SVN are colorized
versions of the concept graphics, basically.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Poison\_Ivy

-   Name=Poison Ivy
-   Image=Poisonivy.png
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A green or red plant with teeth.
-   Behaviour=Walks around. Falls down from every ledge.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.3

**Poison Ivy** is a [badguy](badguy "wikilink") found in the
[Forest](Forest "wikilink") of world 2. The plant roams around at the
ground, falling from platforms.

### Proposed behavior

-   Advanced forms of Poison Ivy could have the ability to flap their
    leaf-wings, then (after some flapping) do a short hop towards Tux

### See also

-   [Walking tree](Walking_tree "wikilink")
-   [Walking leaf](Walking_leaf "wikilink")

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Short\_Fuse

-   Name=Short Fuse
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A tiny version of [Mr. Bomb](Mr._Bomb "wikilink").
-   Behaviour=Walks around excitedly. Falls off platforms.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 2

**Short Fuse** is a [badguy](badguy "wikilink") found in [Icy
Island](Icy_Island "wikilink"). His behavior is intended to be similar
to that of [Mr. Bomb](Mr._Bomb "wikilink"), but the explosions do not
harm Tux -- they only throw him back.

This badguy is planned for [Milestone 2](Milestone_2 "wikilink"). It is
in SVN since [6511](Template:Revision "wikilink").

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Skullyhop

-   Name=Skullyhop
-   Image=Standing-0.png
-   FoundIn=Bonus Level, Ghost Forest
-   Appearance=A hopping skull.
-   Behaviour=Hops around, chasing [Tux](Tux "wikilink").
-   Squish=yes
-   Buttjump=yes
-   Burnable=yes
-   Freeze=yes

**Skullyhops** jump around and chase Tux.

![Iced skully hop.](Skullyhop-iced-left.png "Iced skully hop.")

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== SkyDive

-   Name=SkyDive
-   Image=BombFish.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A black, spherical fish.
-   Behaviour=Falls down; explodes when it hits the ground.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 2

**SkyDive** is a [badguy](badguy "wikilink") usually carried around and
dropped by [Owl](Owl "wikilink").

An initial version of this badguy has been committed to
[SVN](SVN "wikilink") in [6564](Template:Revision "wikilink").

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Sleeping\_Spiky

-   Name=Sleeping Spiky (sspiky)
-   Image=Sleeping-left.png
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=A snowball with a spiky helmet.
-   Behaviour=Sits around; starts walking when [Tux](Tux "wikilink")
    approaches.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=Milestone 2

**Sleeping Spiky** is a variation of the well-known
[Spiky](Spiky "wikilink"). This [badguy](badguy "wikilink") just sits
around sleeping. Only when he spots the player he slowly rises to his
feet and starts walking around.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Snail

-   Name=Snail
-   Image=Snowsnail.png
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A green snail with a purple helmet.
-   Behaviour=Moves around, falling from platforms.
-   Squish=yes
-   Buttjump=yes
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=0.3

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

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Snowball

-   Name=Snowball
-   Image=Snowball.gif
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A walking snowball with eyes and boots on.
-   Behaviour=Walks around. Falls down from all cliffs.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.1

**Snowball** is a simple walking [badguy](badguy "wikilink") found in
[Icy Island](Icy_Island "wikilink"). It will fall off platforms but will
turn around when reaching a wall. [Tux](Tux "wikilink") can easily
handle these badguys by jumping on them, squishing them in the process.

### See also

-   [Bouncing Snowball](Bouncing_Snowball "wikilink")
-   [Captain Snowball](Captain_Snowball "wikilink")
-   [Flying Snowball](Flying_Snowball "wikilink")
-   [Jumpy](Jumpy "wikilink")
-   [Mrs. Snowball](Mrs._Snowball "wikilink")
-   [Sleeping Spiky](Sleeping_Spiky "wikilink")
-   [Snowshot](Snowshot "wikilink")
-   [Spiky](Spiky "wikilink")

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Snowman

-   Name=Snowman
-   Image=SnowmanSprite.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A walking snowman with eyes.
-   Behaviour=Walks around. Falls off platforms. When jumped on, it
    turns into Snowball.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 2

**Snowman** is a [badguy](badguy "wikilink") found in [Icy
Island](Icy_Island "wikilink").

This badguy is planned for [Milestone 2](Milestone_2 "wikilink"). It is
in SVN since [6392](Template:Revision "wikilink").

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Snowshot

-   Name=Snowshot (kamikazesnowball)
-   Image=Kamikaze-left2.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=A flying snowball with a fierce facial expression.
-   Behaviour=Flies in straight line until he crashes in something. Can
    be shot from a [Cannon](Cannon "wikilink").
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 2

**Snowshot** is a [badguy](badguy "wikilink") planned to debut in
[Milestone 2](Milestone_2 "wikilink"). He is a version of
[Snowball](Snowball "wikilink") which is shot from a
[Cannon](Cannon "wikilink") and flies a straight line until crashing
into something.

In [SVN](SVN "wikilink") since [5323](Template:Revision "wikilink").

![Old version of the
badguy.](Kamikaze-left.png "Old version of the badguy.")

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Spider

-   Name=Spider (spidermite)
-   Image=Spidermite0.png
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A spider hanging from the ceiling.
-   Behaviour=Moves up and down.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.4

**Spider** is a [badguy](badguy "wikilink") available in SVN. It flies
up and down vertically, hurting Tux on contact, although Tux can squish
him like a [Snowball](Snowball "wikilink"). It is themed to appear in
the [Forest](Forest "wikilink") world but is not (widely) used yet.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Spike

![](Rightspike.png "fig:Rightspike.png")![](Down.png "fig:Down.png")\
![](Up.png "fig:Up.png")![](Left.png "fig:Left.png")\
IDs: 296, 297, 295, 298\
All spikes are hurting.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Spiky

-   Name=Spiky
-   Image=
-   FoundIn=[Icy Island](Icy_Island "wikilink"),
    [Forest](Forest "wikilink")
-   Appearance=A walking [Snowball](Snowball "wikilink") with a spiky
    helmet.
-   Behaviour=Walks around. Turns at ledges if about to fall offscreen.
-   Squish=no
-   Buttjump=no
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=0.1

**Spiky** is a [badguy](badguy "wikilink") commonly found in his
homeland, the [Icy Island](Icy_Island "wikilink"), but sometimes in the
[Forest](Forest "wikilink"), too. He is wearing a spiky helmet
protecting him from being squished by jumping on him, hurting
[Tux](Tux "wikilink") instead.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Stalactite

-   Name=Stalactite
-   Image=Falling.png
-   FoundIn=[Icy Island](Icy_Island "wikilink")
-   Appearance=An icicle hanging from the ceiling and underneath
    platforms.
-   Behaviour=Falls down when [Tux](Tux "wikilink") gets near.
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no
-   FirstVersion=0.1

**Stalactites** are basic enemies, usually found hanging on ceilings.
They start shaking when [Tux](Tux "wikilink") approaches, falling down
after a short time. They hurt Tux and kill non-invincible enemies on
touch.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Stumpy

-   Name=Stumpy
-   Image=Small-left-4.png
-   FoundIn=[Forest Island](Forest_Island "wikilink")
-   Appearance=A [Stumpy](Stumpy "wikilink") with eyes but treetop.
-   Behaviour=as [Snowball](Snowball "wikilink").
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.3

**Stumpy** is a [badguy](badguy "wikilink") in [Forest
Island](Forest_Island "wikilink"). He is beahaviour as
[Snowball](Snowball "wikilink"), but it is added in version 0.3.0.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Tikitchokwe

-   Name= Tikitchokwe
-   FoundIn=[Tropical\_Island](Tropical_Island "wikilink")
-   Appearance=character with a mask juggling with fire torch.
-   Behaviour=Moves right and left, throw fire torch on Tux.
-   Squish=Maybe
-   Buttjump=Maybe
-   Freeze=Maybe
-   Burnable=Maybe

Tikitchokwe is a proposed badguy for world 3
[Tropical\_Island](Tropical_Island "wikilink"). Graphism would be
influenced by Hawaiian Tiki and Tchokwe mask design. Behavior has to be
think about, limited torch or not, squish without torch but not with.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Toad

-   Name=Toad
-   Image=
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=Poisonous Toad
-   Behaviour=Takes long leaps at regular intervals.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=

**Toad** is a [badguy](badguy "wikilink") found in the
[Forest](Forest "wikilink"). It follows [Tux](Tux "wikilink") by jumping
around in large leaps. Can be squished by jumping on it.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Walking\_leaf

-   Name=Walking leaf
-   Image=Leaf.png
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=Reddish version of [Poison Ivy](Poison_Ivy "wikilink").
-   Behaviour=Walks around. Stays on platforms.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=

**Walking Leaf** is a [badguy](badguy "wikilink") in the
[Forest](Forest "wikilink") world. It is a bit smarter than the ordinary
badguy because it does not fall off of platforms. The leaf will hurt
[Tux](Tux "wikilink") on contact and can be killed the usual ways. Since
it is more careful, it is walks a bit slower than the average badguy.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Walking\_totem

-   Name=Walking totem
-   Image=Walking1.png
-   FoundIn=*none yet*
-   Appearance=A walking totem.
-   Behaviour=Walks around. Falls down from all cliffs.
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=Milestone 3

:   *This [badguy](badguy "wikilink") has been removed from the
    [Milestone 2](Milestone_2 "wikilink") branch in
    [6280](Template:Revision "wikilink").*

**Walking totem** is a [badguy](badguy "wikilink") that's not widely
used. It may be used in [Forest](Forest "wikilink") levels in the
future, though.

There is some “stacking” and “carrying” code in the SVN repository,
which is probably a preparation for the functionality described below.
Currently, only one segment is implemented – layered totems squish the
ones below them.

### Design considerations

<Template:Proposed>

![Walking Totem](Totem.jpg "Walking Totem")

Walking Totem Poles could be especially interesting, as they generally
have many faces... Perhaps as Tux jumps on them it breaks apart into
smaller totems each with a different face.

This or a big Walking Tree could be used as a Boss.

Behaviour: Walks, might spit electricity or fire

Look: A multifaced Totem Pole

Hurt Tux: spitting, run over Tux

Hurt it: jump at it to break into smaller Totems which can be jumped on
or spat at.

![Walking tree](Littletrees.png "Walking tree")

### Comments

-   It could be interesting to have the Walking Totem only loose its
    topmost face when Tux jumps on it
-   Yeah, and it would be even better if Tux has to butt-jump.
-   that would be very hard!
-   the walking tree looks so good, better than a coming-from-nowhere
    totem!
-   The Walking Totem looses only its topmost face when Tux jumps NORMAL
    on it, and it looses more faces when Tux butt-jump on it
-   maybe each face shoots, and when one is squashed, it will not shoot.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Walking\_tree

-   Name=Walking tree
-   Image=Walk-left-6.png
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=A walking tree with eyes.
-   Behaviour=Walks around. Stays on platforms.
-   Squish=yes
-   Buttjump=yes
-   Freeze=yes
-   Burnable=yes
-   FirstVersion=0.3

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

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Will-o-wisp

-   Name=Will-o-wisp
-   Image=Willowisp.png
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=Small green patch of light
-   Behaviour=Moves towards and follows [Tux](Tux "wikilink").
-   Squish=no
-   Buttjump=no
-   Freeze=no
-   Burnable=no
-   FirstVersion=

The **Will-o-wisp** is a mean little [badguy](badguy "wikilink") found
in the haunted regions of the [Forest](Forest "wikilink"). When
[Tux](Tux "wikilink") comes close, it will start to follow him slowly.
Once it reaches Tux, he will be teleported to another, possibly
dangerous part of the level. If Tux manages to get out of reach of the
*Will-o-wisp*, it will stop following him.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

== Zeekling

-   Name=Zeekling
-   Image=
-   FoundIn=[Forest](Forest "wikilink")
-   Appearance=Purple, winged critter
-   Behaviour=Flies left and right high above ground. Dives to hit
    [Tux](Tux "wikilink").
-   Squish=yes
-   Buttjump=yes
-   Freeze=no
-   Burnable=yes
-   FirstVersion=0.3

**Zeekling** is a [badguy](badguy "wikilink") found in the
[Forest](Forest "wikilink"). It flies left and right in a straight path,
usually near the top of the level. When [Tux](Tux "wikilink") is below
it, will dive down to hit him. Tux can avoid being hit by hiding
underneath platform and other solid blocks.

Should be removed from Forest World for now.

[Template:Navbox Badguys](Template:Navbox_Badguys "wikilink")

<Category:Badguy.1> <Category:Outdated> <Category:Badguy.3>
<Category:Badguy.4> <Category:Badguy.3> <Category:Badguy.3>
<Category:Badguy.1> <Category:Badguy.1> <Category:Badguy.3>
<Category:Badguy.3> <Category:Badguy.1> <Category:Badguy.3>
<Category:Badguy.3> <Category:Badguy.1> <Category:Badguy.1>
<Category:Portable> <Category:Badguy.4> <Category:Badguy.3>
<Category:Badguy.4> <Category:Badguy> <Category:Portable>
<Category:Badguy.3> <Category:Badguy.3> <Category:Badguy.1>
<Category:Badguy.4> <Category:Badguy.4> <Category:Badguy.4>
<Category:Badguy.1> <Category:Badguy.1> <Category:Badguy.2>
<Category:Badguy.4> <Category:Badguy.3> <Category:Badguy.3>
<Category:Badguy.3> <Category:Boss> <Category:Outdated>
<Category:Badguy.3> <Category:Badguy.3> <Category:Badguy.3>
