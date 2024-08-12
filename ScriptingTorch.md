> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `Torch` that was given a name can be controlled by scripts.

Instances
--------

A `Torch` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

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
`bool get_burning()` | Returns `true` if the torch is burning.
`void set_burning(bool burning)` | Switches the burning state of the torch.


Variables
---------

Variable | Explanation
---------|---------
`bool burning` | Determines whether the torch is burning.


Constants
---------

None.
