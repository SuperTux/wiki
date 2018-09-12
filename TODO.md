> **Note:** This TODO is not to be used blindly. Use your brain and
> figure out which feature is most important and most practical to
> implement. Don't chase pie-in-the-sky ideas that you'll never get
> done. Also be aware that some of the items listed here might be out
> of date or not good ideas to begin with.

This is a centralized list of things that need to be done. It is
maintained by the SuperTux development team. It can include issues
that are outstanding, or resource requests. The document will also be
used to track decisions on these issues and requests.

Please have a look at our issue tracker on GitHub where you can also
find issues by `category:` tags (e.g.: `category:design` for
graphics/UX tasks, `category:code` for code tasks, and
`category:levels` for level design tasks).

### Artwork

#### New graphics needed

* A bonus block that acts as on/off switch

  - design proposal 1: featuring the [on/off symbols](https://www.shutterstock.com/image-illustration/electric-switch-icon-cartoon-illustration-web-579423751),
    a rollover animation between the states would be nice to have as well (cube tilting/rolling backwards)

  - design proposal 2: use the [powerswitch symbol](https://de.depositphotos.com/152581468/stock-illustration-power-switch-icon.html) instead and just have it grey'ish when off and bright red when on

#### Old graphics in need for cleanup/replacement

These graphics need to be cleaned up or replaced with better looking
ones. Style and color scheme should be kept more or less the same.

* Enlarge it to 1280x800, remove signature:

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/background/oiltux.jpg)

* In need of a little cleanup:

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/background/arcticskies1.png)
  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/background/bluemountain-middle.png)

* Don't match the style that well, could need a bit of smoothing:

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/background/bridgecloud-light.png)
  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/background/bridgecloud-dark.png)

* Regular stone block, currently lacking detail.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/blocks/block10.png)

* Regular stone block, currently lacking detail.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/blocks/block11.png)

* One trampoline is portable, the other is stationary. They should
  look more simialr, while still being distinguishable. Maybe make
  more use of vertical space for more springyness.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/objects/trampoline/trampoline1-0.png) ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/objects/trampoline/trampoline2-0.png)

* These blocks are meant to be iced and slippery versions of bigblock.png, block5.png and Co.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/blocks/icebridge.png)

* Too black in spots and sloppy boarders. Not enough detail.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/engine/menu/frame.png)

* Graphics is screwed up with vertical lines going through it.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/background/cloud.png)

* Placeholder gfx, actual background tileset needs to be more complex. Maybe not worth the effort, background graphics are simpler.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/background/snow-para-1.png)

* Placeholder gfx, actual background tileset needs to be more complex. Maybe not worth the effort, background graphics are simpler.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/background/snow-para-2.png)

* Flame could make use of animation (tiles are barely used, so not high priority)

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/background/backgroundtile3.png)

* Needs to be converted into a decal or completely replaced with a different kind of end sequence.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/goal/goal2-1.png)

* Some issues with tileability.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/nightcave/ground.png)

* Was intended as background graphics, but gets abused as foreground
  graphics. Might need new tile ids to back a backwards compatible
  cleanup.

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/crystalcave/ground.png)

