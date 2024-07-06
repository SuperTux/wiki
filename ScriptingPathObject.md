> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A base class for all objects that contain, or make use of a path

Instances
--------

None.

Inheritance
--------

The following classes inherit functions and variables from this class:
* [Camera](https://github.com/SuperTux/supertux/wiki/ScriptingCamera)
* Coin
* Ghoul
* HeavyCoin
* HurtingPlatform
* Platform
* [TileMap](https://github.com/SuperTux/supertux/wiki/ScriptingTileMap)
* [WillOWisp](https://github.com/SuperTux/supertux/wiki/ScriptingWillOWisp)


Methods
-------

Method | Explanation
-------|-------
`void goto_node(int node_idx)` | Moves the path object until at given node, then stops
`void set_node(int node_idx)` | Jumps instantly to the given node
`void start_moving()` | Starts moving the path object automatically
`void stop_moving()` | Stops moving the path object


Variables
---------

None.

Constants
---------

None.
