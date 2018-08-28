![](https://github.com/SuperTux/data/blob/master/images/creatures/tux/big/stand-0.png)________________________________________ ![](https://github.com/SuperTux/data/blob/master/images/creatures/nolok/walk-0.png) ![](https://github.com/SuperTux/data/blob/master/images/creatures/penny/penny.png) 

SuperTux is a side-scrolling 2D platformer featuring Tux, the Linux mascot. Over the course of the game, Tux will have to make his way through many different levels, in order to reach and rescue Penny, who was captured by evil Nolok.

This file should help players to understand the features of the game at a user level (How to play, not how it works...)

See the [old wiki's user manual](http://supertux.lethargik.org/wiki/User_Manual) to see the (now outdated) source of some of this information.

## Getting Started

 - Download a copy of the game [here](https://supertuxproject.org/download.html)
 - Start it up, after installing it
 - Use the up/down arrow keys or the mouse to select "Start Game" at the main menu
 - Press the Enter key, or Left Click with the mouse
 - Press the Enter key, or click again, this time on "Story Mode"
 
After this, the intro cutscene should begin. Watch it, and then continue onto the section labelled "Gameplay" in this document.

## Gameplay

Oh no! Nolok has captured Tux's girlfriend, Penny. It is now your responsibility to control Tux, and save Penny.

*Disclaimer: It is not currently possible to save Penny, since the game is not complete.*

In order to do this, you need to understand how to play the game. This section of the Manual should help you.

### Worldmaps

![Worldmap Image](https://i.imgur.com/JuNXmRf.jpg)

A worldmap is an island or a collection of islands which Tux must explore in search of Penny (or for some other goal). They feature levels which appear as dots/icons connected by paths.

Currently, there is only one worldmap availible in Story Mode: [Icy Island](Icy-Island)

In later releases, more worldmaps will feature.

Some other worldmaps which you can play are:

 - Forest World (development island)
 - The Halloween Island (Spooky)
 - Bonus Islands 1-3
 - All the addons

Check the Contrib Levels menu:
Start Game > Contrib Levels

There are also worldmaps availible in addons. Please see the section labelled "Addons" below for more information.

### Levels

![Level Image](images/Screenshot_Via-Nostalgica.png)

A level is an area of an worldmap which Tux must traverse.
To "win" in a level, Tux must pass through a finish area, often marked by a set of poles.

Levels are filled with Nolok's minions, out to stop Tux's progress, and item boxes,
which provide a way for Tux to collect coins and powerups. They are also filled with puzzles, difficult jumps, coins to collect and [other objects](Objects) which Tux can interact with.

First, though, you need to understand the controls:

### Controls

Control |	Default mapping |	Description
--------|-----------------|--------------------
Left    |	Cursor Left     |	Makes Tux walk left
Right 	| Cursor Right    | 	Makes Tux walk right
Up 	    | Cursor Up       |	Enter door, activate switch
Down    |	Cursor Down     |	Duck
Jump 	  | Spacebar        |	Makes Tux jump. Hold down longer to jump higher.
Action  |	Left Control    |	Varies; actions are explained below. 

The "P" and "Escape" keys can be used to pause the game.

To change the controls, go to Options > Setup Keyboard.
Select the control you wish to change, and click the key you wish to assign it to.

Unfortunately, it's not as simple as just running and jumping freely through levels:

### Getting Hurt

Tux can get hurt in a number of ways:

 - Walking into [badguys](Badguys) (see below)
 - Being crushed by moving objects
 - Being hit by thrown objects (see below)
 - Falling onto spikes or into lava
 - Falling down a pit
 
Usually, this will cause Tux to lose a [powerup](Items). If he has a [Fire, Ice, Air or Earth Powerup](Items), he will lose his hat. If he is only [Big Tux](Items), he will shrink. Some things will make Tux die instantly, like falling down below the level. Powerups won't help you here.

**If he is small Tux, hurting Tux will make him die!**
 
When Tux dies, it will cause him to return to the start of the level (unless he has reached a checkpoint, please see below)

But don't worry, Tux can find [items](Items) in the levels, to help him overcome these adversaries:

### [Item Boxes](Items)

Tux can find powerups, coins and other goodies in [item boxes](Items)

### Powerups

Powerups can be found in bonus blocks and on the ground. Most are eggs, which will allow you to backflip by pressing down then jumping and butt-jumping by jumping then pressing down. If you already have an egg, hitting an item box containing a powerup will give you a flower.

- Fireflowers will allow you to kill most badguys by pressing the action key, which makes Tux throw a fireball
- Iceflowers will allow you to freeze some badguys and kill some others by pressing the action key, which makes Tux throw a ball of ice. If they are frozen, you can kill most badguys by butt-jumping on them.
- Airflowers will allow you to jump further, sometimes even run faster. However, it can be difficult to do certain jumps as Air Tux.
- Earthflowers give you a light. Also, pressing the action key then down will turn you into a rock for a few seconds, which means Tux is completely invulnerable.

The more fireflowers you collect, the more fireballs you can throw at once.
The more iceflowers you collect, the more balls of ice you can throw at once.
The more earthflowers you collect, the longer you can remain as a rock

### [Badguys](Badguys)

Tux must also avoid "[Badguys](Badguys)" which are found in the level. These are Nolok's minions, and can cause Tux to get hurt.

### Other [Objects](Objects)

There are also some other [objects](Objects) that Tux can interact with.

## Addons

Addons are sets of levels provided by the community. To install and play a new addon: 

 - Select "Add-ons" on the main menu
 - Click on the addon you wish to install
 - Watch as it downloads
 - Go back to the Main Menu (by pressing Escape, or selecting Back)
 - Go into Start Game > Contrib Levels
 - Select the new item(s) in this list, which you wish to play

These addons are not managed by The SuperTux Team, so please do not register your issues regarding them on the SuperTux/supertux repository.
You *may* be able to get help by making an issue [here](https://github.com/SuperTux/addons/issues)

By default the game searches for new addons in the SuperTux Team's addon repo [here](https://github.com/SuperTux/addons).
If you wish to submit a new addon to the repo, please make an issue or pull request there.
If you would rather change the addon repo which the game looks for new addons in, you can start the game with the repository-url argument specified: ```supertux2 --repository-url URL```
**WARNING: THIS IS NOT RECOMMENDED BY THE SUPERTUX TEAM**


User Manual
===========

[s=This user manual is by no means error free, nor is it complete yet.
If you have anything to add, just click an “Edit” link and add some
text](Template:Attention "wikilink")

Introduction
------------

![Rated FUN](images/RATEDFUN.png "Rated FUN")

![](images/Logo.png "Logo.png")

SuperTux is a side-scrolling 2D platformer featuring
[Tux](Tux "wikilink"), the Linux mascot, but it's otherwise entirely
unrelated to Linux. Over the course of the game, Tux will have to make
his way through many different levels, in order to reach and rescue
[Penny](Penny "wikilink"), who was captured by evil
[Nolok](Nolok "wikilink").


Controls
--------

![](images/Littletrees.png "Littletrees.png")

SuperTux is played with either the keyboard or any game controller
recognized by the operating system. The following list shows all
controls needed to play the game, along with their default keys. Note
that all of the controls can be configured in-game.

  Control   Default mapping   Description
  --------- ----------------- -----------------------------------------------------------------
  Left      Cursor Left       Makes Tux walk left
  Right     Cursor Right      Makes Tux walk right
  Up        Cursor Up         Enter door, activate switch
  Down      Cursor Down       Duck
  Jump      Spacebar          Makes Tux jump. Hold down longer to jump higher.
  Action    Left Control      Varies; all actions are [explained below](#Actions "wikilink").

  : Controls


Powerups
--------

To help Tux in his quest to rescue Penny, various powerups have been
placed throughout the levels. Some are in plain view, but most are
hidden in bonus blocks:

![Bonus Block](images/Bonusblock.png "Bonus Block")

When Tux bumps a bonus block from below, he will either collect a coin
or the bonus block will release one of several powerups:

  Pic.                                         Name                                    Effect
  -------------------------------------------- --------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Coin-0.png "Coin-0.png")                 Coin                                    **SuperTux 0.1:** Collect 100 coins to gain an extra life. **SuperTux 0.3:** Every time Tux dies, he will restart at the last firefly he activated.
  ![](images/Egg.png "Egg.png")                       Egg                                     Makes Tux grow. He can then smash wooden boxes with his head and perform a *backflip* (see below).
  ![](images/Fire_flower-0.png "Fire_flower-0.png")   [Fireflower](Fireflower "wikilink")     Only released from bonus blocks when Tux has already picked up an Egg. This will give Tux the power to throw fireballs. In SuperTux 0.1 you can shoot more than two at a time. In SuperTux 0.3 you can shoot them at once as many as you collected.
  ![](images/Ice_flower.png "Ice_flower.png")         [Iceflower](Iceflower "wikilink")       Similar to the Fireflower, but shoots iceballs instead of fireballs. If an enemy is hit, it will be frozen. Does not work on most snow and ice enemies. **(unstable)**
  ![](images/Air_flower.png "Air_flower.png")         [Airflower](Airflower "wikilink")       Allows bigger jumps. **(unstable)**
  ![](images/Earth_flower.png "Earth_flower.png")     [Earthflower](Earthflower "wikilink")   Makes a small light appear from Tux's helmet.. **(unstable)**
  ![](images/1up.png "1up.png")                       Tux Doll                                Ejected from the bonus block and needs to be caught before falling off the screen. If Tux manages to catch it, he is awarded an extra life **(SuperTux 0.1)** or 100 coins **(SuperTux 0.3)**.
  ![](images/Star-0.png "Star-0.png")                 Star                                    Gives Tux invincibility to most hazards for a short amount of time.


Actions
-------

### Running (SuperTux 0.1)

Press the Action button and keep running in the same direction. Tux will
go faster and jump higher. If you release the Action button while
running, Tux will walk at a slower pace again.

### Walking (SuperTux 0.3)

Normally, when you keep running in the same direction, Tux will go
faster and jump higher. If you press the Action button while running,
Tux will walk at a slower pace again.

### Fireballs

After picking up the [Fireflower](Fireflower "wikilink"), Tux will throw
fireballs when the Action button is pressed. Most badguys can be knocked
off the screen by hitting them with a fireball. Also, special “Straw”
blocks can be set on fire by hitting them with a fireball, revealing
areas with special items or opening a shortcut **(SuperTux 0.3 only)**.

### Iceballs (SuperTux 0.3.1 and later)

Similar to the Fireballs, but objects which they hit freeze. It only
works on “MrBomb”, "Jump ", “Spiky”, “Fish”, “Haywire”. They are also
frozen when they are hit by a falling “Stalactite”.

### Butt Stomp (SuperTux 0.3.3 and later)

Only Big and Fire Tux have this ability. When in the air, press the Duck
key to perform a Butt Stomp. Tux can use this ability to break wooden
crates from above and defeat certain badguys that are not harmed by a
normal jump.

### Backflip (SuperTux 0.3 only)

Only Big and Fire Tux have this ability. Hold down the Duck key, then
press Jump to make Tux do a backflip. This will make him jump as high as
he would when running, which is very useful in places where there's not
enough space to run. Note that in 0.3.0, but not 0.3.1, Fire Tux will
lose his hat when doing a backflip.

### Carrying Objects

![](images/needrock.png "fig:needrock.png") Some objects Tux comes across can
be picked up and carried around. This includes a squished [Mr.
IceBlock](MrIceBlock "wikilink") (**SuperTux 0.1** and **SuperTux
0.3**), a [Rock](Rock "wikilink") (**SuperTux 0.3**), a
[Trampoline](Trampoline "wikilink") (**SuperTux 0.3**) and a [Mr.
Bomb](MrBomb "wikilink") (**SuperTux 0.3.3**)

To pick up a portable object, hold down the Action button and walk into
the object. Tux will then carry the object as long as the Action button
is held down.


Badguys
-------

[[Badguys](Badguys "wikilink")](Template:See_also "wikilink")

![](images/Left-1.png "fig:Left-1.png")
![](images/Mriceblock_new.png "fig:Mriceblock_new.png")
![|right](images/Spiky.png "fig:|right") ![](images/Snowsnail.png "fig:Snowsnail.png")

Over the course of the game, Tux will encounter lots of different
enemies – some easy to avoid, some tough to get past. When Tux touches a
badguy, he will either lose a Powerup or – if no powerups are left – get
thrown off the screen. Most, but not all, of the easier enemies can
easily be knocked out by jumping on their head, but take care: As a rule
of thumb, enemies with a pointy top cannot be squished, and if he tries,
it will hurt him. Fireballs can take out most badguys, but beware: Some
badguys are even immune to those.

For more information on the occurring badguys, please take a look at the
[Badguys page](Badguys "wikilink").


Special Game Objects
--------------------

### Bells

![](images/bell-r.png "fig:bell-r.png") When Tux gets thrown off the screen, he
will normally have to start the current level over from the beginning.
There is one exception, though: Most levels contain one or more bells.
When Tux activates a Bell by touching it, he won't have to restart the
level from the beginning, but will instead restart from the last
activated bell - as long as he has at least one life **(SuperTux 0.1)**
or 25 coins **(SuperTux 0.3)** left. In SuperTux 0.1, bells are
invisible, but don't need to be touched to use- only passed by.

### Secret Blocks

![](images/Empty.png "fig:Empty.png") Secret blocks are special blocks that
appear out of thin air when Tux jumps in certain places.

They can then be stepped on to reach higher places, e.g. a secret area
or a shortcut.

appart from that they do nothing, you can stand on them.

### Doors (SuperTux 0.3 only)

![](images/Door-0.png "fig:Door-0.png") Press the Up key to enter a door. Tux
will be transported to another place in the level.


### Switches (SuperTux 0.3 only)

![](images/Left-0.png "fig:Left-0.png") Switches come in two different styles:
Levers and panels.

Press the Up key to activate a switch. This might open blocked paths,
start platforms, turn off a stream of air, etc.

Most switches are near the object they affect. Objects that are farther
away from their switch often have a colored sign next to them. A sign of
the same color can then be found next to the corresponding switch.

### Platforms (SuperTux 0.3 only)

![](images/Flying_platform-0.png "Flying_platform-0.png")

Over the course of his adventure, Tux comes across a variety of moving
Platforms.

Some are mounted on rails, some swim in water, some even float freely
through the air.

While some Platforms just move on their own, most Platforms will only
move when Tux steps on them.

Some might also require Tux to visit another part of the level and
activate a Switch first. When this is the case Tux will most probably
find a helpful sign next to the Platform.

### Info Blocks (SuperTux 0.3 only)

![](images/Infoblock.png "Infoblock.png")

Levels that introduce new game elements often contain Info Blocks.

Info Blocks can be bumped from below to display helpful text that
introduces a certain element.

When you activate an Info Block, the game will pause and you can use the
Up and Down buttons to scroll through the text. Press the Menu button to
resume the game.

they are really useful. make sure to bop one if you see it.

### Trampolines (SuperTux 0.3 only)

![](images/trampoline1-0.png "fig:trampoline1-0.png")
![](images/trampoline2-0.png "fig:trampoline2-0.png")

Trampolines come in two flavors: A stationary version, which looks a bit
like a mushroom and a portable version, which looks like a large spring.
For information about carrying them around, see section [Carrying
Objects](#Carrying_Objects "wikilink").

Normally, Tux will only bounce up and down a small amount on a
Trampoline. To make him jump higher, hold down the jump button when
landing on the Trampoline.


### Magic Blocks and Lanterns (SuperTux 0.3 only)

Magic Blocks look pale and are not solid unless Tux brings a carry-able
Lantern that is the same color as the block near the block. Lanterns
also double as a light source which allows Tux to see in dark areas.

### Wind (SuperTux 0.3 only)

The Wind transports Tux to another location. Levels with Wind: “Find the
Bigger Fish!”, “Treasure in the skies”, “Tree sheets in the wind” and “A
Village in the Forest”.


Further Reading
---------------

Have fun browsing the SuperTux wiki. You can find lots of in-depth
information about most objects in the game here.

If you have paid for SuperTux, you have been ripped off. Supertux is
available for free download at
[Download/Installation](Download "wikilink").

[Category:For Users](Category:For_Users "wikilink")
