Objects can be found throughout the levels in SuperTux. Some of them provide helpful items or means to progress. Others,
however, serve as obstacles Tux must avoid.

**Objects can be broken down into three categories:**
  1. [Environment](https://github.com/SuperTux/supertux/wiki/Objects#Environment)
  2. [Carriables](https://github.com/SuperTux/supertux/wiki/Objects#Carriables)
  3. [Platforms](https://github.com/SuperTux/supertux/wiki/Objects#Platforms)

---

## Environment

### Bonus Blocks

![](images/Bonusblock.png)
![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/bonus_block/purple_0.png?raw=true)

Bonus Blocks generally contain coins and sometimes powerups. Generally you cannot see what is in the block until you hit it.
They can be hit from below but also can be butt-jumped from the top as well as being hit by throwable badguys, like
[Mr. Iceblock](https://github.com/SuperTux/supertux/wiki/Badguys-Icy#Mr-Iceblock).

### Info Block

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/bonus_block/infoblock.png?raw=true)

Info Blocks can give valuable information about the level ahead. They can be hit from below or butt-jumped from on top. 

### Wooden Crates

![](https://github.com/SuperTux/supertux/blob/master/data/images/tiles/blocks/brick0.png?raw=true "Normal Crate")
![](https://github.com/SuperTux/supertux/blob/master/data/images/tiles/blocks/brick1.png?raw=true "Snowy Crate")
![](https://github.com/SuperTux/supertux/blob/master/data/images/tiles/blocks/brick2.png?raw=true "Spooky Crate")
![](https://github.com/SuperTux/supertux/blob/master/data/images/tiles/blocks/brick3.png?raw=true "Heavy Crate")

Same as Bonus Blocks, Wooden Crates contain coins and can be hit by the same means. Unlike Bonus Blocks they commonly do
not contain anything and simply break after hitting them as Big Tux.

Heavy Crates are a slightly different as these are metal reinforced crates which require stronger force! They can only be
broken by detonating a bomb next to it, by large Crusher variants, like Krosh, or using Earth Tux's rock ability.

### Checkpoint

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/resetpoints/bell-m.png?raw=true)

Checkpoints are represented by golden bells that when rang will allow you to spawn back there if you die.

### Door

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/door/door-0.png?raw=true)

Doors can transport Tux to another part of a level. Press the up key whilst in front of one to use it. Sometimes there will
be a door there to go back, but not always. 

### Switches

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/switch/switch-0.png?raw=true "Lever")
![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/pushbutton/pushbutton-0.png?raw=true "Pushbutton")

Switches can either be levers or buttons. Levers work by pressing the up key and buttons by jumping on them. They both run
scripts, which can change something in the level, like moving a platform or activate a sequence. In most cases, it will help
Tux making progress. Sometimes there will be two signs of the same colour at the switch and the thing that gets changed by
the script.

### Rublight

Rublights are commonly used in very dark areas. Stepping on one will generate light for short amount of time. Badguys can
activate rublights, too.

### Magic Block

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/magicblock/magicblock.png?raw=true "Inactive Magic Block")

Magic Blocks are non solid blocks that only turn solid when illuminated by a light of the same colour.

### Weak Blocks

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/weak_block/straw.png?raw=true "Straw")
![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/weak_block/meltbox.png?raw=true "Meltbox")

Weak Blocks, such as Straw or Meltboxes are solid blocks that can be destroyed by throwing a fireball as Fire Tux or detonating a
[Mr. Bomb](https://github.com/SuperTux/supertux/wiki/Badguys-Misc#Mr-Bomb) or similar close to it.

---

## Carriables

### Rock

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/rock/rock.png?raw=true)

Rocks can be carried by holding the action key. They can allow Tux to get over new obstacles by stacking them or to crush
badguys by dropping the rock on their head.

### Trampolines

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/trampoline/trampoline1-0.png?raw=true "Portable Trampoline")
![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/trampoline/trampoline2-0.png?raw=true "Fixed Trampoline")
![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/rusty-trampoline/rustytrampoline1.png?raw=true "Rusty Portable Trampoline")

Trampolines are available fixed and portable and sit on the ground or on walls. They can be jumped on to help Tux reach
new heights or push him around. Portable ones can be moved with the action key. There are also ones that rust and break
after a few jumps.

### Lantern

![](https://github.com/SuperTux/data/blob/master/images/objects/lantern/lantern-1.png?raw=true)

Lanterns can be carried like rocks. They are also a good light source and can activate
[Magic Blocks](https://github.com/SuperTux/supertux/wiki/Objects#Magic-Blocks) of the same colour solid.

Catching a [Will-o-wisps](https://github.com/SuperTux/supertux/wiki/Badguys-Forest#Will-o-wisp) with an empty
lantern results in the lantern lighting up in the colour of the wisp.

---

## Platforms

### Moving Platforms

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/flying_platform/flying_platform-0.png?raw=true)

Moving Platforms take Tux to and from places. Some are always moving, some move when Tux gets on them and others need to be started
by a switch or a script. They come in varying forms and sizes.

### Unstable Tiles

![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/unstable_tile/snow-0.png?raw=true "Snow Variant")
![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/unstable_tile/normal.png?raw=true "Brick Variant")
![](https://github.com/SuperTux/supertux/blob/master/data/images/objects/skull_tile/skull.png?raw=true "Skull Variant")

An Unstable Tile is an object that will fall down a few seconds after standing on them. A similar object, the Skull Tile, will
only begin to fall if standing on them for too long. Both objects respawn after five seconds.
