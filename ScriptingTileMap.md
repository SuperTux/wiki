> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `TileMap` that was given a name can be controlled by scripts. The tilemap can be moved by specifying a path for it. 

Instances
--------

A `TileMap` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* LayerObject
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* [PathObject](https://github.com/SuperTux/supertux/wiki/ScriptingPathObject)


Methods
-------

Method | Explanation
-------|-------
`void set_solid(bool solid = true)` | Switches the tilemap's real solidity to `solid`.<br /><br /> <br /><br />**NOTE:** The effective solidity is also influenced by the alpha of the tilemap. 
`bool get_solid()` | Returns the effective solidity of the tilemap. 
`int get_tile_id(int x, int y)` | Returns the ID of the tile at the given coordinates or 0 if out of bounds. The origin is at the top left. 
`int get_tile_id_at(float x, float y)` | Returns the ID of the tile at the given position (in world coordinates). 
`void change(int x, int y, int newtile)` | Changes the tile at the given coordinates to `newtile`. The origin is at the top left. 
`void change_at(float x, float y, int newtile)` | Changes the tile at the given position (in-world coordinates) to `newtile`. 
`void change_all(int oldtile, int newtile)` | Changes all tiles with the given ID. 
`void fade(float alpha, float time)` | Starts fading the tilemap to the opacity given by `alpha`. Destination opacity will be reached after `time` seconds. Also influences solidity. 
`void tint_fade(float time, float red, float green, float blue, float alpha)` | Starts fading the tilemap to tint given by RGBA. Destination opacity will be reached after `time` seconds. Doesn't influence solidity. 
`void set_alpha(float alpha)` | Instantly switches the tilemap's opacity to `alpha`. Also influences solidity. 
`float get_alpha()` | Returns the tilemap's opacity.<br /><br /> <br /><br />**NOTE:** While the tilemap is fading in or out, this will return the current alpha value, not the target alpha. 


Variables
---------

Variable | Explanation
---------|---------
`bool solid` | Equivalent to `get_solid()` and `set_solid()`. 
`float alpha` | Determines the tilemap's current opacity. requested tilemap opacity 


Constants
---------

None.
