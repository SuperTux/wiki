# How to use the Level Editor

## Contents

1. [Setting up your Level](wikilink)
2. [Tilemaps and Tilegroups](wikilink)
3. [Objects and Badguys](wikilink)
4. [Using Pathnodes](wikilink)
5. [Ambient Light](wikilink)
6. [Scripting](wikilink)
7. [Setting up your Worldmap](wikilink)

---

Beginning Steps
===============

Upon opening the Level Editor you have the option to open an existing world/levelset or create one of your own.
For this Guide we will start fresh and create a new one.

Select `Create World` and enter a name and description for your new world. The description is optional so if you are unsure what to write, just skip it and select `OK`.

Now you can begin to create your first level.


Setting Up Your Level
=====================

You are now presented with a snowy background and a lot of empty space.
On the right you see the Tile Select, Object Select and your general tools and on the bottom you will find several means to edit the level sector.

Placement Tools
---------------

- ![](https://github.com/SuperTux/supertux/blob/master/data/images/engine/editor/select-mode0.png?raw=true)
  The **Red-Selection** is the most basic tool. It allows you to place tiles and Objects.
- ![](https://github.com/SuperTux/supertux/blob/master/data/images/engine/editor/select-mode1.png?raw=true)
  The **Green-Selection** allows placing multiple instaces of a tile or group of tiles by holding the Left-Mouse.
- ![](https://github.com/SuperTux/supertux/blob/master/data/images/engine/editor/select-mode2.png?raw=true)
  The **Fill-Bucket** let's you fill an area with the selected tile.
- ![](https://github.com/SuperTux/supertux/blob/master/data/images/engine/editor/rubber.png?raw=true)
  The **Eraser** simply removes tiles and objects from your level.
- ![](https://github.com/SuperTux/supertux/blob/master/data/images/engine/editor/arrow.png?raw=true)
  The **Selector** is the tool that has you select objects from your level.
- ![](https://github.com/SuperTux/supertux/blob/master/data/images/engine/editor/move-mode1.png?raw=true)
  The **Duplicator** can be used to duplicate an object on the spot.


Tiles And Tilemaps
==================

Let's make a basic level. First, select the little drop down menu labeled `Tiles` in the top right corner and select a category. In our example we chose `Snow`.

Select the tile you would like to use by clicking on it. You can select multiple tiles at once by holding the Left-mouse button and dragging your mouse over the tiles you want to select. Your selection is now displayed besides the cursor, moving across the grid. By left clicking you can place them now was many times as you want.

Note: Right clicking on a tile inside your level, you can copy it. This can save you time if you don't want to frequently switch back and forth between categories.

To make sure Tux is able to stand on the tiles you place must make sure that you are placing them on a solid tilemap. The default for newly made levels is tilemap marked `0` in the bottom bar. You can edit preexisting tilemaps by right clicking on their icon or add new ones. More infos on Objects [here](wikilink).

The default background tilemap is marked `-100` and the default foreground tilemap is marked `100`.


Objects And Badguys
===================

Now that you have build your level, let's take a look at how to place objects, such as enemies (Badguys), moving platforms, ladders, script triggers, and more. While in **Object Mode** you cannot interact with tiles!

First, select the drop down menu labeled `Objects` and select a category. The categroies `Enemies` and `Bosses` contain all aviable Badguys and Bosses you can use for your level. Upon placing an enemy you can edit some of their properties by right clicking on the enemy.

Using Doors
-----------

For a door to work properly you must first define a destination. This is done by adding another spawnpoint and naming it. Now everything left to do is enter the name of the sector and the spawnpoint you want to Tux to go when using the door.

---

Using Pathnodes
===============

Pathnodes are used to form a path for a platforms, coins, tilemaps etc. to move on.

To do this, selected the object and click with the **Pathnode tool** on the small grey circle on its top-left. If you now click anywhere else in your level, you will draw a new pathnode between it and the last node you selected. For coins and tilemaps, make sure you have `Following path` enabled!

You can find the tool under `Enviorment` in the Objects menu as a red arrow pointing to the right.

After setting up your pathnodes you can now edit each nodes property by right clicking each individual node.


Ambient Light
=============

To use things like lanterns, magic blocks or anything else that can emit light and have it shown, you must darken the
sector beforehand. Rightclick the lightbulb icon next to your tilemaps and define the sector's ambient light using RGBA.
Give each value a number between 0 (0%) and 1 (100%). For our example we set it to **R:0.5 G:0.5 B:0.8 A:1**.


Scripting
=========

Scripting allows for much more dynamic elements to be used in level creation. Scripts are written in Squirrel and
can be trigger in many different ways:

- A common one is the **Script trigger** object. It marks the area in which the script will be executed with a pink
  square and can be resized as desired. The script gets trigger when Tux enters this area.
- If you wish to execute a script immideatly after entering a sector you can do that with the **Initialization script**.
  You will find it in the settings of your sector. Mind you, the script will also be executed everytime you restard from
  a checkpoint in that sector!
- Badguys may also serve as a way to use scripts. Each badguy can be given a **Death script** that is executed upon
  the enemy's defeat. This methode is commonly used for Bosses, for example `sector.Tux.trigger_sequence("fireworks");`
  for the Yeti Boss in Icy Island.
- Other prominent methodes for scripts are buttons/switches, picking up powerups or running into Will ’O’ Wisp.

**For a list of commands that can be used in scripts, take a look at the [scripting reference](https://github.com/SuperTux/supertux/wiki/Scripting_reference).**

---

Setting Up Your Worldmap
========================

You are now presented with a tilemap that is filled with dark blue tiles, representing the ocean. We recommend you to change the tileset in your worldmap settings fro `worldmap.strf` to `ice_world.strf` as it grants much more and fleshed-out tiles.

Worldmap creation works similar to level making. The biggest differnce stems from the objects which there is only a small amount.
Instead of Badguys, Moving Platforms and Blocks you only have Leveldots, Teleports, Special Tiles and Sprite Changer.

- A **leveldot** let's you set a level which to be entered from your worldmap.
- **Teleporters** move Tux from one place to another in an instant.
- The **special tile** can be used to initiate scripts or show messages.
- **Sprite Changer** let you change Tux's sprite on the worldmap into something else after touching it, such as a sailing boat.
