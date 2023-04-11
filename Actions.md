### General
- [Jumping](#jumping)
- [Running](#running)
- [Ducking](#ducking)
- [Carrying](#carrying)
- [Buttjump](#buttjump)
- [Backflip](#backflip)
- [Swimming](#swimming)

### Power-Ups
- [Egg](#egg)
- [Fire Flower](#fire-flower)
- [Ice Flower](#ice-flower)
- [Air Flower](#air-flower)
- [Earth Flower](#earth-flower)
- [Star](#star)
- [Tux Doll](#tux-doll)

### Proposed
- [Super-Butt-Jump](#super-butt-jump)
- [Blowflyer](#blowflyer)
- [Sliding](#sliding)
- [Flapping](#flapping)
- [Diving](#diving)


General
=======

Jumping
-------

![](https://github.com/ahm8076/wiki/blob/master/images/jump.gif)

Jumping is the most basic ability present in platformers. A jump will allow Tux to reach
four tiles in height. A running jump reaches five tiles in height.

Running
-------

![](https://github.com/ahm8076/wiki/blob/master/images/run.gif)

Running is an automatic action that gets activated when Tux is walking in the same direction
for a certain amount of time.

Milestone 1 used a dedicated RUN key, since Milestone 2 it is automatic.

Ducking
-------

![](https://github.com/ahm8076/wiki/blob/master/images/duck.gif)

Ducking can be used to slide down small, one tile high holes as big Tux or to avoid projectiles
which are shot one tile above ground.

Carrying
--------

![](https://github.com/ahm8076/wiki/blob/master/images/carry.gif)

Walking into or standing next to [carriable objects](https://github.com/SuperTux/supertux/wiki/Objects#Carriables)
while holding the *ACTION* key allows Tux to carry the object around. Releasing the *ACTION* key while walking results
in Tux throwing the object. Doing so while standing still results in Tux simply dropping the object right next to him.

Buttjump
--------

![](https://github.com/ahm8076/wiki/blob/master/images/buttjump.gif)

A buttjump allows Tux to crush boxes from above and destroy some badguys that cannot be harmed
by a normal jump. To perform the buttjump, jump and hold down the *DOWN* key while in the air.

It takes Tux a small amount of time to jump back onto his feet upon touching the ground.

Backflip
--------

![](https://github.com/ahm8076/wiki/blob/master/images/backflip.gif)

The backflip is a special jump which gives Tux some extra height compared to a normal jump.
It is performed while ducking and pressing the *JUMP* key.

Swimming
--------

![](https://github.com/ahm8076/wiki/blob/master/images/swim.gif)

When in water, Tux can move and turn in all directions with his movement speed being momentum based.

Instead of jumping, Tux will gain a boost which lets him swim much faster.

---

Power-Ups
=========

Egg
---

![](https://github.com/SuperTux/supertux/blob/master/data/images/powerups/egg/egg.png?raw=true)

The **egg** is the first and most vital power-up Tux encounters on his journey,
turning him into Big Tux. He now can take one more hit before dying, break crates
by jumping against them and perform actions such as the buttjump and backflip.

Fire Flower
-----------

![](https://github.com/SuperTux/supertux/blob/master/data/images/powerups/fireflower/fire_flower-0.png?raw=true)

The **fire flower** gives Tux the ability to spit bouncing fire bullets that kill
most badguys in his path.

Any subsequent fire flower that Tux takes increase the amount of fire bullets that
can be on the screen at the same time, but do not increase the amount of hits Tux
can take.

Ice Flower
----------

![](https://github.com/SuperTux/supertux/blob/master/data/images/powerups/iceflower/ice_flower-0.png?raw=true)

The **ice flower** gives Tux the ability to shoot ice bullets. These will not bounce
like fire bullets, but will shoot out in a straight path towards the enemy. When the
ice bullet hits an enemy it will freeze him for a short time, if the enemy is actually
freezable.

Any subsequent ice flower that Tux takes increase the amount of ice bullets that can
be on the screen at the same time, but do not increase the amount of hits Tux can take.

- Perhaps the ice bullet could freeze water, bouncing across the
  surface of a body of the aforesaid liquid and freezing the surface
  of the **one block** it touches, and maybe one block either side of
  it. I got the idea from water -&gt; ice on the User Ideas page.

Air Flower
----------

![](https://github.com/SuperTux/supertux/blob/master/data/images/powerups/airflower/air_flower-0.png?raw=true)

The **air flower** grants Tux the ability to jump much higher and run much faster.
Additionally, holding down the *JUMP* key after a jump will allow Tux to glide for
a couple of seconds.

Any subsequent air flower that Tux takes increase the amount of time Tux can glide,
but do not increase the amount of hits Tux can take.

Earth Flower
------------

![](https://github.com/SuperTux/supertux/blob/master/data/images/powerups/earthflower/earth_flower-0.png?raw=true)

The **earth flower** gives Tux the ability to turn into a stone version of himself for a
short amount of time. When turned to stone, Tux is invulnerable to all types of damage,
but cannot move during that time.

In dark areas the earth flower will also provides a small cone of light.

Any subsequent earth flower that Tux takes increase the amount of time Tux will remain in
his stone form, but do not increase the amount of hits Tux can take.

Star
----

![](https://github.com/SuperTux/supertux/blob/master/data/images/powerups/star/star-0.png?raw=true)

A white **star** will turn Tux invincible for about 14 seconds, visualized by white sparks
surrounding him.

Tux Doll
--------

![](https://github.com/SuperTux/supertux/blob/master/data/images/powerups/1up/1up.png?raw=true)

The **Tux Doll** grants Tux 100 extra coins.

Before the life-system was discarded in Milestone 2, the Tux Doll granted one extra life.

---

Proposed Abilities
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

The **blowflyer** or **BalloonTux** action should be a temporary limited action in
which Tux fills his body with air (helium?!) and is thus able to fly for a short time,
i.e. as long as he can go without breathing. The end of the flight should be announced
by Tux changing color and catching for air.

Perhaps there could be a hidden “pump” in each level, which tux could pump himself up with.

Sliding
-------

Tux will be able to make use of smooth terrain by using the slide action. By using the
slider action Tux will jump on its belly and thus slide speedy down the hill. Terrain
that is formed like a ramp should allow him to make huge jumps, which would be impossible
without the slide action. While sliding downhill Tux shall be invulnerable by normal enemies,
however special enemies with spikes or so, might still be able to stop him.

Exact details on how the sliding will work have to be worked out, but it might get a rather
central role in gameplay.

![](images/slider.jpg)

![](images/slider2.png)

Somewhat related, you could have icy platforms that when running on it is much harder to
stop/change-direction (i.e. you could slide off the edge accidently) that require you to
be extra careful.. these could appear on later harder levels. If these aren't flat, you
get what is shown in the above picture, which you could slide down instead.

We'd probably need tile-based friction to make this work well. Holding the *DOWN* key while
moving above a certain speed (or on a slope) will reduce Tux's friction by a large factor (4?)
and make him slide as illustrated in the above picture. He'll be able to kill/stun certain
enemies this way, but some (like the spiky ones) will damage and stop him.

Flapping
--------

![](images/Flapping.png)

Once in the air, Tux should be allowed to flap with his wings. They are not enough to let him fly,
but should allow him to get some additional air-time (like a small double-jump).

- While not as a core ability, this could very well be turned into
  how Tux glides with the new air flower costume designs.

Diving
------

When jumping from a great height, Tux should have his beak facing down, like a dive. It would work
well with the swim ability.
