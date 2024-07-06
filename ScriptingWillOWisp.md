> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `WillOWisp` that was given a name can be controlled by scripts

Instances
--------

A `WillOWisp` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [BadGuy](https://github.com/SuperTux/supertux/wiki/ScriptingBadGuy)
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener
* Portable
* GameObjectComponent
* [PathObject](https://github.com/SuperTux/supertux/wiki/ScriptingPathObject)


Methods
-------

Method | Explanation
-------|-------
`void set_state(string state)` | Sets the state of the WillOWisp<br /><br /> `state` - One of the following: "stopped", "move_path" (moves along a path), "move_path_track" (moves along a path but catches Tux when he is near), "normal" (starts tracking Tux when he is near enough), "vanish". 


Variables
---------

None.

Constants
---------

None.
