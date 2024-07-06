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
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* [PathObject](https://github.com/SuperTux/supertux/wiki/ScriptingPathObject)


Methods
-------

Method | Explanation
-------|-------
`void set_solid(bool solid)` | Switches the tilemap's real solidity to `solid`
`int get_tile_id(int x, int y)` | Returns the ID of the tile at the given coordinates or 0 if out of bounds
`int get_tile_id_at(float x, float y)` | Returns the ID of the tile at the given position (in world coordinates)
`void change(int x, int y, int newtile)` | Changes the tile at the given coordinates to `newtile`
`void change_at(float x, float y, int newtile)` | Changes the tile at the given position (in-world coordinates) to `newtile`
`void change_all(int oldtile, int newtile)` | Changes all tiles with the given ID
`void fade(float alpha, float time)` | Starts fading the tilemap to the opacity given by `alpha`
`void tint_fade(float time, float red, float green, float blue, float alpha)` | Starts fading the tilemap to tint given by RGBA
`void set_alpha(float alpha)` | Instantly switches the tilemap's opacity to `alpha`
`float get_alpha()` | Returns the tilemap's opacity


Variables
---------

None.

Constants
---------

None.
