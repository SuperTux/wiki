The SuperTux game engine is structured as follows:

1.  On startup, [main.cpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/main.cpp) instantiates a single MainLoop ([mainloop.cpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/mainloop.cpp)) that is run until the application terminates.
2.  The MainLoop manages, updates and draws all Screens, Controllers, Menus and the [Console](Console "wikilink").

:\*A Screen ([screen.hpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/screen.hpp)) is the abstract base class for code that the MainLoop runs exclusively and full-screen.

  
Probably the most important Screen is the GameSession ([game\_session.cpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/game_session.cpp)), which actually runs a Level ([level.cpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/level.cpp)).

Examples of other Screens are:

1.  The SuperTux title screen ([title.cpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/title.cpp))
2.  a world map ([world.cpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/world.cpp))
3.  an intro text scroller ([textscroller.cpp](http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/textscroller.cpp))

<!-- -->

  
A GameSession loads and runs a single Level, which consists of multiple, separate parts, the Sectors. Sectors contain the various GameObjects that can be encountered in SuperTux.

Examples of such GameObjects are the [Badguys](Badguys "wikilink"), Players and TileMaps, but also Thunderstorm controllers, the currently visible viewport (i.e. a Camera object), the sector's time limit, etc.

More in-depth information about the game engine can be found in the source code itself, e.g. as [Doxygen HTML Documentation](http://supertux.lethargik.org/development/doxygen/html/), or on pages in [:Category:Game Engine](:Category:Game_Engine "wikilink"), most notably:

-   [File formats](File_formats "wikilink") and [File Formats](:Category:File_Formats "wikilink")
-   [Collision detection](Collision_detection "wikilink")
-   [Tile](Tile "wikilink")
-   [Objects](Objects "wikilink")