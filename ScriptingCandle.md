> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Candle` that was given a name can be controlled by scripts.

Instances
--------

A `Candle` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener


Methods
-------

Method | Explanation
-------|-------
`void puff_smoke()` | Spawns a puff of smoke
`bool get_burning()` | Returns `true` if the candle is lit up
`void set_burning(bool burning)` | Sets the burning state of the candle<br /><br /> `burning` - If `true`, the candle is lit up. If `false`, it's extinguished. 


Variables
---------

None.

Constants
---------

None.
