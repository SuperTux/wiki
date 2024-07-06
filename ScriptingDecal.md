> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Decal` that was given a name can be controlled by scripts.

Instances
--------

A `Decal` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

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
`void fade_sprite(string sprite, float time)` | Fades the decal sprite to a new one in `time` seconds
`void change_sprite(string sprite)` | **Deprecated!** Use `set_sprite()` instead!<br /><br />Changes the decal sprite
`void fade_in(float time)` | Fades in the decal in `time` seconds
`void fade_out(float time)` | Fades out the decal in `time` seconds


Variables
---------

None.

Constants
---------

None.
