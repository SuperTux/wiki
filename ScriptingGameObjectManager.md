> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

This class provides basic controlling functions for a sector.

Instance
--------

For in-level sectors, an instance under `sector.settings` is available from scripts and the console.

For worldmap sectors, such instance is available under `worldmap.settings`. 

Methods
-------

Method | Explanation
-------|-------
`set_ambient_light(float red, float green, float blue)` | Sets the sector's ambient light to the specified color. 
`fade_to_ambient_light(float red, float green, float blue, float fadetime)` | Fades to a specified ambient light color in `fadetime` seconds. 
`get_ambient_red()` | Returns the red channel of the ambient light color. 
`get_ambient_green()` | Returns the green channel of the ambient light color. 
`get_ambient_blue()` | Returns the blue channel of the ambient light color. 
`set_music(string music)` | Sets the sector's music. <br /><br /> `music` - Full filename, relative to the "music" folder. 
`add_object(string class_name, string name, int posX, int posY, string direction, string data)` | Adds a `MovingObject` to the manager. Note: If adding objects to a worldmap sector, `posX` and `posY` have to be tile positions (sector position / 32). <br /><br /> `class_name` - GameObject's class. <br /> `name` - Name of the created object. <br /> `posX` - X position inside the current sector. <br /> `posY` - Y position inside the current sector. <br /> `direction` - Direction. <br /> `data` - Additional data in S-Expression format (check object definitions in level files). 


Constants
---------

None.
