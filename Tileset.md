SuperTux tilemaps are composed from tiles, little 32x32 pixel wide images. These tiles are defined
in an [S-Expression](https://en.wikipedia.org/wiki/S-expression) based file, located under `data/images/tiles.strf`.

These tilesets are included into the level by a `tiles` and `tilegroup` entry.

# Contents

1. [Introduction](#introduction)
2. [Tile Attributes](#tile-attributes)
   * [Attribute Combinations](#attribute-combinations)
   * [Deprecated Attributes](#deprecated-attributes)
3. [Tile Datas](#tile-datas)
   * [Slope Types](#slope-types)
4. [Adding Your Own Tiles](#adding-your-own-tiles)
   * [Initial Preparations](#step-1-initial-preparations)
   * [Adding Tiles](#step-2-adding-tiles)
   * [Adding Tilegroups](#step-3-adding-tilegroups)
5. [Special Tiles](#special-tiles)
   * [Adding Objects As Tiles](#adding-objects-as-tiles)

Introduction
============

A general `tile` contains an ID number, an images path and an attribute to determine its use
(e.g. a tile being solid, a slope, slippery etc).

A `tilegroup` describes the collection of several tiles usually sorted by themes. For example,
all snow-themed tiles are sorted into a `snow` tilegroup while all forest-themed tiles are sorted
into a `forest` tilegroup.

Examples
--------

An example of a simple solid tile looks like this:

```
(tiles
  (width 1)
  (height 1)
  (ids 1)
  (attributes 1)
  (images "tiles/[tilegroup]/[tile].png")
)
```

The `attribute` defines the tile's properties. In this example we set it to 1 which makes this
tile solid so Tux can stand on it.

More on tile attributes can be read [here](#tile-attributes).

---

For an animated tile you can define its animation speed with an `FPS` value:

```
(tiles
  (width 1)
  (height 1)
  (ids 2)
  (fps 12)
  (attributes 512)
  (images "tiles/[tilegroup]/[animatedtile]-0.png"
          "tiles/[tilegroup]/[animatedtile]-1.png"
          "tiles/[tilegroup]/[animatedtile]-2.png"
          "tiles/[tilegroup]/[animatedtile]-3.png")
)
```

---

It is also possible to extract parts of bigger images to create tiles:

```
(tiles
  (width 3)
  (height 2)
  (ids
    3 4 5 6
    7 8 9 0)
  (attributes
    0 0 0 0
    1 1 1 0)
  (image "tiles/[tilegroup]/[multipletiles].png")
)
```

---

For a tile that looks one way in editor and other way in game, you can set the images separately:

```
(tiles
  (width 1)
  (height 1)
  (ids 4)
  (attributes 2)
  (images "tiles/[tilegroup]/[tile].png")
  (editor-images "tiles/[tilegroup]/[tile]-editor.png")
)
```
If you want the tile to be invisible in game, you just remove the "(images)" section

---

In the following example, a basic set of tiles will be extracted from the image `tileset_example.png`.
The left tiles are solid ground with the rest of the tiles becoming various types of slopes.

To ignore a portion of an image (e.g. empty spaces), an ID of 0 is always being used in the appropriate places.

![tileset_example.png](images/tileset_example.png "An example image of a common tileset structure in SuperTux, with visible tile IDs")

To define a tile as a slope, its `attribute` must be set to either 16 or 17. You will also have to set an appropriate `data`
value to define the correct slope-type.

More on tile datas can be read [here](#tile-datas).

```
(tiles
  (width 11)
  (height 4)
  (ids
    10 11 12 19 20 21 22 27 28 31 35
    13 14 15 23 24 25 26 29 30 32 36
    16 17 18 0  0  0  0  0  0  33 37
    0  0  0  0  0  0  0  0  0  34 38)
  (attributes
    1 1 1 17 17 17 17 17 17 17 17
    1 1 1 17 17 17 17 17 17 17 17
    1 1 1 0  0  0  0  0  0  17 17
    0 0 0 0  0  0  0  0  0  17 17)
  (datas
    0 0 0 18 34 32 16 2 0 66 48
    0 0 0 33 17 19 35 1 3 50 64
    0 0 0 0  0  0  0  0 0 49 67
    0 0 0 0  0  0  0  0 0 65 51)
  (image "tiles/[tilegroup]/tileset_example.png")
)
```

Tile Attributes
===============

A tile can have the following attributes:

| Attribute  | Value           | Description                                         | Data section                                                        |
|------------|-----------------|-----------------------------------------------------|---------------------------------------------------------------------|
| solid      | `0x0001` / 1    | Tile collision that is solid / walkable             |                                                                     |
| unisolid   | `0x0002` / 2    | Changes the tile collision to be only detected from one side. | Unisolid side. `0` = up / `1` = down / `2` = left / `3` = right. |
| slope      | `0x0010` / 16   | Changes the tile collision to be a slope            | Type of slope. [See below](#slope-types) for possible values.       |
| ice        | `0x0100` / 256  | Changes the tile collision to make it slippery.     |                                                                     |
| water      | `0x0200` / 512  | Tile collision that is liquid / swimmable.          |                                                                     |
| harmful    | `0x0400` / 1024 | Tile collision that hurts the player when touched.  |                                                                     |
| glowing    | `0x0800` / 2048 | The tile emits a softly pulsating light. The light becomes red if the tile is harmful. |                                  |
| walljump   | `0x1000` / 4096 | The tile is walljump-able.                          |                                                                     |

Attribute Combinations
----------------------
A tile can have multiple attributes on it by adding the values together.
Some attributes may not work alone in a tile (i.e: unisolid, slope and ice), as they modify the tile collision instead of defining it.
That being known, it is important to combine different tile attributes in order of making the tile behave as you want it to.

Attribute combination examples:

| Combination   | Value           | Added Values                    | Description                                     |Data section |
|---------------|-----------------|---------------------------------|-------------------------------------------------|-------------|
| unisolid tile | `0x0003` / 3    | `0x0001 + 0x0002` / 1 + 2       | The tile is solid, but only from one side.      | Unisolid side. `0` = up / `1` = down / `2` = left / `3` = right. |
| solid slope   | `0x0011` / 17   | `0x0001 + 0x0010` / 1 + 16      | The tile is a walkable slope, solid from all sides. | Type of slope. [See below](#slope-types) for possible values. |
| unisolid slope | `0x0013` / 19  | `0x0001 + 0x0002 + 0x0010` / 1 + 2 + 16 | The tile is a walkable slope, only solid from one side. | Type of slope. [See below](#slope-types) for possible values. |
| ice tile      | `0x0101` / 257  | `0x0001 + 0x0100` / 1 + 256     | The tile is fully solid and slippery.           |             |
| unisolid ice tile | `0x0103` / 259 | `0x0001 + 0x0002 + 0x0100` / 1 + 2 + 256 | The tile is solid from one side and slippery. | Unisolid side. `0` = up / `1` = down / `2` = left / `3` = right. |
| ice slope     | `0x0111` / 273  | `0x0001 + 0x0010 + 0x0100` / 1 + 16 + 256 | The tile is a fully solid, slippery slope.| Type of slope. [See below](#slope-types) for possible values. |
| unisolid ice slope | `0x0113` / 275 | `0x0001 + 0x0002 + 0x0010 + 0x0100` / 1 + 2 + 16 + 256 | The tile is a slippery slope, solid only from one side. | Type of slope. [See below](#slope-types) for possible values. |
| water slope   | `0x0210` / 528 | `0x0010 + 0x0200` / 16 + 512     | The tile is swimmable but only at the area of a slope. | Type of slope. [See below](#slope-types) for possible values. |
| harmful unisolid | `0x0402` / 1026 | `0x0002 + 0x0400` / 2 + 1024 | The tile hurts the player, but only if touched from a certain side. | Unisolid side. `0` = up / `1` = down / `2` = left / `3` = right. |
| harmful slope | `0x0410` / 1040 | `0x0400 + 0x0010` / 16 + 1024   | The tile hurts the player, but only at the area of a slope. | Type of slope. [See below](#slope-types) for possible values. |
| harmful water | `0x0600` / 1280 | `0x0400 + 0x0800` / 512 + 1024  | The tile is swimmable and hurts the player.     |             |
| light block   | `0x0801` / 2049 | `0x0001 + 0x0800` / 1 + 2048    | The tile is solid and emits light.              |             |
| fire          | `0x0C00` / 3072 | `0x0400 + 0x0800` / 1024 + 2048 | The tile hurts the player and emits a red light. |            |
| lava          | `0x0E00` / 3584 | `0x0200 + 0x0400 + 0x0800` / 512 + 1024 + 2048 | The tile is swimmable, hurts the player and emits a red light. | |

You can try as many different combinations as you want, the ones above are only examples of what you can do.

Deprecated Attributes
---------------------

Some attributes that were used to make a tile have a special behavior don't seem to be working on current builds of the game, as they were replaced by the possibility of creating object tiles.
[See here](#adding-objects-as-tiles) the guide for adding objects as tiles.

| Attribute | Value          | Description |
|-----------|----------------|-------------|
| brick     | `0x0004` / 4   | The tile would act as a brick that could be destroyed by hitting it in different ways. |
| goal      | `0x0008` / 8   | The tile would finish the level when touched, with data `0` triggering end sequence and data `1` finishing instantly. |
| fullbox   | `0x0020` / 32  | The tile would act as Bonus Block, with datas `1` to `5` defining its content. |
| coin      | `0x0040` / 64  | The tile would act as a coin. |
| ???       | `0x0080` / 128 | This attribute doesn't seem to do anything at all. |

Tile Datas
==========

Each tile definition can have a `datas` section. This section is used when the yes/no-information
usually stored in the `attributes` definition isn't appropriate for the type of information.
Currently, this section is only used to store slope angles and unisolid sides.

Each type of information stored in the data section needs to reserve a range of values for itself.
The slope information, for example, uses the values zero through 67 (64+3), so the mask is at least
`0x007f`. To allow for future extension, the mask `0x00ff` has been reserved.

| Name              | Mask                          | Meaning                                                                                |
|-------------------|-------------------------------|----------------------------------------------------------------------------------------|
| Slope information | `0x00ff` (actually: `0x0073`) | Valid only when the tile has a collision attribute set. See [slope types](#slope-types) below. |
| Unisolid side | `0x0003` | Valid only when the tile has a collision attribute set. `0` = up / `1` = down / `2` = left / `3` = right. |

Slope Types
-----------

![](images/aatriangletypes2.png "All types of slopes supported by SuperTux")
![](images/Slope-data.png "Circle showing the 20 different valid slope data values")

The **deformation** means the following:

| Name    | Value | Meaning                                  |
|---------|-------|------------------------------------------|
| Deform1 | 16    | Only the lower half of the tile is used. |
| Deform2 | 32    | Only the upper half of the tile is used. |
| Deform3 | 48    | Only the left half of the tile is used.  |
| Deform4 | 64    | Only the right half of the tile is used. |

The important part is that the deformation determines which part of the tile is used and
not the actual **form** of the tile. For example, the `0+48` tile is a (steep, south-west)
**triangle**, while `2+48` is a (steep, south-east) **trapezoid**.

---

Adding Your Own Tiles
=====================

You want to contribute new tiles to the main game or just add custom tilesets for your own levels?
This next portion will show how to do so.

You can simply add new tiles with the help of a text editor of your choice. You can now either add
new tiles to the main file `tiles.strf` or create your own should you only seek to use custom tiles.
In that case create a new file and end it with `.strf`!

At first glance a tileset file can look quite intimidating. But worry not. In its core it is not that
bad. The following steps will show you how everything works in a more controlled environment. The SuperTux
tileset file is quite big, which makes it look more complicated than it is.

Step 1: Initial Preparations
----------------------------

To prepare your new file it is important to set it up the right way, so the game can read it properly
*(This step can be skipped if you want to add your tiles to `tiles.strf`)*.

**Before you begin adding your tile entries, your file should look like this:**

```
(supertux-tiles
)
```

Step 2: Adding Tiles
--------------------

Next, you can start adding your tiles one by one. In this example we are adding one tile entry for some
solid tiles and another one for some slopes.

Which tiles you include in one entry is fully up to you. Technically, you could also combine both tile
entries into one big tile entry. But for simplicity and better readability it is advised to make separations!

```
(supertux-tiles
  (tiles
    (width 3)
    (height 3)
    (ids
      1 2 3
      4 5 6
      7 8 9)
    (attributes
      1 1 1
      1 1 1
      1 1 1)
    (image "tiles/[tilegroup]/[tiles1].png")
  )
  (tiles
    (width 4)
    (height 6)
    (ids
      10 11 12 13
      14 15 16 17
      18 19 22 23
      20 21 24 25
      0  0  26 27
      0  0  28 29)
    (attributes
      17 17 17 17
      17 17 17 17
      17 17 17 17
      17 17 17 17
      0  0  17 17
      0  0  17 17)
    (datas
      18 34 32 16
      33 17 19 35
      2  0  66 48
      1  3  50 64
      0  0  49 67
      0  0  65 51)
    (image "tiles/[tilegroup]/[tiles2].png")
  )
)
```

Step 3: Adding Tilegroups
-------------------------

To create a tilegroup which lists all of your new tiles, you must add an `tilegroup` entry. Try categorizing
your tiles by themes (e.g. Snow, Forest, etc.) so you don't have to search for all your tiles in one single
tilegroup.

```
(supertux-tiles
  (tilegroup
    (name (_ "My Tilegroup"))
    (tiles
      1  2  3  0
      4  5  6  0
      7  8  9  0
      10 11 12 13
      14 15 16 17
      18 19 22 23
      20 21 24 25
      0  0  26 27
      0  0  28 29)
  )
  
  (tiles
    (width 3)
    (height 3)
    (ids
      1 2 3
      4 5 6
      7 8 9)
    (attributes
      1 1 1
      1 1 1
      1 1 1)
    (image "tiles/[tilegroup]/[tiles1].png")
  )
  (tiles
    (width 4)
    (height 6)
    (ids
      10 11 12 13
      14 15 16 17
      18 19 22 23
      20 21 24 25
      0  0  26 27
      0  0  28 29)
    (attributes
      17 17 17 17
      17 17 17 17
      17 17 17 17
      17 17 17 17
      0  0  17 17
      0  0  17 17)
    (datas
      18 34 32 16
      33 17 19 35
      2  0  66 48
      1  3  50 64
      0  0  49 67
      0  0  65 51)
    (image "tiles/[tilegroup]/[tiles2].png")
  )
)
```

Special Tiles
=============
Some tiles are special, as they turn into objects (i.e: Bonus Blocks, Coins and Bricks) when the level is loaded.

Adding Objects As Tiles
-----------------------

Special tiles can only be defined one by one, that meaning, you can't turn a larger image into multiple tiles.
Turning a tile into an object is done by adding an `object-name` and an `object-data` within the `tile`
The general structure for adding a special tile in your tileset is the following:
```
(tile
    (id [your tile ID])
    (images
      "objects/[object]/[object].png"
    )
    (object-name "[object class name]")
    (object-data "
      ([propriety1] 50)
      ([propriety2] \"[string]\")
    ")
)
```
Be aware that any object propriety that has quotation marks on it, must get a backslask (\) before any quotation marks, as they are quotation marks inside other quotation marks.

---
If you find it difficult to write the object proprieties you want to add as a tile, you can place this object in your level, open the level in a text editor and copy the information you'll find about this object, for example, if you want a Mr.Snowball, you get in the level file and search for it, you'll find:

```
(snowball
      (z-pos 52)
      (direction "left")
      (x 288)
      (y 128)
)
```
From this information, you may extract what you want to turn into a tile, you must ignore the x and y positions as they will be defined as where the tile is.

---
Let's turn that Mr. Snowball into a tile, then:

```
(tile
    (id 52)
    (images
      "creatures/snowball/snowball-0.png"
    )
    (object-name "snowball")
    (object-data "
      (z-pos 50)
      (direction \"left\")
    ")
)
```
---
For another example, here is a rock added as a tile:

```
(tile
    (id 53)
    (object-name "rock")
    (images
      "objects/rock/rock.png"
    )   
)
```
---
Now, a not-portable trampoline as a tile:

```
(tile
    (id 54)
    (images
      "objects/trampoline/trampoline2-0.png"
    )
    (object-name "trampoline")
    (object-data "
      (type \"stationary\")
      (z-pos 50)
    ")
)
```
---
Now let's be creative, let's say you want to add a bonus block that is orange and has 2 Mr.Icecubes inside it:

```
(tile
    (id 55)
    (images
      "objects/bonus_block/orange-0.png"
    )
    (object-name "bonusblock")
    (object-data "
      (type \"orange\")
      (z-pos 51)
      (custom-contents
        (mriceblock
          (z-pos 50)
        )
      )
      (count 2)
      (contents \"custom\")
    ")
)
```
Again, if you feel confused with what information you must type in the object name and data sections, you can copy them from an object that's already placed in your level file!

---

And that is all! Go open / create a new level in the Level Editor and select your tileset file in the Level
Properties and see if your tiles and / or tilegroups appear in the tiles menu.

---

Tileset Manager
---------------

**WARNING**: *Unfortunately the tilemanage application is broken at the moment and does not work
correctly! You'll destroy several tile attributes like slopes and some of the tiles created from
multiple images, when opening and saving a tileset with the editor!*

We provide an easy to use editor to make this task easier (especially extracting regions of bigger images).
You can find it in the `tools/tilemanager` directory. It's a `mono/gtk\#` app so you have
to have these 2 things installed and should invoke make in that directory then. It'll create
`tilemanager.exe` which you can then start with mono like this:

```mono tilemanager.exe```

NOTE: You should be careful when choosing tile ids to not overwrite existing tiles. You should
also keep in mind that existing levels will break if you change tile numbers later (the levels
just save a big a list of numbers that reference the tile file).

Trickery
--------

Note that some tiles aren't actually used in-game. Right after the level is loaded, various
tiles in the solid tilemaps are replaced with objects. These include all with the coin, fullbox,
brick, or goal attributes, and tile id 112 (invisible block). But the game doesn't end there.
It also adds light sources to torches and lava, which are then hidden unless the level uses a lightmap.
