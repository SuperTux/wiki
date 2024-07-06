> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides basic controlling functions for a sector

Instances
--------

For in-level sectors, an instance under `sector.settings` is available from scripts and the console.

For worldmap sectors, such instance is available under `worldmap.settings`.

Inheritance
--------

The following classes inherit functions and variables from this class:
* [Sector](https://github.com/SuperTux/supertux/wiki/ScriptingSector)
* WorldMapSector


Methods
-------

Method | Explanation
-------|-------
`void set_ambient_light(float red, float green, float blue)` | Sets the sector's ambient light to the specified color
`void fade_to_ambient_light(float red, float green, float blue, float fadetime)` | Fades to a specified ambient light color in `fadetime` seconds
`float get_ambient_red()` | Returns the red channel of the ambient light color
`float get_ambient_green()` | Returns the green channel of the ambient light color
`float get_ambient_blue()` | Returns the blue channel of the ambient light color
`void set_music(string music)` | Sets the sector's music<br /><br /> `music` - Full filename, relative to the "music" folder. 
`void add_object(string class_name, string name, float pos_x, float pos_y, string direction, string data)` | Adds a `MovingObject` to the manager<br /><br /> `class_name` - GameObject's class. <br /> `name` - Name of the created object. <br /> `pos_x` - X position inside the current sector. <br /> `pos_y` - Y position inside the current sector. <br /> `direction` - Direction. <br /> `data` - Additional data in S-Expression format (check object definitions in level files). 


Variables
---------

None.

Constants
---------

None.