* The whole `pole/` folder should be redone

  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/pole/cross.png)
  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/pole/bend.png)
  ![](https://raw.githubusercontent.com/SuperTux/supertux/master/data/images/tiles/pole/t-cross.png)

#### Cutscenes

- [ ] Intro: Picnic with Penny
  - [x] Make it look less like a level
  - [ ] Fix some minor issues with new version
- [ ] Antarctica part II
  - [ ] Interlude: Yeti
  - [ ] Interlude: Where is Penny?
  - [ ] Outro: Leaving Antarctica…

#### Graphics

- [ ] Sliding (Tux)
- [ ] Swimming (Tux)

##### Tiles

- Levels
  - Add tiles for deeper areas of modern lava (needed for castles)
  - Parallax background tiles (Milestone 1 castle, Snow Castle, Brown Castle, DFK Castle) that can be used in levels close to the castles
  - More background tiles (parallax background) such as those in Antarctica, but for (Ghost Forest)
  - Dead bushes
  - More variants of dead trees
  - Underground tiles (<https://github.com/SuperTux/data/issues/48>; Parallax background tiles, slopes, decoration, tiles that can be used to make a platform some tiles higher without having to end the platform and having to make a new one)
  - Fixed tiling for Snow and Brown Castle
  - Crystalcave tileset should be fixed to be usable
  - Waterfall graphics fitting to the new water type
  - Electrified version of new water
  - Add modern fluid style acid/poison (purple liquid)
  - Castle: Add tiles adapted to the location of the castle (example: upper right-hand corner of <http://supertux.lethargik.org/wiki/images/9/97/Forestworldoverview.jpg>)

- Worldmap
  - Dark forest worldmap tiles without river required for transition
  - Ghost Forest worldmap tiles matching the new, blue-grass style from the levels (Ghost Forest style from <http://supertux.lethargik.org/wiki/File:Forestworldoverview.jpg> will be used later for Wasteland, no need for that now)
  - Transition tiles from normal as well as dark forest to ghost forest
  - Mountain worldmap tiles, similar to those of Icy Island
  - "Slope" tiles for the worldmap too, to create an illusion of height on the Forest Island.
  - Small forest castle tiles (Snow/Brown castle variant as well as Dark Forest Keep castle variant) (already discussed before)
  - All castle tile variants in a smaller version, as a tower
  - "Also some decoration for the ghost forest worldmap: dead bushes and dead trees (or are we using those decals from the halloween worldmap?). The same for the forest in general. The tiles should have a transparant background, so you can use them everywhere, like the trees, slopes and edges of icy island, because some decoration tiles from forest and darker forest have a background of the land that they are placed on." ~ RustyBox
  - Forest cave/underground worldmap tiles

##### Backgrounds

- More diverse Ghost Forest backgrounds

##### Objects

- Badguys
  - MrIceBlock: waking graphics (see <https://github.com/SuperTux/supertux/pull/581>)
  - Ghost enemy (<http://supertux.lethargik.org/wiki/images/8/8b/Ghost-sprite.png>)

##### Meta

- Source files for all stuff?
- Clarify license? GPLv2+ only? CC-BY-SA what version only? Dual: GPLv2+ / CC-BY-SA Y.Z?

#### Levels

- [ ] Improved Forest World

### Code

- [ ] Comments: explain arbitary(?) constants in physics code
- [ ] Ghost enemy
- [ ] Sliding
- [ ] Swimming
  - [x] Basic code for moving in water tiles
  - [ ] How to move underwater?
  - [ ] Discuss: fluid simulation as game object rather than tiles?
- [ ] Coin: expose to scripting interface for path/movement settings
- [ ] HeavyCoin: expose to scripting interface to enable/disable effect of gravity

### Translations

Translations are always a very important part of the game. You can contribute
to them [on Transifex](https://www.transifex.com/arctic-games/supertux/).


TODO List
---------

This is a list of tasks and issues that might be worth to implement or fix. This list is however not an authorative list of things that must be done, its a collection of random things that pop up during development, therefore not everything in here might be well thought out or worth to implement. Use your brain before implementing anything on this list and always think about how useful a new feature would be in the context of the whole game or if a potential performance enhanchment, actually enhanchmes anything at all.

TODO List as of March of 2015
-----------------------------

### Translation Related Stuff

-   <http://supertux.lethargik.org/bugs/view.php?id=106>

### Graphic Related Stuff

-   make “downer” lava tiles for the newer lava graphics. WIP by Sydney.
-   Iced Cherry bomb graphics are ugly. <http://supertux.lethargik.org/bugs/view.php?id=1036> WIP by Sydney
-   Stone Tux graphics would be nice. Tobbi and Sydney tried but didn't get far. contact them if you want to see what they have so far. <http://supertux.lethargik.org/bugs/view.php?id=1072>
-   Tree Boss need Graphics improvement.

### Code Related Stuff

-   <https://github.com/SuperTuxTeam/supertux/issues/14>
-   <http://supertux.lethargik.org/bugs/view.php?id=1052>
-   <https://github.com/SuperTuxTeam/supertux/issues/24>

### Level Related Stuff

-   On going task, always WIP it seems. Mostly fixed though. <http://supertux.lethargik.org/bugs/view.php?id=1016>
-   Add ghost tree level: <http://supertux.lethargik.org/bugs/view.php?id=1037>

### Editor related Stuff

-   <http://supertux.lethargik.org/bugs/view.php?id=1066>
-   <http://supertux.lethargik.org/bugs/view.php?id=1056>
-   <http://supertux.lethargik.org/bugs/view.php?id=1055>

### Mailing List stuff

-   <http://supertux.lethargik.org/bugs/view.php?id=1073>

OLD TODO LIST
=============

Major Issue
-----------

-   Memory leaks : Assigned to Tobbi, fixed soon
-   See if anything is usefull in [Editor\_Ideas](Editor_Ideas "wikilink")
-   Make any editor working correctly

Minor Issue
-----------

### Internationalisation

-   -   Translation of menu and worlds [1](https://www.transifex.com/projects/p/supertux/)
    -   Font improve (needs feed back: arabic and cyrillic)

### Graphic Tasks

-   make downer tiles of lava flow
-   Frozen enemies
-   Consolidate/cleanup/organize image files and tilesets
-   Find a way to make the menu border work
-   A waterfall to match the new water look
-   Fix tiling issues


crystal cave tiles

brown castle tiles

some blue castle tiles

ghostly word

-   Fill out some of the new tilesets or remove (e.g. blue mtn.)
-   Animate some badguy deaths
-   LiveFire final sprite
-   Alternative candle sprites (animated background torches, glowing crystals, maybe a brazier/open flame, maybe a light bulb)
-   Need parallax versions of backgrounds (in forest)
-   Visual effects for willowisp warp and level flip
-   Fix Tux graphics ugliness (floating debris outside of Tux and transparent holes inside)
-   Replace airarrow with one that is both visible and isn't confusing (maybe a glowing sprite w/o Tux)
-   General icons for jump and action buttons, can be used on billboards and in keybinding menu

### Coding Task

-   Internationalization of add-on
-   Improve font support for diacritics
-   Code buttjumpable when frozen for spiky and jumpy
-   Code effect of Iceflower on forest badguys
-   Improve fish


it also looks weird when fish disappears in transparent water

start of the jump should depend on top of water- i.e. be dynamic for moving water tiles

-   the backflip billboard doesn't work if “jump with up” is not selected

### Sound effect

-   Splash effect when falling in water

Misc.
-----

From previous TODO list, some point should be rethink, or may have been corrected …

### Coding Standard Stuff

-   remove overuse of multi-inheritance
-   remove overuse of friend'ship
-   maybe mark interfaces as interfaces (ISerializable or SerializableInterface)
-   split files with multiple classes into multiple files with one class each
-   Decide what to do with magic constants of objects (static vs anonymous namespace vs lisp property)
-   check the code with Valgrind and profilers
-   use Vector in Physics for 'a' and 'v'
-   replace random generator with C++11 stuff
-   md5.hpp and random\_generator.hpp could go to external/
-   write/finish scripts to automatically:
    -   make all includes relative to top level dir
    -   sort includes (.hpp file, then system includes, then other project files)
    -   include guards proper and of the form HEADER\_SUPERTUX\_${PATH\_TO\_FILE}\_HPP
    -   remove trailing whitespace

### Suggesions

-   more moving directories around?
    -   addon/
    -   audio/
    -   control/
    -   gui/
    -   lisp/
    -   math/
    -   physfs/
    -   sprite/
    -   util/
    -   video/
    -   squirrel/ - for generic squirrel code
    -   supertux/
        -   worldmap/
        -   trigger/
        -   scripting/ - for scripting wrapper code
        -   badguy/
        -   object/
-   implement a system that allows to attach comments to specific regions in a level
-   implement a tool to “screenshot” a complete level
-   GameObject::RemoveListenerListEntry: Ughs, somebody trying to implement a list class within in the GameObject?!
-   add --datadir DIR (data/) and --userdir DIR (~/.supertux/), allow multiple --datadir's
-   make gravity constant-&gt; To be discussed…
-   rename Vector -&gt; Vector2f
-   get rid of SCREEN\_WIDTH/SCREEN\_HEIGHT overuse, give them a proper name at least -&gt; to think when upgrading to SDL2
-   resolution menu entry moves the wrong way around
-   having dictionary\_manager in Lisp is extremely ugly
-   enforce proper naming of files to match their class (SomeClass -&gt; some\_class.?pp or so)
-   file naming is inconsistent: some times we use '\_' to separate words, sometimes we don't
-   implement PNG screenshot
-   having hitbox in Sprite is fugly
-   add code that compares the last Log line with the current, if they are the same reject them and just output something like:

` ** last line has been repeated X times`

-   implement: <http://standards.freedesktop.org/basedir-spec/basedir-spec-0.6.html>
-   peaking up/down doesn't work properly
-   peaking left/right should make Tux look into that direction (up/down to, needs new sprites)
-   cleanup scripting interface
-   replace cloud tiles with decals
-   add support for automatic scrolling backgrounds
-   add direct reading of Vector2f to Reader/lisp
-   refactor Camera code, break ugly long functions into pieces and such
-   allow fully custom magnification levels from command line (maybe GUI to if there is a proper/easy way to let the user enter numbers) (--magnification or -g WIDTHxHEIGHT:ASPECTX:ASPECTY@MAGNIFICATION)
-   use AnchorPoint in Background instead of Alignment
-   allow gradients to parallax scroll like Background (make it optional)
-   add multicolored gradients (see Windstille source code, which can deal with Gimp gradients)
-   fix alpha blending in the SDL renderer, currently all sprites (Tux, etc.) appear transparent
-   shadow font glyphs bleed into other glyphs
-   sprite/sprite.cpp: frame should never get out of range:

` if((int)frame >= get_frames() || (int)frame < 0)`
`   log_warning << "frame out of range: " << (int)frame << `“`/`”` << get_frames() << " at " << get_name() << `“`/`”` << get_action() << std::endl;`

-   Surface::hflip() is used exactly once, should probally be part of the constructor

### Scenegraph and Physics Engine Restructuring

-   random idea to restructure engine stuff (might lead to nicer code and easier scriptability (and a need to rewrite lots of stuff...):

   class SomeBadGuy : public PhysicsCallbackListener // or use boost::function
   {
   private:
         PhysicsPtr box;
         SpritePtr sprite;

   public:
         SomeBadGuy(Engine& engine)
         {
            box    = engine.physics().create_box(Rectf(0,0,32,32));
            box->register_listener(this);
            sprite = engine.graphics().create_and_add_sprite(“Foobar”);
         }

         void update(float delta)
         {
            // not much to do, as most stuff is done internally in the engine
            if (dead)
            {
                     sprite->replace_with(“Foobar_dead”);
            }
            else
            {
                   sprite->hide();
                   sprite->set_pos(box->get_pos());
           }
         }

         // no more draw(), done by the scene graph

         void on_collision(CollisionData data)
         {
           // respond
         }
   };

Random Notes
------------

-   calculate the size of an background image that should fill the screen:

     image_size = (1 - parallax_speed) * screen_size + level_size * parallax_speed

`def calc(parallax, screen, tiles):`
`   return (1 - parallax) * screen + parallax * tiles * 32`

Whats the point in adding new features while the existing features and badguys can't be used due to lack of images or animations?

As long as all these points haven't been fixed, Milestone 2 will not be considered as Stable, so won't be released.

Supported Resolutions
---------------------

SuperTux shall support resolutions from 640x480 to 1280x800 at a magnification of 1x. For resolutions higher, such as 2560x1600, upscaling will be used. For resolutions smaller, like 320x240 downscaling will be used.

Higher resolution graphics for 2x maginification might be provided. Lower res graphics for 0.5x maginification might be provided as well.

Resolution and magnification can be freely configured by the user within the given limits.

In tiles this means we have 40x25 (=1280x800px) tiles per screen.

Music Recode
------------

Currently the music makes up a large chunk of the total tarball size. Compression could fix this:

      ,-- Size of data/music/*.ogg
      V
    40MB - Current quality in SVN
    24MB - Default oggenc quality (3)
    14MB - oggenc at 0 quality
    10MB - oggenc at -1 quality

> No audible difference on my sound setup.
> -- grumbel

TODO
----

Milestone 2
===========

Documents and ideas: [Milestone 2](Milestone_2 "wikilink") esp. [World 2](World_2 "wikilink")

Notes
-----

Apart from issues listed here, [:Category:Needs Code](:Category:Needs_Code "wikilink"), [:Category:Needs Sound](:Category:Needs_Sound "wikilink") and [:Category:Needs Graphics](:Category:Needs_Graphics "wikilink") list articles that describe content which still lacks one of the three. Bugs can be found in our [bug tracker](http://supertux.lethargik.org/bugs).

Game Tasks
----------

### Current

#### Integration/Organisation

-   integrate new bomb sprite, remove the old
-   integrate new green pipe
-   make list of ugly titles that need replacement
-   remove the helper-tiles in levels where enemies should be stay-on-platform

#### Graphics

-   repaint dead-iceblock
-   redraw underground ice tileset
-   design a new ice-castle titleset
-   design enemies that fit into a ice-castle

#### Coding

-   make submenus look different then clickable menu items
-   implement threading in netbrush-server (needed so that new users don't bring the session to a crawl)
-   make lisp reader get(name, bool) handle 0/1 as bool instead of fail
-   getting stuck under a tile as large-tux shouldn't harm you, just unstuck you

#### Input

-   implement wiimote support (easily done with cwiid), should be \#ifdef'ed out if library doesn't exit or better dlopen the library at runtime
-   check that joystick code works with analogsticks properly and fix where necessary

#### Bugs

-   german umlauts seem to be broken when switching the language in game
-   In special levels, such as ones were tux walks upside down or levels where the camera moves at a constant speed, spawning at a checkpoint causes tux to die immediately. (Mac OS X Version)

### Future

-   add paralax scrolling to all levels
-   remove old water from levels (bridge levels)

Editor
------

(The editor is not release critical therefore no ratings for these TODOS)

-   Scroll TileList with middle mouse, Get different Tilegroups

    Isn't that the way it is atm? --[WolfgangB](User#wolfgangb "wikilink") 18:23, 7 Aug 2006 (BST)


    Only if one tilegroup is selected, with default group (empty string) you can't scroll, once you have set it to “All” or anything else you can. Should be bug (or feature) in GTK, it's not controlled by program.

-   Create an overview widget (where to place this in the GUI?)

    Overview for what? -- [Penguinmaster](User#penma "wikilink") 15:46, 4 Oct 2006 (CEST)


    The sector. Like a minimap.

-   Grab Mouse Pointer when scrolling so that we can scroll as much as we want (and the mouse is still where it was before scrolling)

    I don't think that would be a good idea. I at least found that applications that does that are hard to use. --[AnMaster](User#anmaster "wikilink") 10:46, 13 Nov 2006 (CET)

-   More custom property editors:
    -   Texts
    -   Scripts (we had a very good gtksourceview based editor which is disabled at the moment, maybe split the editor to a separate dll and load different editors on demand?)

        Why was it disabled? --[WolfgangB](User#wolfgangb "wikilink") 16:45, 13 Jul 2006 (BST)


        Because it crash the editor on Windows, and because it add lots of extra deps. --[AnMaster](User#anmaster "wikilink") 23:27, 20 Jul 2006 (BST)


        “lots of extra deps” anything that is not part of every serious distro? Why not fix the crash instead of removing features?
-   Layer switching on keys 1,2,3,...,0 CTRL+1,2,3,...,0 to switch visibility, key 0 for objects
-   Editor has strange behaviour when you select a tile in the middle, right-click select and move the mouse too much to the right
-   Tool not working after loading new level

    Added a workaround for this by resetting to the Select tool when loading new level. --[AnMaster](User#anmaster "wikilink") 20:25, 8 Sep 2006 (BST)

-   Windows builds seem to silently crash when loading huge levels

    huge as in 100x100 or more like 10000x10000?


    the level old world2/airkey.stl crashed both editor and the game itself on windows. --[AnMaster](User#anmaster "wikilink") 17:56, 30 Jun 2006 (BST)


    the old airkey was 300x300. It makes the editor slow on my Linux box but it's working--[WolfgangB](User#wolfgangb "wikilink") 00:14, 6 Jul 2006 (BST)


    The editor crashes on windows certainly. It stops also responding very often. I think it's partly windows, wich causes the crash. --[Yaniel](User#yaniel "wikilink")

-   Make the right click menu from sector tab a normal menu so that users can easily find it

    Maybe add them to a toolbar? that could be useful. --[AnMaster](User#anmaster "wikilink") 23:27, 20 Jul 2006 (BST)

-   Add a new way to copy parts of one level to another.

<Category:Development>
