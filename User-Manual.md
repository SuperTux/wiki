# SuperTux User Manual (For v0.5.0)

![](https://github.com/SuperTux/data/blob/master/images/creatures/tux/big/stand-0.png)--------------------------------------> ![](https://github.com/SuperTux/data/blob/master/images/creatures/nolok/walk-0.png) ![](https://github.com/SuperTux/data/blob/master/images/creatures/penny/penny.png) *Help Me!*

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

Currently, there is only one worldmap availible in Story Mode: [Icy Island](https://github.com/SuperTux/supertux/wiki/Icy-Island)

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

![Level Image](https://i.imgur.com/XMaMJYQ.png)

A level is an area of an worldmap which Tux must traverse.
To "win" in a level, Tux must pass through a finish area, often marked by a set of poles.

Levels are filled with Nolok's minions, out to stop Tux's progress, and item boxes,
which provide a way for Tux to collect coins and powerups. They are also filled with puzzles, difficult jumps, coins to collect and [other objects](https://github.com/SuperTux/supertux/wiki/Objects) which Tux can interact with.

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

 - Walking into [badguys](https://github.com/SuperTux/supertux/wiki/Badguys) (see below)
 - Being crushed by moving objects
 - Being hit by thrown objects (see below)
 - Falling onto spikes or into lava
 - Falling down a pit
 
Usually, this will cause Tux to lose a [powerup]((https://github.com/SuperTux/supertux/wiki/Items)). If he has a [Fire, Ice, Air or Earth Powerup](https://github.com/SuperTux/supertux/wiki/Items), he will lose his hat. If he is only [Big Tux](https://github.com/SuperTux/supertux/wiki/Items), he will shrink. Some things will make Tux die instantly, like falling down below the level. Powerups won't help you here.

**If he is small Tux, hurting Tux will make him die!**
 
When Tux dies, it will cause him to return to the start of the level (unless he has reached a checkpoint, please see below)

But don't worry, Tux can find [items](https://github.com/SuperTux/supertux/wiki/Items) in the levels, to help him overcome these adversaries:

### [Item Boxes](https://github.com/SuperTux/supertux/wiki/Items)

Tux can find powerups, coins and other goodies in [item boxes](https://github.com/SuperTux/supertux/wiki/Items)

### Powerups

Powerups can be found in bonus blocks and on the ground. Most are eggs, which will allow you to backflip by pressing down then jumping and butt-jumping by jumping then pressing down. If you already have an egg, hitting an item box containing a powerup will give you a flower.

- Fireflowers will allow you to kill most badguys by pressing the action key, which makes Tux throw a fireball
- Iceflowers will allow you to freeze some badguys and kill some others by pressing the action key, which makes Tux throw a ball of ice. If they are frozen, you can kill most badguys by butt-jumping on them.
- Airflowers will allow you to jump further, sometimes even run faster. However, it can be difficult to do certain jumps as Air Tux.
- Earthflowers give you a light. Also, pressing the action key then down will turn you into a rock for a few seconds, which means Tux is completely invulnerable.

The more fireflowers you collect, the more fireballs you can throw at once.
The more iceflowers you collect, the more balls of ice you can throw at once.
The more earthflowers you collect, the longer you can remain as a rock

### [Badguys](https://github.com/SuperTux/supertux/wiki/Badguys)

Tux must also avoid "[Badguys](https://github.com/SuperTux/supertux/wiki/Badguys)" which are found in the level. These are Nolok's minions, and can cause Tux to get hurt.

### Other [Objects](https://github.com/SuperTux/supertux/wiki/Objects)

There are also some other [objects](https://github.com/SuperTux/supertux/wiki/Objects) that Tux can interact with.

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

## Using The Level Editor

*Level Editor documentation has not been written yet.*
