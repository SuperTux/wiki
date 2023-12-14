> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides additional controlling functions for a worldmap sector, other than the ones listed at [GameObjectManager](https://github.com/SuperTux/supertux/wiki/ScriptingGameObjectManager).

Instance
--------

An instance under `worldmap.settings` is available from scripts and the console. 

Methods
-------

Method | Explanation
-------|-------
`get_tux_x()` | Gets Tux's X position on the worldmap. 
`get_tux_y()` | Gets Tux's Y position on the worldmap. 
`set_sector(string sector)` | Changes the current sector of the worldmap to a specified new sector. 
`spawn(string sector, string spawnpoint)` | Changes the current sector of the worldmap to a specified new sector, moving Tux to the specified spawnpoint. 
`move_to_spawnpoint(string spawnpoint)` | Moves Tux to a specified spawnpoint. 
`get_filename()` | Gets the path to the worldmap file. Useful for saving worldmap specific data. 
`set_title_level(string filename)` | Overrides the "Title Screen Level" property for the world with `filename`. The newly set level will be used for the title screen, after exiting the world. 


Constants
---------

None.
