> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides additional controlling functions for a worldmap sector, other than the ones listed at [GameObjectManager](https://github.com/SuperTux/supertux/wiki/ScriptingGameObjectManager). 

Instances
--------

An instance under `worldmap.settings` is available from scripts and the console. 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* Base::Sector
* [GameObjectManager](https://github.com/SuperTux/supertux/wiki/ScriptingGameObjectManager)


Methods
-------

Method | Explanation
-------|-------
`float get_tux_x()` | Returns Tux's X position on the worldmap. 
`float get_tux_y()` | Returns Tux's Y position on the worldmap. 
`void set_sector(string sector)` | Changes the current sector of the worldmap to a specified new sector. 
`void spawn(string sector, string spawnpoint)` | Changes the current sector of the worldmap to a specified new sector, moving Tux to the specified spawnpoint. 
`void move_to_spawnpoint(string spawnpoint)` | Moves Tux to the specified spawnpoint. 
`string get_filename()` | Gets the path to the worldmap file. Useful for saving worldmap-specific data. 
`void set_title_level(string filename)` | Overrides the "Title Screen Level" property for the world with `filename`. The newly set level will be used for the title screen, after exiting the world. 


Variables
---------

None.

Constants
---------

None.
