The level format is a bit complex, which is why the [level editor](Editor_FAQ "wikilink") can prove itself very useful. If you are interested in how the levels look like or want to edit them manually (and find some of the parameters not self-explanatory enough), then you may read or skim through this section.

    (supertux-level                       ;; This initiates a level.

      (version 2)                         ;; This document only describes version 2. Version 1 is deprecated
                                          ;; and I'm not going to teach it since it lacks a lot of features.

      (name (_ "Some demo level"))        ;; Name of the level. Call it a nice name. Note that this should be
                                          ;; internationalised (that's why the extra underscore and brackets).

      (author "Ondra Hosek")              ;; Put your name here unless you are me (very improbable)
      
      (license "public domain")           ;; Choose under which license you wish this level to be redistributed.
                                          ;; You can basically type anything here. The presets are "GPL 2+ / CC-by-sa 3.0"
                                          ;; (both GNU GPL 2 or later and Creative Commons Attribution-ShareAlike 3.0)
                                          ;; and "non-redistributable" (all rights reserved). In the spirit of SuperTux,
                                          ;; we're politely asking you to allow redistribution, but it's your decision.

      (sector                             ;; A level is divided into independent sectors that can be connected
                                          ;; by doors or teleporters.

        (name "main")                     ;; Tux begins in the sector named "main".

        (music "ondraschipdisko.ogg")     ;; Name of the music file. See the data/music/ directory.

        (gravity 10.0)                    ;; Gravity of Tux. 10.0 is the default and sanest value (unless you
                                          ;; are ready to apply the level design correctly).

        (tilemap                          ;; Here come the tiles.
          (z-pos -100)                    ;; What layer the tilemap is supposed to be on. If you remember SuperTux 0.1,
                                          ;; "background" is now -100, "interactive" is 0 and "foreground" is 100.

          (solid  #f)                     ;; Will Tux collide with tiles in this tilemap?
                                          ;; Note: more than one tilemap can be solid per sector.

          (speed  1.0)                    ;; If the tilemap is solid, this has to be 1. Basically sets how
                                          ;; fast the tilemap scrolls horizontally.

          (speed-y 1.0)                   ;; Same, but vertical scrolling. If the tilemap is solid, this has to be 1.

          (width  5)                      ;; Number of tiles you plan to put in a row...
          (height 5)                      ;; ... and in a column. (5x5 is pretty tiny; small Tux
                                          ;; takes up 1x1 tiles, big Tux 1x2 tiles).

          (tiles                          ;; Integer lists of which tiles you want to use.
            0 0 0 0 0                     ;; The tiles and their numbers are defined in
            0 0 0 0 0                     ;; data/images/tiles.strf.
            0 0 0 0 0
            0 0 0 0 0
            0 0 0 0 0
          )
        )
        (tilemap
          (z-pos 0)
          (solid #t)
          ;; See the definition of layer -100. Tux will collide with the tiles in this tilemap.
        )
        (tilemap
          (z-pos 100)
          ;; ...
        )

        (camera-config                    ;; Definitions of the camera mode and paths

          (mode "autoscroll")             ;; This can be set to "normal" to deactivate
                                          ;; forced scrolling. Then you can omit the
                                          ;; "path" directive.

          (path                           ;; Forced scrolling path

            (mode "circular")             ;; "circular": A -> B -> C -> A -> ...
                                          ;; "ping-pong": A -> B -> C -> B -> A -> ...
                                          ;; "one-shot": A -> B -> C

            (xmode 1)                     ;; These two specify the feel of the camera.
            (ymode 1)                     ;; 1 is fix, 2 is Mario/Yoshi, 3 is Kirby
                                          ;; see src/objects/camera.cpp for special options

            (node (x 2) (y 3) (time 2))   ;; Point to which camera will scroll.

            (node
              ;; ...
            )
          )
        )

        (background
          (image "ocean.jpg")                ;; Background from data/images/background
          (speed 0.5)                        ;; Scrolling speed
          (speed-y 0.5)                      ;; Vertical scrolling speed
          (layer -100)                       ;; Which layer should the background scroll on?
          (image-top "arctis_top.jpg")       ;; Image at the top
          (image-bottom "arctis_bottom.jpg") ;; Image at the bottom
        )

        (spawnpoint                       ;; A spawning point for Tux. By default, he is
          (name "main")                   ;; spawned at spawnpoint named "main".
          (x 0)
          (y 0)
        )

        ;; THE FOLLOWING OBJECTS ARE OPTIONAL.
        (init-script "
    // A Squirrel script
    // See the scripting reference for more information.
    ")

        ;; Here you can add badguys of your choice.
        ;; Details on this can be read later in this chapter.

        ;; Particle systems
        ;; It is advisable only to use one particle system at a time.

        (particles-&lt;type&gt;                 ;; Valid values for &lt;type&gt; are rain, snow, comets, ghosts and clouds

          (layer 201)                     ;; -100 are background, 0 are interactive, 200 are foreground tiles.
                                          ;; Choose a number to put the rain between two layers. In this case,
                                          ;; the rain is in front of the foreground tiles. (see also
                                          ;; src/video/drawing_context.hpp)
        )

        (leveltime

          (time 300)                      ;; The player must complete this level
                                          ;; within 300 seconds.
        )
      ) ;; End of sector

      ;; You can add other sectors here.
    )
    ;; End of level

### Badguys

This section describes the various badguys and their parameters.

The next few sections describe the extra parameters for the other badguys.

#### Common parameters

    (&lt;badguy-name&gt;
      (x 270)                 ;; The badguy's X coordinate.
      (y 126)                 ;; The badguy's Y coordinate. (Note that the origin is in the top-left corner!)
      (dead-script "
    // A squirrel script that is executed once the badguy dies. Optional.
    ")
      (direction "auto")      ;; Direction in which the badguy will move after spawning. "left", "right" or "auto".
                              ;; Optional (except with some badguys).
    )

Angry Stones, Bouncing Snowballs, Fish, Flying Snowballs, Ghost Trees, Igels, Jumpies, Moles, Mr Bombs, Mr Iceblocks, Mr Rockets, Mr Trees, Plants, Poison Ivies, Skullyhops, Snails, Snowballs, Spider Mites, Spikies, Sleeping Spikies, Stalactites, Stumpies, Toads, Totems, Yeti Stalactites, Walking Leaves, Yetis and Zeeklings only require this list of parameters. Simply substitute <badguy-name> with one of the following:

-   `angrystone`
-   `bouncingsnowball`
-   `fish`
-   `flyingsnowball`
-   `ghosttree`
-   `igel`
-   `jumpy`
-   `mole`
-   `mrbomb`
-   `mriceblock`
-   `mrrocket`
-   `mrtree`
-   `plant`
-   `poisonivy`
-   `skullyhop`
-   `snail`
-   `snowball`
-   `spidermite`
-   `spiky`
-   `sspiky`
-   `stalactite`
-   `stumpy`
-   `toad`
-   `totem`
-   `yeti`
-   `yeti_stalactite`
-   `walkingleaf`
-   `zeekling`

#### Dart trap

    (darttrap
      (initial-delay 3)       ;; How long to wait after being activated before starting to shoot?
      (fire-delay 3)          ;; How long to wait between shots?
      (ammo -1)               ;; How many shots do we have? (-1 is infinity)
      (direction "left")      ;; This common parameter is NOT optional with the dart trap.
    )

#### Dispenser

    (dispenser
      (cycle 3)               ;; How often should a badguy be dispensed?
      
      (badguy random)         ;; Valid values are "snowball", "bouncingsnowball", "mrbomb",
                              ;; "mriceblock", "mrrocket", "poisonivy", "skullyhop", "snail", or "random".
    )

#### Flame

    (flame
      (radius 3)              ;; How big should the radius of the circle be that the flame
                              ;; follows?
      
      (speed 10)              ;; How fast should the flame be?
    )

#### Lightning orb

The lightning orb (`kugelblitz`) ignores the `y` coordinate, spawning above the visible screen.

#### Mr. Rocket

`direction` is not optional.

#### Spike

Don't mistake this badguy for Spiky! Spiky is the snowball-like creature with spikes, whilst a spike is an object serving the same purpose like the stalactite.

    (spike
      (direction 2)           ;; 0: north, 1: south, 2: west, 3: east
    )

#### Will-o-Wisp

    (willowisp
      (sector "main")         ;; Sector to teleport player into when touched
      (spawnpoint "willo1")   ;; Spawnpoint to teleport player to
      (name "wisp1")          ;; Name for scripting control
      (flyspeed 3)            ;; Speed at which wisp flies towards player
      (track-range 30)        ;; How near must the player be to be followed?
      (vanish-range 60)       ;; How far must the player be for the wisp to vanish?
      (running #f)            ;; Should we follow a preset path?
      (path
        ;; Path to follow if running is true. See the path in camera-config for the syntax.
      )
    )