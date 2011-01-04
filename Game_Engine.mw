The SuperTux game engine is structured as follows:

# On startup, [http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/main.cpp main.cpp] instantiates a single MainLoop ([http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/mainloop.cpp mainloop.cpp]) that is run until the application terminates.
# The MainLoop manages, updates and draws all Screens, Controllers, Menus and the [[Console]].
:*A Screen ([http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/screen.hpp screen.hpp]) is the abstract base class for code that the MainLoop runs exclusively and full-screen.
:Probably the most important Screen is the GameSession ([http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/game_session.cpp game_session.cpp]), which actually runs a Level ([http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/level.cpp level.cpp]).
:Examples of other Screens are:
:# The SuperTux title screen ([http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/title.cpp title.cpp])
:# a world map ([http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/world.cpp world.cpp])
:# an intro text scroller ([http://supertux.lethargik.org/svn/supertux/trunk/supertux/src/textscroller.cpp textscroller.cpp])

:A GameSession loads and runs a single Level, which consists of multiple, separate parts, the Sectors. Sectors contain the various GameObjects that can be encountered in SuperTux.
:Examples of such GameObjects are the [[Badguys]], Players and TileMaps, but also Thunderstorm controllers, the currently visible viewport (i.e. a Camera object), the sector's time limit, etc.

More in-depth information about the game engine can be found in the source code itself, e.g. as [http://supertux.lethargik.org/development/doxygen/html/ Doxygen HTML Documentation], or on pages in [[:Category:Game Engine]], most notably:

* [[File formats]] and [[:Category:File Formats|File Formats]]
* [[Collision detection]]
* [[Tile]]
* [[Objects]]

[[Category:Game Engine]]
