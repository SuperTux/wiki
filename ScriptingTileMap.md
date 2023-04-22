> Note: This file is auto-generated from the [SuperTux scripting interface source code](https://github.com/SuperTux/supertux/tree/master/src/scripting), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `TileMap` that was given a name can be controlled by scripts.

Instance
--------

A `TileMap` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Methods
-------

Method | Explanation
-------|-------
`goto_node(int node_no)` | Moves the tilemap along a path until at given node, then stops. 
`start_moving()` | Starts moving the tilemap. 
`stop_moving()` | Stops the tilemap at the next node. 
`get_tile_id(int x, int y)` | Returns the ID of the tile at the given coordinates or 0 if out of bounds. The origin is at the top left. 
`get_tile_id_at(float x, float y)` | Returns the ID of the tile at the given position (in-world coordinates). 
`change(int x, int y, int newtile)` | Changes the tile at the given coordinates to `newtile`. The origin is at the top left. 
`change_at(float x, float y, int newtile)` | Changes the tile at the given position (in-world coordinates) to `newtile`. 
`fade(float alpha, float time)` | Starts fading the tilemap to the opacity given by `alpha`. Destination opacity will be reached after `time` seconds. Also influences solidity. 
`tint_fade(float time, float red, float green, float blue, float alpha)` | Starts fading the tilemap to tint given by RGBA. Destination opacity will be reached after `time` seconds. Doesn't influence solidity. 
`set_alpha(float alpha)` | Instantly switches the tilemap's opacity to `alpha`. Also influences solidity. 
`get_alpha()` | Returns the tilemap's opacity. <br /><br /> Note that while the tilemap is fading in or out, this will return the current alpha value, not the target alpha. 
`set_solid(bool solid)` | Switches the tilemap's real solidity to `solid`. <br /><br /> Note that the effective solidity is also influenced by the alpha of the tilemap. 


Constants
---------

None.
