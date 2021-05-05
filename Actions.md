### General
- [Jumping](#jumping)
- [Running](#running)
- [Ducking](#ducking)
- [Carrying](#carrying)
- [Buttjump](#buttjump)
- [Backflip](#backflip)
- [Swimming](#swimming)

### Power-Ups
- [Fireflower](#fireflower)
- [Iceflower](#iceflower)
- [Airflower](#airflower)
- [Earthflower](#earthflower)
- [Star](#star)
- [Tuxdoll](#tuxdoll)

### Proposed
- [Super-Butt-Jump](#super-butt-jump)
- [Blowflyer](#blowflyer)
- [Slider](#slider)
- [Flapping](#flapping)
- [Dive](#dive)


General
=======

Jumping
-------

Jumping is the most basic ability present in platformers. A jump will
allow Tux to reach four tiles in height.

Running
-------

Running is an automatic action that gets activated when Tux is walking
in the same direction for a certain amount of time. When Tux is
running he is able to jump five tiles high instead of just four.

Milestone 1 used a dedicated run button, since Milestone 2 it's automatic.

Ducking
-------

Ducking can be used to slide down small, one tile high holes as big Tux or
to avoid projectiles which are shot one tile above ground.

Carrying
--------

Walking into or standing next to [carriable objects](https://github.com/SuperTux/supertux/wiki/Objects#Carriables)
while holding the ACTION key allows Tux to carry the object around. Releasing the ACTION key while walking results
in Tux throwing the object. Doing so while standing still results in Tux simply dropping the object right next to him.

Buttjump
--------

The buttjump is an ability that lets Tux crush boxes from above
and destroy some badguys that cannot be harmed by a normal jump. It is
performed by jumping up into the air and then pressing the DOWN key
while in the air. It takes Tux a small amount of time to jump back onto his feet to get back to normal

Backflip
--------

The backflip is a special jump which gives Tux some extra height
compared to a normal jump. It requires that Tux comes to a full stop
and turns around.

Swimming
--------

When in water, Tux can move and turn in all directions with his movement
speed being momentum based.

Instead of jumping, Tux can gain a boost which lets him swim much faster.

---

Power-Ups
=========

Fireflower
----------

The behaviour of the **fireflower** is that it gives Tux the ability
to spit bouncing fire bullets. Most badguys are killed when being
struck by a fire bullet.

Any subsequent fireflowers that Tux takes increase the amount of fire
bullets that can be on the screen at the same time, but do not
increase the amount of hits Tux can take.

Iceflower
---------

The **iceflower** will give Tux the ability to shoot ice bullets. Ice
bullets will not bounce like fire bullets, but will shoot out in a
straight path towards the enemy. When the ice bullet hits an enemy it
will freeze him for a short time, if the enemy is actually freezable.

Any subsequent iceflowers that Tux takes increase the amount of ice
bullets that can be on the screen at the same time, but do not
increase the amount of hits Tux can take.

- Perhaps the ice bullet could freeze water, bouncing across the surface
  of a body of the aforesaid liquid and freezing the surface of the
  **one block** it touches, and maybe one block either side of it. I got
  the idea from water -&gt; ice on the User Ideas page.

Airflower
---------

The **airflower** grants Tux the ability to jump much higher and run
much faster. Additionally, holding down the JUMP key after a jump will
allow Tux to glide for a couple of seconds.

Any subsequent airflower that Tux takes increase the amount of time
Tux can glide, but do not increase the amount of hits Tux can take.

Earthflower
-----------

The **earthflower** will give Tux the ability to turn into a stone version
of himself for a short amount of time. When turned to stone, Tux is
invulnerable to all types of damage, but cannot move during that.

In dark areas the eartflower will also provides a small cone of light.

Any subsequent earthflower that Tux takes increase the amount of time
Tux will remain in his stone form, but do not increase the amount of
hits Tux can take.

Star
----

An white **star** will turn Tux invincible for about 14 seconds, visualized
by white sparks surrounding him.

Tuxdoll
-------

The **Tuxdoll** grants Tux 100 extra coins.

Before Milestone 2, a Tuxdoll granted one extra life.

---

Proposed abilities
==================

Super-Butt-Jump
---------------

1.  Player moves Tux to a high position on the map
2.  Player jumps from the ledge
3.  Player presses 'down'
4.  Tux does some acrobatic movement to get into the 'butt-position'
5.  Tux then falls down back to the ground, butt first with increasing speed,
    due to the higher altitude he will change to Super-Butt-Jump-mode
6.  When smashing on the ground nearby enemies might be turned upside down,
    rendering them unmovable or killing them (might depend on the type of
    enemy and of the type of ground)
7.  It takes Tux a small amount of time to jump back onto his feet to get back to normal

Blowflyer
---------

![](images/Blowflyer.png)

The **blowflyer** or BalloonTux action should be a temporary limited
action in which Tux fills his body with air (helium?!) and is thus
able to fly for a short time, i.e. as long as he can go without
breathing. The end of the flight should be announced by Tux changing
color and catching for air.

Perhaps there could be a hidden “pump” in each level, which tux could
pump himself up with.

Slider
------

Tux will be able to make use of smooth terrain by using the slide
action. By using the slider action Tux will jump on its belly and thus
slide speedy down the hill. Terrain that is formed like a ramp should
allow him to make huge jumps, which would be impossible without the
slide action. While sliding downhill Tux shall be invulnerable by
normal enemies, however special enemies with spikes or so, might still
be able to stop him.

Exact details on how the sliding will work have to be worked out, but
it might get a rather central role in gameplay.

![](images/slider.jpg)

![](images/slider2.png)

Somewhat related, you could have icy platforms that when running on it
is much harder to stop/change-direction (i.e. you could slide off the
edge accidently) that require you to be extra careful.. these could
appear on later harder levels. If these aren't flat, you get what is
shown in the above picture, which you could slide down instead.

We'd probably need tile-based friction to make this work well. Holding
“duck” while moving above a certain speed (or on a slope) will reduce
Tux's friction by a large factor (4?) and make him slide as
illustrated in the above picture. He'll be able to kill/stun certain
enemies this way, but some (like the spiky ones) will damage and stop
him.

Flapping
--------

![](images/Flapping.png)

Once in the air, Tux should be allowed to flap with
his wings. They are not enough to let him fly, but should allow him to
get some additional air-time (like a small double-jump).

Dive
----

When jumping from a great height, Tux should have his beak facing
down, like a dive. It would work well with the swim ability.
