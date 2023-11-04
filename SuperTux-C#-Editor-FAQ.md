> This is about the SuperTux C# Editor, **NOT** about the editor built into SuperTux

Generic
-------

### How do i find out if my level is good or not?

Ask somebody! There is an internet chat (we use [IRC](IRC "wikilink"))
that you can get on, show your level, and if you stick around for a few
minutes (it takes a little while to get noticed), they'll probably love
to tell you how good it is or isn't and what's right or wrong about it.
Now isn't that exciting?

Keep in mind that many people on `#supertux` have spent many hours
playing *SuperTux*. Therefore it is often hard for them to judge
difficulty of a level. If you have a sister, young cousin or son, they
may be a better judge with regard to difficulty.

Don't forget that if you're young, you should get your parent's
permission before getting on the webchat. Most people that get on our
webchat are nice, but that doesn't change that you need permission.

:   Join using [freenode
    Webchat](http://webchat.freenode.net/?randomnick=1&channels=supertux)
    or see [Contact\#IRC](Contact#IRC "wikilink").

Oh, and if your level is good enough, the third party fansite would ask
you if they can add it to the [player made
levels](http://www.beige-box.com/supertux/pml.html) area. Let's see some
levels! :)

### How do I install the new supertux-editor?

You have two options:

1.  From source through [Subversion](Download/Subversion "wikilink").
    1.  Choose the supertux-editor URL from the
        [listing](Download/Subversion#Locations_inside_the_Subversion_repository "wikilink")
        and checkout the repository:\
        **svn checkout
        http://supertux.lethargik.org/svn/supertux/trunk/supertux-editor**
    2.  Install the development versions of the [necessary
        dependencies](#What_do_I_need_to_compile_supertux-editor_SVN_edition.3F "wikilink").
        This requires you to know methods appropriate to your
        distribution or operating system.
    3.  Compile:\
        **cd supertux-editor**\
        **make**
2.  From a [binary package](Download#Level_Editor "wikilink") by MMlosh
    or for your distribution.

### What do I need to compile supertux-editor SVN edition?

You first need the supertux-editor package from the [Subversion
Repository](Download/Subversion "wikilink").

The following packages are required by the SVN supertux-editor at
runtime and buildtime:

-   gtk-sharp
-   glade-sharp
-   mono

The following packages are only needed at runtime:

-   libsdl
-   sdl-image
-   opengl
-   glu

Unix-specific dependencies:

-   make

Windows-specific dependencies:

-   Microsoft .net development program

Because of the interdependencies of these packages, you probably only
need to ask your package manager to install glade-sharp. Also, most unix
systems will have a good copy of make installed already.

[SVN version](Download/Subversion "wikilink")

### How do I move around in a level?

Click and drag with the middle mouse button.\
There are also scrollbars since r4886.

\

Tiles
-----

### How do I add tiles to a level

Click on the layer you want the tiles on and select the tile you want
from the Tiles Tool. Note: Tiles can be places only on “Tilemap” layers
(check property editor's title to ensure);

### How do I filter the tiles so I can find a specific one?

With the Tiles tool selected, there is a combo box above the pane with
all of the tiles in it. This combo box contains categories (called tile
groups) which filter what is displayed in the pane.

### How do I hide layers (tiles, background, objects..)?

Click on the small eye (![](images/EditorEyeIcon.png "fig:EditorEyeIcon.png"))
in the layer listing to adjust how hidden a layer is. Options are shown,
semitransparent, and hidden.

### How should I place the tiles for the end-level structures?

The best way to learn this is to look at existing levels. For the exit
tree in MS2 the best place to look at is levels/test/tree-exit.stl at
this point. Also note that using tiles for triggering the end sequence,
although still supported, is no longer necessary. See [What is the
SequenceTrigger object
for?](#What_is_the_SequenceTrigger_object_for? "wikilink")

### How do I add a new tilemap?

![](images/Tilemap.png "fig:Tilemap.png") Select the tilemap object and place
it like a normal object anywhere in the level. The result will be a new
that a new tilemap is created.\
Since r5427: Right-click any item in LayerList and select “Add”, this
will currently (8.5.2009) add only tilemaps, but it may contain a
sub-menu in the future.

\

Objects
-------

### How do I easily align an object to the grid?

Press the Control key while moving an object to snap to every 16 pixels.
Press the Shift key to snap to every 32 pixels.

### What is the SequenceTrigger object for?

![](images/Sequencetrigger.png "fig:Sequencetrigger.png") The SequenceTrigger
object is used to define the areas that start and stop the end sequence
(Tux walks into Igloo / Exit). The sequence names for that are
“endsequence” and “stoptux”, respectively. Also, you can use
“fireworks”.

### What is the SpawnPoint object for?

![](images/Spawnpoint.png "fig:Spawnpoint.png") The SpawnPoint object is used
to define places where Tux could “spawn”. This is used to mark where Tux
should start in the level, the destination of doors and more. The
spawnpoint where Tux will start on loading the level must be named
“main” and be in the sector called “main”.

### What is the Script object for?

![](images/Scripttrigger.png "fig:Scripttrigger.png") The script object is used
to define an occurrence which will happen when Tux enters the defined
area. To edit the script, click the 'Edit Script' button. For details
please see [Scripting reference](Scripting_reference "wikilink"). Some
examples of scripting:

#### Example: Moving platform

To move a moving platform: Change the platform's name. Example, Plat1.
Then in the script, type:

`Plat1.goto_node(#);`

The node the platform starts on is 0, then 1, et cetera. To make the
platform return:

`Plat1.goto_node(0);`

You can also make the platform go and return in one go.

`Plat1.goto_node(#);`\
`Plat1.goto_node(0);`

#### Example: Candle

To light candles: Change the candle's name. Example, Candle1. Untick the
'burning' box.

`Candle1.set_burning(true);`

The candle will light. To make a candle turn off, leave the candle
'burning' and type:

`Candle1.set_burning(false);`

#### Example: Waiting

A few more simple commands:

`wait(#);     (wait the specified number of seconds)`

And example of using wait:

```
Candle1.set_burning(true);
wait(0.1);
Candle2.set_burning(true);
wait(2);
Candle1.set_burning(false);
wait(0.1);
Candle2.set_burning(false);
```

The result of this will be that candle1 lights, followed by candle2 a
fraction of a second later. After two more seconds, candle1 and then
candle2 will go out.

### How do I change the background image?

Select “Background” in the sector objects view. There you can change
it's properties, including what picture(s) should be used for
background.\
Since r5769: Background image is present as “BG Image” in LayerList.
Click it.\
Since r5888: Background image is present as “Background IMG.”

Other tools
-----------

### How do I use brushes?

![](images/EditorBrushIcon.png "fig:EditorBrushIcon.png") Brushes are used to
clean up edge tiles. The brush tool does that by replacing a chosen 3x3
section of tiles with the best of several “good-looking” patterns stored
in so-called brushes. Keep that in mind when working with brushes - a
brush will never apply a pattern it does not know about.

There are already a few brushes in `trunk/supertux-sharp/data/brushes`
that know some valid patterns e.g. for earth tiles or snow tiles. Load
one in the level and then drag it over tiles to correct edge tiles of
rough tile “blocks”.

Note that the brushes are incomplete, so you might need to fix some
things manually. If you used a pattern a brush did not yet know, you can
add it to the list of known patterns by dragging a selection around the
new pattern(s) with your right mouse button. All patterns in the
selected region will be added to the list of valid patterns for the
currently loaded brush. Because patterns are currently 3x3 tiles in
size, your selection obviously has to be at least 3x3 tiles big. Also
don't forget to save the brush afterwards or your changes will be lost
when you deselect the brush.

To create a new brush you currently got to “train” an empty one:

1.  Make a level that looks good.
2.  Select the tilemap you placed those tiles in.
3.  Load the brush `trunk/supertux-sharp/data/brushes/empty.csv`
4.  Right click and drag to select the area to get tiles from.
    -   The minimum size for a selection that works is 3x3 tiles.
5.  When you are finished save the brush.

Note that a good brush would need several thousand patterns.

Sectors
-------

### Where are the sector tabs?

Near the top of the editor. The default sector in a level is called
“main” and is the sector where the game will start.

### How do I resize a sector?

Right click on the [tab for the
sector](#Where_are_the_sector_tabs? "wikilink") and select “Resize”.

### How do I create a new sector?

Right click at the [sector tab](#Where_are_the_sector_tabs? "wikilink")
area and select “New”.

### How do I delete a sector?

Right click at the [sector tab](#Where_are_the_sector_tabs? "wikilink")
for the current sector and select “Delete”.

Operating system specific notes
-------------------------------

### I'm on OpenSUSE and I get a message about that it couldn't load gtk-sharp

`Could not load file or assembly 'gtk-sharp, Version=2.10.0.0, `\
`Culture=neutral, PublicKeyToken=35e10195dab3c99f' or one of its dependencies.`

If you are on OpenSUSE and get a message like this you might want to try
[this](http://supertux.lethargik.org/bugs/view.php?id=211#481) and the
note directly below it as well.

We (the developers) are unable to reproduce the problem but we do not
use OpenSUSE. Try asking the OpenSUSE developers about what is going on
there.

### Does the editor work under Mac OS X?

Yes, it does, but the setup is complex; you will have to do the
following:

-   install Apple's X11
-   download and build Gtk and its dependencies (Glib, Pango, Cairo,
    Atk, Gdk and maybe more)
-   download and build Mono and GTK\#
-   install glew and boost via Mac port
-   download and build the editor

Since the Mono project doesn't pre-package Gtk\# and its dependencies
with the OS X installer, we are unable to provide a nice editor package.
Additionally, we offer no official support, so no one might be able to
help you on the mailing list if the editor crashes due to an OS
X-specific problem.

### Can the editor be run with Wine?

Unfortunately, since it needs mono/GTK, that would be pretty hard. The
editor relies on some programs, so it could not be without manually
installing the components.

:   Why run it in wine? Mono binaries run natively on Linux, too. Don't
    be confused by the .exe extension, just run it.
:   Because is really hard to run with mac without it. I would be nice
    just to be able to open it, no building necessary.
    [173.55.240.235](Special:Contributions/173.55.240.235 "wikilink")(Monstertux)

### Does the editor work under Microsoft Windows Vista?

Yes, but it requires a complete setup. you will have to compile some
GTK\# programs amongst other things. We are able to provide a package.

### SuperTux is slow when I test my level

Very common. You just need to make sure your out of the “Node Editor”
and switch to the tile editor.

:   There is no bug report about this so called “common problem”. Works
    fine on all systems I know about.
:   Well you must not have tested with the 0.3.0 mono one then. Its fine
    with the net version.

Bugs and Errors
---------------

[s=For any bug reports where please provide the **full backtrace** (if
one exists) when reporting at our
[bugtracker](http://supertux.lethargik.org/bugs/)](Template:Attention "wikilink")

### I get an error about “Object reference not set to an instance of an object”

This can be several things:

1.  Check that the paths to the supertux data directory and to supertux
    itself in the editor preferences are correct.
2.  If you run it under mono (unless you know that you don't do it, you
    probably do run it under mono) check that the mono version is at
    least [1.2.2.1](http://www.mono-project.com/Downloads).

**Note: That the Mono version with installation is not compatible with
the Level Editor.**

### I'm using Windows Vista or Windows 7, and the editor UI is really strange

This bug has been
[reported](https://supertux.lethargik.org/bugs/view.php?id=672) on the
bug tracker and will be fixed some time in the future.

### My bug is not listed above

If any of the above didn't solve the problem and you manage to recreate
the error, report the bug with at least this info:

-   Full backtrace
-   What you did to cause the bug
-   What OS and OS version you use
-   What versions of mono, the editor itself, GTK and GTK\# that you use

These types of bugs can not be solved without that info (and sometimes
we might need more details than that, so please check back at the bug
once day or so if there is any more info asked for).