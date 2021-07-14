# How to use the Level Editor

## Contents

1. [Setting up your Level](wikilink)
2. [Tilemaps and Tilegroups](wikilink)
3. [Objects and Badguys](wikilink)
4. [Scripting](wikilink)
5. [Setting up your Worldmap](wikilink)

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

- The **Red-Selection** is the most basic tool. It allows you to place tiles and Objects.
- The **Green-Selection** allows placing multiple instaces of a tile or group of tiles by holding the Left-Mouse.
- The **Bucket** let's you fill an area with the selected tile.
- The **Erasor** simply removes tiles and objects from your level.
- The **Selector** is the tool that has you select objects from your level.
- The **Duplicator** can be used to duplicate an object on the spot.


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


Scripting
=========


Setting Up Your Worldmap
========================

You are now presented with a tilemap that is filled with dark blue tiles, representing the ocean. We recommend you to change the tileset in your worldmap settings fro `worldmap.strf` to `ice_world.strf` as it grants much more and fleshedout tiles.

Worldmap creation works similar to level making. The biggest differnce stems from the objects which there is only a small amount.
Instead of Badguys, Moving Platforms and Blocks you only have Leveldots, Teleports, Special Tiles and Sprite Changer.

- A leveldot let's you set a level which to be entered from your worldmap.
- Teleports move Tux from one place to another in an instant.
- A special tile can be used to initiate scripts or show messages.
- The Sprite Changer let's you change Tux's sprite on the worldmap into something else, like a boat.
